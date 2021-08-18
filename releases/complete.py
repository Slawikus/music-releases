from dal import autocomplete
from .models import Release


class BandNameAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        if not self.request.user.is_authenticated:
            return Release.objects.none()

        qs = Release.objects.all()

        if self.q:
            qs = qs.filter(band_name__istartswith=self.q)

        return qs
