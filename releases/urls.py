from django.urls import path

from .views import CreateReleaseView, SubmitReleaseView, DetailReleaseView


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('submit/<int:pk>/', SubmitReleaseView.as_view(), name='release_submit'),
    path('<int:pk>/', DetailReleaseView.as_view(), name='release_detail'),
]
