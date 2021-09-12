from django.urls import path
from .views import NotificationRedirectView, NotificationListView

urlpatterns = [
	path('redirect?notification=<int:id>/', NotificationRedirectView.as_view(), name='notif_redirect'),
	path('', NotificationListView.as_view(), name='notifications')
]