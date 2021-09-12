from django.views.generic import ListView
from notifications.models import Notification


class NotificationListView(ListView):
	model = Notification
	context_object_name = "notifications"
	template_name = "notifications_list.html"

	def get_queryset(self):
		return Notification.objects.filter(profile=self.request.user.profile)
