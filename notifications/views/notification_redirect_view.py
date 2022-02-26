from django.views.generic import View
from django.http import HttpResponseRedirect
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin


class NotificationRedirectView(LoginRequiredMixin, View):
    def get(self, request, pk):
        notification = get_object_or_404(Notification, id=pk)

        if request.user != notification.profile.user:
            return HttpResponseForbidden("redirect forbidden")

        notification.is_viewed = True
        notification.save()

        return HttpResponseRedirect(notification.target_url)
