from django.urls import path
from django.conf.urls import url

from .views import CreateReleaseView, AllReleaseView, MyReleasesView, UpcomingReleasesView, RecentlySubmittedView, \
    SubmitReleaseView, UpdateWholesaleAndTradesView, CreateWholesalePriceView

urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('<int:pk>/submit/', SubmitReleaseView.as_view(), name='release_submit'),
    path('', AllReleaseView.as_view(), name='all_releases'),
    url("upcoming/", UpcomingReleasesView.as_view(), name="upcoming_releases"),
    path("recently-submitted/", RecentlySubmittedView.as_view(), name='recently_submitted'),
    path("my-releases/", MyReleasesView.as_view(), name='my_releases'),
    path('<int:pk>/wholesale_and_trades', UpdateWholesaleAndTradesView.as_view(), name='wholesale_and_trades_edit'),
    path('<int:pk>/release_wholesale_price', CreateWholesalePriceView.as_view(), name='release_wholesale_price_add')
]
