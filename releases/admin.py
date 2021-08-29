from django.contrib import admin
from .models import Release, TradeRequest

# Register your models here.
admin.site.register(Release)
admin.site.register(TradeRequest)