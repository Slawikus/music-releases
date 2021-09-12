from django.urls import path

from . import views

urlpatterns = [
    path('signup/<str:public_id>/', views.SignUpView.as_view(), name='signup'),
    path('profile/edit/', views.EditProfileView.as_view(), name='profile_edit'),
    path('currencies/', views.ListProfileCurrencyView.as_view(), name='currencies_list'),
    path('currencies/new/', views.CreateProfileCurrencyView.as_view(), name='currency_create'),
    path('currencies/<int:pk>/delete/', views.DeleteProfileCurrencyView.as_view(), name='currency_delete'),
    path('labels/', views.ListLabelView.as_view(), name='labels_list'),
    path('labels/new/', views.CreateLabelView.as_view(), name='label_add'),
    path('labels/<int:pk>/edit/', views.UpdateLabelView.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', views.DeleteLabelView.as_view(), name='label_delete'),
    path('invitations/', views.ShowInvitationsView.as_view(), name='invitations'),
    path('submissions/', views.BandSubmissionsView.as_view(), name='submissions'),
    path('trade-requests/', views.TradeRequestListView.as_view(), name='trade_requests'),
    path('trade-details/<int:pk>/', views.TradeRequestDetailView.as_view(), name='trade_details'),
    path('notifications/', views.NotificationsListView.as_view(), name='notifications')
]
