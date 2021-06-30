from django.urls import path

from .views import SignUpView, EditProfileView, AddCurrencyView, DeleteCurrencyView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/edit/', EditProfileView.as_view(), name='profile_edit'),
    path('currencies/edit/', AddCurrencyView.as_view(), name='currencies_list'),
    path('currencies/edit/<int:pk>', DeleteCurrencyView.as_view(), name='currency_delete'),
]
