from django.urls import path
from django.conf.urls import url

from .views import (CreateReleaseView, AllReleaseView, MyReleasesView,
                    UpcomingReleasesView, RecentlySubmittedView, EditReleaseView,
                    DeleteWholesalePriceView, CreateWholesalePriceView,
                    SubmitReleaseView, ImportReleasesView, UpdateMarketingInfosView,
                    UpdateReleaseTradesInformationView, UpdateReleaseWholesaleInformationView)


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('<int:pk>/submit/', SubmitReleaseView.as_view(), name='release_submit'),
    path('', AllReleaseView.as_view(), name='all_releases'),
    url("upcoming/", UpcomingReleasesView.as_view(), name="upcoming_releases"),
    path("recently-submitted/", RecentlySubmittedView.as_view(), name='recently_submitted'),
    path("my-releases/", MyReleasesView.as_view(), name='my_releases'),
    path("<int:pk>/edit/", EditReleaseView.as_view(), name='edit_release'),
    path('<int:pk>/release_trades_info', UpdateReleaseTradesInformationView.as_view(), name='release_trades_info_edit'),
    path('<int:pk>/release_wholesale_info', UpdateReleaseWholesaleInformationView.as_view(), name='release_wholesale_info_edit'),
    path('<int:pk>/release_wholesale_price', CreateWholesalePriceView.as_view(), name='release_wholesale_price_add'),
    path("import-releases/", ImportReleasesView.as_view(), name="import_releases"),
    path('<int:pk>/wholesale_price_delete', DeleteWholesalePriceView.as_view(), name='wholesale_price_delete'),
    path('<int:pk>/marketing_infos', UpdateMarketingInfosView.as_view(), name='marketing_infos_edit'),
]
