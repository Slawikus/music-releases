from django.urls import path

from trades.views import CreateTradeRequestView

urlpatterns = [
    path('<int:pk>/create_request/', CreateTradeRequestView.as_view(), name='create_trade_request')
]
