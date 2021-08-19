from .models import Release
from django.http import JsonResponse


def get_band_name(request, query):
    result = []
    if query:
        releases = Release.objects.filter(band_name__istartswith=query)

        for release in releases:
            result.append(release.band_name)

    return JsonResponse(result, safe=False)
