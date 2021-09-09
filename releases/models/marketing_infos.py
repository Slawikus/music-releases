from django.db import models


class MarketingInfos(models.Model):
    release = models.OneToOneField("releases.Release", on_delete=models.CASCADE)
    style = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        help_text='“Marketing” style of the release, i.e. instead of Black Metal -> Ethnic Black Metal from Sri Lanka'
    )
    release_overview = models.TextField(null=True, blank=True)
    youtube_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='YouTube URL',
        help_text='Link to video teaser or complete track from the release'
    )
    soundcloud_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='SoundCloud URL',
        help_text='Link to audio teaser or complete track from the release'
    )
    press_feedback = models.TextField(null=True, blank=True)
