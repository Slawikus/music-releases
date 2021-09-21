from django.urls import path

from .views import (
    SignUpView,
    EditProfileView,
    CreateProfileCurrencyView,
    DeleteProfileCurrencyView,
    ListProfileCurrencyView,
    CreateLabelView,
    ListLabelView,
    UpdateLabelView,
    DeleteLabelView,
    LabelDetailView,
    BandSubmissionsView,
    ShowInvitationsView,
    TradeRequestDetailView,
    TradeRequestListView
)

urlpatterns = [
    path('signup/<str:public_id>/', SignUpView.as_view(), name='signup'),
    path('profile/edit/', EditProfileView.as_view(), name='profile_edit'),
    path('currencies/', ListProfileCurrencyView.as_view(), name='currencies_list'),
    path('currencies/new/', CreateProfileCurrencyView.as_view(), name='currency_create'),
    path('currencies/<int:pk>/delete/', DeleteProfileCurrencyView.as_view(), name='currency_delete'),
    path('labels/', ListLabelView.as_view(), name='labels_list'),
    path('labels/new/', CreateLabelView.as_view(), name='label_add'),
    path('labels/<int:pk>/edit/', UpdateLabelView.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', DeleteLabelView.as_view(), name='label_delete'),
    path('labels/<int:pk>/detail/', LabelDetailView.as_view(), name='label_detail'),
    path('invitations/', ShowInvitationsView.as_view(), name='invitations'),
    path('submissions/', BandSubmissionsView.as_view(), name='submissions'),
    path('trade-requests/', TradeRequestListView.as_view(), name='trade_requests'),
    path('trade-details/<int:pk>/', TradeRequestDetailView.as_view(), name='trade_details')
]
