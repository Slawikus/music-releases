from django.shortcuts import render


def handle404(request, exception=None):
    return render(request, 'error_handlers/404.html', status=404)


def handle403(request, exception=None):
    return render(request, 'error_handlers/403.html', status=403)


def handle500(request, exception=None):
    return render(request, 'error_handlers/500.html', status=500)
