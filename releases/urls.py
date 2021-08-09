from django.urls import path
from django.conf.urls import url

from .views import (CreateReleaseView, AllReleaseView, MyReleasesView, ImportReleasesView,
                    UpcomingReleasesView, RecentlySubmittedView, EditReleaseView, get_example_excel)


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('', AllReleaseView.as_view(), name='all_releases'),
    url("upcoming/", UpcomingReleasesView.as_view(), name="upcoming_releases"),
    path("recently-submitted/", RecentlySubmittedView.as_view(), name='recently_submitted'),    
    path("my-releases/", MyReleasesView.as_view(), name='my_releases'),
    path("edit-release/<int:pk>", EditReleaseView.as_view(), name='edit_release'),
    path("import-releases/", ImportReleasesView.as_view(), name="import_releases"),
    path("example-excel/", get_example_excel, name='get_example_excel')
]
