from django.db import models


class NotificationManager(models.Manager):
    def unread_by(self, profile):
        return self.filter(profile=profile).filter(is_viewed=False)
