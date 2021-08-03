from django.urls import path
from django.conf.urls import url

from .views import (CreateReleaseView, AllReleaseView, MyReleasesView,  submit_release, SubmitReleaseView,
                    UpcomingReleasesView, RecentlySubmittedView, EditReleaseView)


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('', AllReleaseView.as_view(), name='all_releases'),
    url("upcoming/", UpcomingReleasesView.as_view(), name="upcoming_releases"),
    path("recently-submitted/", RecentlySubmittedView.as_view(), name='recently_submitted'),    
    path("my-releases/", MyReleasesView.as_view(), name='my_releases'),
    path("<int:pk>/submit/", submit_release, name='submit_release'),
    path("<int:pk>/edit/", EditReleaseView.as_view(), name='edit_release'),
]
