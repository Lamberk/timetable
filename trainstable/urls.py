from django.conf.urls import url
from .views import table, generator, finder

urlpatterns = [
    url(r'^index/', table, name='table'),
    url(r'^generator/', generator, name='generator'),
    url(r'^finder/', finder, name='finder')
]