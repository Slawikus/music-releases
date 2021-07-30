from django.urls import path

from .views import CreateReleaseView, AllReleaseView, RecentlyAddedView, UpcomingReleasesView, RecentlyReleasedView, publish_release


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('all/', AllReleaseView.as_view(), name='all_releases'),
    path("upcoming/", UpcomingReleasesView.as_view(), name="upcoming"),
    path("recently-released/", RecentlyReleasedView.as_view(), name='recently_released'),
    path("recently-released/<str:format>", RecentlyReleasedView.as_view(), name='recently_released'),
    path("recently-added/", RecentlyAddedView.as_view(), name="recently_added"),
    path("publish/<int:pk>", publish_release, name='publish')
]
