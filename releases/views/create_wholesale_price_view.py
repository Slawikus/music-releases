from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.urls import  reverse
from releases.forms import CreateWholesalePriceForm
from releases.models import Release, ReleaseWholesalePrice


class CreateWholesalePriceView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ReleaseWholesalePrice
    template_name = 'release/wholesale_price_add.html'
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

