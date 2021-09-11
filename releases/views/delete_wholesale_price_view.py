from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from django.urls import reverse

from releases.models import ReleaseWholesalePrice


class DeleteWholesalePriceView(DeleteView):
    model = ReleaseWholesalePrice

    def delete(self, request, *args, **kwargs):
        wholesale_price = ReleaseWholesalePrice.objects.get(pk=self.kwargs.get("pk"))
        wholesale_price.delete()
        return HttpResponseRedirect(reverse('release_wholesale_price_add', args=[wholesale_price.release.pk]))