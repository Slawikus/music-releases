from django.urls import path
from django.conf.urls import url

from .views import CreateReleaseView, AllReleaseView, MyReleasesView, UpcomingReleasesView, RecentlyReleasedView, publish_release


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    url('all/', AllReleaseView.as_view(), name='all_releases'),
    url("upcoming/", UpcomingReleasesView.as_view(), name="upcoming"),
    url("recently-released/", RecentlyReleasedView.as_view(), name='recently_released'),
    
    url("my_releases/", MyReleasesView.as_view(), name='my_releases'),
    path("publish/<int:pk>", publish_release, name='publish'),
]
