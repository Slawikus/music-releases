from django.urls import path

from .views import (CreateReleaseView, AllReleaseView, UpcomingReleasesView, 
RecentlyReleasedView, SubmitReleaseView, DetailReleaseView)


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('submit/<int:pk>/', SubmitReleaseView.as_view(), name='release_submit'),
    path('<int:pk>/', DetailReleaseView.as_view(), name='release_detail'),
    path('all/', AllReleaseView.as_view(), name='all_releases'),
    path("upcoming/", UpcomingReleasesView.as_view(), name="upcoming"),
    path("recently-released/", RecentlyReleasedView.as_view(), name='recently_released')

]
