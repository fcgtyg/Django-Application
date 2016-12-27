from django.conf.urls import url

from .views import show_entries, get_entries

urlpatterns = [
    url(r'^$', show_entries),
    url(r'^(?P<entry_id>[0-9]+)', get_entry)
]
