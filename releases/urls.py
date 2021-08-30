from django.urls import path
from django.conf.urls import url

from .views import (CreateReleaseView,
                    AllReleaseView,
                    MyReleasesView,
                    UpcomingReleasesView,
                    RecentlySubmittedView,
                    EditReleaseView,
                    UpdateWholesaleAndTradesView,
                    CreateWholesalePriceView,
                    SubmitReleaseView,
                    ImportReleasesView,
                    RequestPublicTradeListView
                    )


urlpatterns = [
    path('new/', CreateReleaseView.as_view(), name='release_add'),
    path('<int:pk>/submit/', SubmitReleaseView.as_view(), name='release_submit'),
    path('', AllReleaseView.as_view(), name='all_releases'),
    url("upcoming/", UpcomingReleasesView.as_view(), name="upcoming_releases"),
    path("recently-submitted/", RecentlySubmittedView.as_view(), name='recently_submitted'),
    path("my-releases/", MyReleasesView.as_view(), name='my_releases'),
    path("<int:pk>/edit/", EditReleaseView.as_view(), name='edit_release'),
    path('<int:pk>/wholesale_and_trades', UpdateWholesaleAndTradesView.as_view(), name='wholesale_and_trades_edit'),
    path('<int:pk>/release_wholesale_price', CreateWholesalePriceView.as_view(), name='release_wholesale_price_add'),
    path("import-releases/", ImportReleasesView.as_view(), name="import_releases"),
    path("tradelist/<str:trade_id>", RequestPublicTradeListView.as_view(), name='public_tradelist'),
]
