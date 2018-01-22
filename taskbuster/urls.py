# -*- coding: utf-8 -*-
"""taskbuster URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import logout
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files

urlpatterns = [
    re_path(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files'),
    # re_path(r'^accounts/logout/$', logout, {'next_page': '/'}),
    re_path(r'^accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    re_path(r'^$', home, name='home'),
    path('admin/', admin.site.urls),
)
