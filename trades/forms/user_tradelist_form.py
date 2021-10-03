from public_tradelist.forms import BaseTradeListForm
from trades.models import UserTradeRequest


class UserTradeListForm(BaseTradeListForm):
    class Meta:
        model = UserTradeRequest
        exclude = ['name', 'profile', 'from_profile']
