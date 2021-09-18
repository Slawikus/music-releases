from django.urls import path
from .views import NotificationRedirectView, NotificationListView

urlpatterns = [
	path('<int:pk>/redirect-to-target', NotificationRedirectView.as_view(), name='notif_redirect'),
	path('', NotificationListView.as_view(), name='notifications')
]