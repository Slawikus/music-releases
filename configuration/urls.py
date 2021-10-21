"""configuration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from core.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('labels/', include('labels.urls')),
    path('releases/', include('releases.urls')),
    path('band-submissions/', include('band_submissions.urls')),
    path('public_tradelist/', include('public_tradelist.urls')),
    path('trades/', include('trades.urls')),
    path('notifications/', include('notifications.urls')),
    path('messages/', include('postman.urls')),
    path('', dashboard, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.handle404'
handler403 = 'core.views.handle403'
handler500 = 'core.views.handle500'
