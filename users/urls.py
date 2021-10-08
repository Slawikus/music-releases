from django.urls import path

from users import views

urlpatterns = [
    path('signup/<str:public_id>/', views.SignUpView.as_view(), name='signup'),
    path('profile/edit/', views.EditProfileView.as_view(), name='profile_edit'),
    path('currencies/', views.ListProfileCurrencyView.as_view(), name='currencies_list'),
    path('currencies/new/', views.CreateProfileCurrencyView.as_view(), name='currency_create'),
    path('currencies/<int:pk>/delete/', views.DeleteProfileCurrencyView.as_view(), name='currency_delete'),
    path('invitations/', views.ShowInvitationsView.as_view(), name='invitations'),
    path('submissions/', views.BandSubmissionsView.as_view(), name='submissions'),
    path('submission-details/<int:pk>', views.BandSubmissionDetailView.as_view(), name='submission_details'),
    path('trade-requests/', views.TradeRequestListView.as_view(), name='trade_requests'),
    path('trade-details/<int:pk>/', views.TradeRequestDetailView.as_view(), name='trade_details'),
    path('user-trade-details/<int:pk>/', views.UsersTradeRequestDetailView.as_view(), name='user_trade_details'),
]
