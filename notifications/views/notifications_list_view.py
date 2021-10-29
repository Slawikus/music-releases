from django.views.generic import ListView
from notifications.models import Notification
from django.contrib.auth.mixins import LoginRequiredMixin


class NotificationListView(LoginRequiredMixin, ListView):
	model = Notification
	context_object_name = "notifications"
	template_name = "notifications_list.html"

	def get_queryset(self):
		return Notification.objects.\
			filter(profile=self.request.user.profile).\
			filter(is_viewed=False).\
			order_by("-created")
