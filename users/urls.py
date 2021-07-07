from django.urls import path

from .views import SignUpView, EditProfileView, CreateProfileCurrencyView, DeleteProfileCurrencyView, ListProfileCurrencyView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/edit/', EditProfileView.as_view(), name='profile_edit'),
    path('currencies/', ListProfileCurrencyView.as_view(), name='currencies_list'),
    path('currencies/new/', CreateProfileCurrencyView.as_view(), name='currency_create'),
    path('currencies/<int:pk>/delete/', DeleteProfileCurrencyView.as_view(), name='currency_delete'),
]
