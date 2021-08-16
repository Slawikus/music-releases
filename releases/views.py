from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.utils.timezone import datetime
from django.contrib import messages

from .forms import CreateReleaseForm, UpdateTradesAndWholesaleForm, CreateWholesalePriceForm, UpdateReleaseForm, ImportReleaseForm
from .models import Release, WholesaleAndTrades, ReleaseWholesalePrice
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
                                             submitted_at__gte=datetime.today(),
                                             ).order_by("-submitted_at")


class RecentlySubmittedView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Recently Submitted Releases"
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             submitted_at__lte=datetime.today(),
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
        release_currencies = ReleaseWholesalePrice.objects.values('price', 'currency__currency', 'release')\
            .filter(release=self.kwargs.get('pk'))
        context.update({'release_currencies': release_currencies})

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
        kwargs['profile'] = self.request.user.profile
        kwargs['release'] = Release.objects.get(id=self.kwargs.get('pk'))
        return kwargs

    def get_success_url(self):
        wholesale_and_trades = WholesaleAndTrades.objects.get(id=self.kwargs.get('pk'))
        return reverse('wholesale_and_trades_edit', args=[wholesale_and_trades.pk])

    def test_func(self):
        obj = Release.objects.get(id=self.kwargs.get('pk'))
        return obj.profile == self.request.user.profile


class DeleteWholesalePriceView(DeleteView):
    model = ReleaseWholesalePrice


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
