from django.db import models
from django.db.models import Q

from configuration.file_storage import DuplicationFixFileSystemStorage


class Label(models.Model):
    profile = models.ForeignKey(
        "users.Profile",
        on_delete=models.CASCADE,
        related_name='labels'
    )
    name = models.CharField(
        max_length=250,
        verbose_name='Label name',
        help_text='Label name as you write on your releases',
    )
    logo = models.ImageField(
        upload_to='images/labels/',
        blank=True,
        null=True,
        verbose_name='Label logo',
        help_text='For best result - black logo on white or transparent background',
        storage=DuplicationFixFileSystemStorage()
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Short label description',
    )
    is_main = models.BooleanField(
        default=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'profile'],
                name='unique_label_per_profile'
            ),
            models.UniqueConstraint(
                fields=['profile'],
                condition=Q(is_main=True),
                name='unique_main_label_per_profile'
            ),
        ]
        ordering = ['-is_main']

    def __str__(self):
        return self.name

    def belongs_to_user(self, user):
        return self.profile == user.profile
