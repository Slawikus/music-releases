from django.views.generic import View
from django.http import HttpResponseRedirect
from notifications.models import Notification
from django.shortcuts import get_object_or_404


class NotificationRedirectView(View):
	def get(self, request, id):
		notification = get_object_or_404(Notification, id=id)
		notification.is_viewed = True
		notification.save()

		return HttpResponseRedirect(notification.url)
