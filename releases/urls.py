from django.urls import path

from .views import CreateReleaseView


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
]
