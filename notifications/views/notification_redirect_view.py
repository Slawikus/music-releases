from django.views.generic import View
from django.http import HttpResponseRedirect
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

from public_tradelist.models import TradeRequest
from band_submissions.models import BandSubmission
import re


class NotificationRedirectView(LoginRequiredMixin, View):
	def get(self, request, pk):
		notification = get_object_or_404(Notification, id=pk)
		# parse primary key from url
		target_pk = int(re.findall(r'\d+', notification.target_url)[0])

		target = (TradeRequest.objects.filter(pk=target_pk) or
				  BandSubmission.objects.filter(pk=target_pk))[0]

		# if user does not own trade request or band submission forbid
		if request.user != target.profile.user:
			return HttpResponseForbidden("redirect forbidden")

		notification.is_viewed = True
		notification.save()

		return HttpResponseRedirect(notification.target_url)
