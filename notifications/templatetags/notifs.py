from django import template
from notifications.models import Notification
register = template.Library()

@register.simple_tag(takes_context=True)
def number_of_unread_notifications(context):
	user = context["user"]
	return Notification.objects.unread_by(profile=user.profile).count()


@register.simple_tag(takes_context=True)
def last_file_notifications(context):
	user = context["user"]
	notifications = Notification.objects.unread_by(profile=user.profile)
	return notifications[:5]
