"""Weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('Weather/', include('Weather.urls'))
"""
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from apps.weather.views import weather
import Weather.views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', weather, name='main'),
    path(r'accounts/', include('allauth.urls')),
    path(r'accounts/', include('myauth.urls')),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'media/favicon.ico')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path(r'weather/', weather, name='weather'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,) + static(settings.STATIC_URL,
                                                                            document_root=settings.STATIC_ROOT)

handler404 = Weather.views.page_not_found
handler500 = Weather.views.page_error
