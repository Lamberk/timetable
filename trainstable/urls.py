from django.conf.urls import url
from .views import search, station_detail, train_detail

urlpatterns = [
    url(r'^search/', search, name='search'),
    url(r'^station/(?P<station_id>[0-9]+)/$', station_detail, name='station_detail'),
    url(r'^train/(?P<train_id>[0-9]+)/$', train_detail, name='train_detail')
]