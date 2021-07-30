from django.urls import path

from .views import CreateReleaseView, AllReleaseView, UpcomingReleasesView, RecentlyReleasedView


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('all/', AllReleaseView.as_view(), name='all_releases'),
    path("upcoming/", UpcomingReleasesView.as_view(), name="upcoming"),
    path("recently-released/", RecentlyReleasedView.as_view(), name='recently_released')

]
