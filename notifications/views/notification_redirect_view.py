from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.models import Notification
from django.shortcuts import get_object_or_404


class NotificationRedirectView(LoginRequiredMixin, View):
	def get(self, request, pk):
		notification = get_object_or_404(Notification, id=pk)
		notification.is_viewed = True
		notification.save()

		return HttpResponseRedirect(notification.target_url)
