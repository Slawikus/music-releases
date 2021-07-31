from django.urls import path

from .views import CreateReleaseView, SubmitReleaseView


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('submit/<int:pk>/', SubmitReleaseView.as_view(), name='release_submit'),
]
