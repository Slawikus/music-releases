from django.urls import path
from . import views

urlpatterns = [
    path('', views.LabelListView.as_view(), name='label_list'),
    path('users-labels/', views.UsersLabelListView.as_view(), name='users_label_list'),
    path('new/', views.CreateLabelView.as_view(), name='label_add'),
    path('<int:pk>/edit/', views.UpdateLabelView.as_view(), name='label_update'),
    path('<int:pk>/delete/', views.DeleteLabelView.as_view(), name='label_delete'),
    path('<int:pk>/detail/', views.LabelDetailView.as_view(), name='label_detail'),
    path('<int:pk>/set-as-main/', views.SetAsMainLabelView.as_view(), name='label_set_as_main')
]
