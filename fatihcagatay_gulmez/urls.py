"""fatihcagatay_gulmez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseRedirect
from todo.views import *
from users.views import *
from blog.views import *
from tags.views import *

urlpatterns = [url(r'^admin/', admin.site.urls),
               url(r'^todos/', show_todo),
               url(r'^todos/(?P<todo_id>[0-9]+)', get_todo),
               url(r'^users/register/$', signup),
               url(r'^users/', include("django.contrib.auth.urls")),
               url(r'^tags/$', show_tag),
               url(r'^accounts/profile', redirect),
               url(r'^blog/entries/$', show_entries),
               url(r'^blog/entries/(?P<entry_id>[0-9]+)', get_entry),
               url(r'^todos/all/$', show_all_todo),
               url(r'^todos/all/user/(?P<userId>[0-9]+)$', show_all_todo_from_user),
               url(r'^blog/entries/all/$', show_all_entries),
               url(r'^blog/entries/all/user/(?P<userId>[0-9]+)$', show_all_entries_from_user),
               ]

