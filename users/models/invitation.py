from django.db import models
import uuid


class Invitation(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="invitations")
    is_active = models.BooleanField(default=True)
