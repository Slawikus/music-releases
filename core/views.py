from django.shortcuts import render
from django.db.models import Count

from labels.models import Label
from releases.models import Release
from public_tradelist.models import TradeRequest
from trades.models import UserTradeRequest


# Create your views here.
def handle404(request, exception=None):
	return render(request, 'error_handlers/404.html', status=404)

def handle403(request, exception=None):
	return render(request, 'error_handlers/403.html', status=403)

def handle500(request, exception=None):
	return render(request, 'error_handlers/500.html', status=500)

def dashboard(request):
	context = {}
	context["labels"] = Label.objects.count()
	context["releases"] = Release.objects.count()
	context["trades"] = TradeRequest.objects.count() + UserTradeRequest.objects.count()
	context["recent_releases"] = Release.objects.order_by("-submitted_at")[:3]
	context["biggest_labels"] = Label.objects.all().annotate(rel_amount=Count('releases')).order_by('-rel_amount')[:3]

	return render(request, 'home.html', context)
