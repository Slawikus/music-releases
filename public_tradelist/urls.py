from django.urls import path
from .views import PublicTradeListView

urlpatterns = [
    path('<str:trade_id>', PublicTradeListView.as_view(), name='public_tradelist'),
    # path('<int:pk>/create_request/', CreateTradeRequestView.as_view(), name='create_trade_request')
]
