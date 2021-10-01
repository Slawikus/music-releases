from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('new/', views.CreateReleaseView.as_view(), name='release_add'),
    path('<int:pk>/submit/', views.SubmitReleaseView.as_view(), name='release_submit'),
    path('<int:pk>/add-to-wishlist', views.AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('', views.AllReleaseView.as_view(), name='all_releases'),
    url("upcoming/", views.UpcomingReleasesView.as_view(), name="upcoming_releases"),
    path("recently-submitted/", views.RecentlySubmittedView.as_view(), name='recently_submitted'),
    path("my-releases/", views.MyReleasesView.as_view(), name='my_releases'),
    path("favourite-releases/", views.WishlistView.as_view(), name='favourite-releases'),
    path("<int:pk>/edit/", views.EditReleaseView.as_view(), name='edit_release'),
    path('<int:pk>/trades_info', views.UpdateReleaseTradesInfoView.as_view(), name='release_trades_info_edit'),
    path('<int:pk>/wholesale_info', views.UpdateReleaseWholesaleInfoView.as_view(), name='release_wholesale_info_edit'),
    path('<int:pk>/release_wholesale_price', views.CreateWholesalePriceView.as_view(), name='release_wholesale_price_add'),
    path("import-releases/", views.ImportReleasesView.as_view(), name="import_releases"),
    path('<int:pk>/wholesale_price_delete', views.DeleteWholesalePriceView.as_view(), name='wholesale_price_delete'),
    path('<int:pk>/marketing_infos', views.UpdateMarketingInfosView.as_view(), name='marketing_infos_edit'),
]
