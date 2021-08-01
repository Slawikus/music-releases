import django_filters
from .models import Release

class ReleaseFilter(django_filters.FilterSet):

    FORMATS = (
        ("CD", 'CD'),
        ("Vinyl", "Vinyl"),
        ("Tape", "Tape"),
        ("DVD", "DVD")
    )

    format = django_filters.ChoiceFilter(choices=FORMATS, method='filter_by_format')

    def filter_by_format(self, queryset, name, value):

        return queryset.filter(format=value)

    class Meta:

        model = Release
        fields = ["base_style", "submitted_at"]