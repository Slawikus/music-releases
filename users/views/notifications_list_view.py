from django.views.generic import ListView
from notifications.models import Notification


class NotificationsListView(ListView):
	model = Notification
	template_name = 'profile/notifications_list.html'
	context_object_name = 'notifications'

	def get_queryset(self):
		return Notification.objects.filter(profile=self.request.user.profile)
