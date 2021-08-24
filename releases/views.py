from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.utils import timezone

from .forms import CreateReleaseForm, UpdateTradesAndWholesaleForm, CreateWholesalePriceForm, UpdateReleaseForm, \
    ImportReleaseForm, UpdateMarketingInfosForm
from .models import Release, WholesaleAndTrades, ReleaseWholesalePrice, MarketingInfos
from .filters import ReleaseFilter
from .excel import save_excel_file


class CreateReleaseView(LoginRequiredMixin, CreateView):
    model = Release
    template_name = 'release_add.html'
    form_class = CreateReleaseForm
    success_url = reverse_lazy('my_releases')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs


class SubmitReleaseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Release
    fields = ['is_submitted']
    login_url = 'login'
    success_url = reverse_lazy('all_releases')

    def form_valid(self, form):
        form.instance.is_submitted = True
        form.instance.submitted_at = timezone.datetime.now()
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user.profile


class EditReleaseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Release
    form_class = UpdateReleaseForm
    template_name = "edit_release.html"
    success_url = reverse_lazy("my_releases")

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user.profile

    def get_success_url(self):
        return reverse('edit_release', args=[self.object.pk])


class BaseRelease(LoginRequiredMixin, ListView):
    context_object_name = "releases"

    template_name = "release_list.html"
    model = Release


class AllReleaseView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Releases"
        return context

    def get_queryset(self):
        return Release.objects.filter(is_submitted=True)


class UpcomingReleasesView(LoginRequiredMixin, ListView):
    template_name = "upcoming.html"
    model = Release

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ReleaseFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             submitted_at__gte=timezone.now(),
                                             ).order_by("-submitted_at")


class RecentlySubmittedView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Recently Submitted Releases"
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             submitted_at__lte=timezone.now(),
                                             ).order_by("-submitted_at")


class MyReleasesView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My Releases"
        return context

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile).order_by("-submitted_at")


class UpdateWholesaleAndTradesView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WholesaleAndTrades
    form_class = UpdateTradesAndWholesaleForm
    template_name = 'release_trades_wholesale.html'
    login_url = 'login'
    context_object_name = 'wholesale_and_trades'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        release_wholesale_prices = ReleaseWholesalePrice.objects.select_related('currency').filter(
            release=Release.objects.get(wholesaleandtrades=self.kwargs.get('pk')))
        context.update({'release_wholesale_prices': release_wholesale_prices})

        return context

    def get_success_url(self):
        return reverse('wholesale_and_trades_edit', args=[self.object.pk])

    def test_func(self):
        obj = self.get_object()
        return obj.release.profile == self.request.user.profile


class CreateWholesalePriceView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ReleaseWholesalePrice
    template_name = 'wholesale_price_add.html'
    form_class = CreateWholesalePriceForm
    login_url = 'login'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.release = Release.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['release'] = Release.objects.get(id=self.kwargs.get('pk'))
        return kwargs

    def get_success_url(self):
        wholesale_and_trades = WholesaleAndTrades.objects.get(release=self.kwargs.get('pk'))
        return reverse('wholesale_and_trades_edit', args=[wholesale_and_trades.pk])

    def test_func(self):
        obj = Release.objects.get(id=self.kwargs.get('pk'))
        return obj.profile == self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['release'] = Release.objects.get(id=self.kwargs.get('pk'))
        context['release_wholesale_prices'] = ReleaseWholesalePrice.objects.filter(release=context['release'])
        return context


class DeleteWholesalePriceView(DeleteView):
    model = ReleaseWholesalePrice

    def delete(self, request, *args, **kwargs):
        wholesale_price = ReleaseWholesalePrice.objects.get(pk=self.kwargs.get("pk"))
        wholesale_price.delete()
        return HttpResponseRedirect(reverse('release_wholesale_price_add', args=[wholesale_price.release.pk]))


class UpdateWholesaleAndTradesView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WholesaleAndTrades
    form_class = UpdateTradesAndWholesaleForm
    template_name = 'release_trades_wholesale.html'
    login_url = 'login'
    context_object_name = 'wholesale_and_trades'

    def dispatch(self, request, *args, **kwargs):
        self.release = get_object_or_404(Release, pk=self.kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        release = self.release
        release_wholesale_prices = ReleaseWholesalePrice.objects.select_related('currency').filter(release=self.release)
        context.update(
            {
                'release_wholesale_prices': release_wholesale_prices,
                'release': release
            }
        )

        return context

    def get_success_url(self):
        return reverse('wholesale_and_trades_edit', args=[self.release.pk])

    def test_func(self):
        obj = self.get_object()
        return obj.release.profile == self.request.user.profile

    def get_object(self, queryset=None):
        return self.release.wholesaleandtrades


class CreateWholesalePriceView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ReleaseWholesalePrice
    template_name = 'wholesale_price_add.html'
    form_class = CreateWholesalePriceForm
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        self.release = get_object_or_404(Release, pk=self.kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.release = self.release
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['release'] = self.release
        return kwargs

    def get_success_url(self):
        return reverse('release_wholesale_price_add', args=[self.release.pk])

    def test_func(self):
        obj = self.release
        return obj.profile == self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'release_wholesale_prices': ReleaseWholesalePrice.objects.filter(release=self.release),
                'release': self.release
            }
        )
        return context


class ImportReleasesView(LoginRequiredMixin, FormView):
    template_name = "upload_release.html"
    form_class = ImportReleaseForm
    success_url = reverse_lazy("my_releases")

    def form_valid(self, form):
        file = form.cleaned_data.get("file")
        profile = self.request.user.profile
        import_error = save_excel_file(file, profile)
        # if result contains any error
        if import_error:
            messages.error(self.request, import_error)
            return self.render_to_response(
                self.get_context_data(request=self.request, form=form)
            )
        else:
            return super().form_valid(form)


class UpdateMarketingInfosView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MarketingInfos
    form_class = UpdateMarketingInfosForm
    template_name = 'marketing_infos_edit.html'
    login_url = 'login'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        self.release = get_object_or_404(Release, pk=self.kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('marketing_infos_edit', args=[self.release.pk])

    def test_func(self):
        obj = self.get_object()
        return obj.release.profile == self.request.user.profile

    def get_object(self, queryset=None):
        return self.release.marketinginfos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['release'] = self.release
        return context
