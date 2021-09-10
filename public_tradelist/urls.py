from django.urls import path
from .views import PublicTradeListView


urlpatterns = [
	path('<str:trade_id>', PublicTradeListView.as_view(), name='public_tradelist')
]