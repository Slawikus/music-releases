from django.urls import path

from .views import SignUpView, EditProfileView, CreateCurrencyView, DeleteCurrencyView, ListCurrenciesView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/edit/', EditProfileView.as_view(), name='profile_edit'),
    path('currencies/', ListCurrenciesView.as_view(), name='currencies_list'),
    path('currencies/new/', CreateCurrencyView.as_view(), name='currency_create'),
    path('currencies/<int:pk>/delete/', DeleteCurrencyView.as_view(), name='currency_delete'),
]
