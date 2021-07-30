from django.urls import path

from .views import CreateReleaseView, ListReleaseView


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('all/', ListReleaseView.as_view(), name='release_list')
]
