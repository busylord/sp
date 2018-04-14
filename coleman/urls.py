"""coleman URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from coleman.core import views as core_views
from django.urls import path
from django.conf import settings
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    path(r'', core_views.welcome, name='welcome'),
    path(r'^about/$', core_views.about, name='about'),
    #url(r'^$', lambda r: HttpResponseRedirect('admin/')),   # Remove this redirect if you add custom views
    path('dashboard/', admin.site.urls),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'})
]

admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_TITLE
admin.site.index_title = settings.INDEX_TITLE