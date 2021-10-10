from django.shortcuts import render

# Create your views here.
def handle404(request, exception=None):
	return render(request, 'error_handlers/404.html')

def handle403(request, exception=None):
	return render(request, 'error_handlers/403.html')

def handle500(request, exception=None):
	return render(request, 'error_handlers/500.html')
