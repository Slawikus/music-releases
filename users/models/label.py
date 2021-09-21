from django.db import models
from configuration.file_storage import DuplicationFixFileSystemStorage


class Label(models.Model):
    profile = models.ForeignKey(
        "users.Profile",
        on_delete=models.CASCADE,
        related_name='label'
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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'profile'],
                name='unique_label_per_profile'
            ),
        ]

    def __str__(self):
        return self.name
