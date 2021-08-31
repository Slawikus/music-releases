from django.db import models


class TradeItemManager(models.Manager):
    def tradelist_items_for_user(self, profile):
        return super().get_queryset().filter(wholesaleandtrades__available_for_trade=True). \
                                      filter(wholesaleandtrades__available_for_wholesale=True). \
                                      filter(is_submitted=True).filter(profile=profile)