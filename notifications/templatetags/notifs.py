from django import template
from notifications.models import Notification
register = template.Library()

@register.filter
def number_of_unread_notifications(user):
	return Notification.objects.unread_by(profile=user.profile).count()


@register.filter
def last_five_notifications(user):
	notifications = Notification.objects.unread_by(profile=user.profile)
	return notifications[:5]
