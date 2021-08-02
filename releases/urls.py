from django.urls import path
from django.conf.urls import url

from .views import (CreateReleaseView, AllReleaseView, MyReleasesView, 
                    UpcomingReleasesView, RecentlySubmittedView, EditReleaseView)

from .excel import get_excel_file


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('', AllReleaseView.as_view(), name='all_releases'),
    url("upcoming/", UpcomingReleasesView.as_view(), name="upcoming_releases"),
    path("recently-submitted/", RecentlySubmittedView.as_view(), name='recently_submitted'),    
    path("my-releases/", MyReleasesView.as_view(), name='my_releases'),
    path("edit-release/<int:pk>", EditReleaseView.as_view(), name='edit_release'),
    path("excel/", get_excel_file, name="excel")
]
