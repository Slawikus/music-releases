from django.urls import path

from .views import SignUpView, EditProfileView, AddCurrenciesView, DeleteCurrenciesView, AddLabelView, ListLabelsView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('currencies/edit/', AddCurrenciesView.as_view(), name='edit_currencies'),
    path('currencies/edit/<int:pk>', DeleteCurrenciesView.as_view(), name='delete_currencies'),
    path('labels/', ListLabelsView.as_view(), name='labels_list'),
    path('labels/add/', AddLabelView.as_view(), name='label_add'),
]
