from django import template

register = template.Library()

@register.filter
def notifs_amount(user):
	return user.profile.notifications.filter(is_viewed=False).count()


@register.filter
def notifs_list(user):
	notifications = user.profile.notifications.filter(is_viewed=False)
	return notifications[:5]