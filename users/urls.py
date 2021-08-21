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
    SubmissionLinkView,
    BandSubmissionListView,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/edit/', EditProfileView.as_view(), name='profile_edit'),
    path('currencies/', ListProfileCurrencyView.as_view(), name='currencies_list'),
    path('currencies/new/', CreateProfileCurrencyView.as_view(), name='currency_create'),
    path('currencies/<int:pk>/delete/', DeleteProfileCurrencyView.as_view(), name='currency_delete'),
    path('labels/', ListLabelView.as_view(), name='labels_list'),
    path('labels/new/', CreateLabelView.as_view(), name='label_add'),
    path('labels/<int:pk>/edit/', UpdateLabelView.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', DeleteLabelView.as_view(), name='label_delete'),
    path('submission-links/', SubmissionLinkView.as_view(), name='submission_links'),
    path('submissions/', BandSubmissionListView.as_view(), name='submissions')
]
