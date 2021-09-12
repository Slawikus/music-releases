from django.urls import path
from .views import NotificationRedirectView

urlpatterns = [
	path('redirect?notification=<int:id>/', NotificationRedirectView.as_view(), name='notif_redirect')
]