from django.db import models


# Create your models here.
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
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Short label description',
    )
    def __str__(self):
        return self.name
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'profile'],
                name='unique_label_per_profile'
            ),
        ]