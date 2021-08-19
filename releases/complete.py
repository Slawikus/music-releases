from .models import Release
from django.http import JsonResponse, HttpResponseForbidden


def get_band_name(request, query):

    if not request.user.is_authenticated:
        return HttpResponseForbidden

    result = []
    releases = Release.objects.filter(band_name__istartswith=query)
    for release in releases:
        result.append(release.band_name)

    return JsonResponse(result, safe=False)
