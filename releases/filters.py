import django_filters
from .models import Release

class ReleaseFilter(django_filters.FilterSet):

    class Meta:

        model = Release
        fields = ["format", "base_style", "submitted_at"]
