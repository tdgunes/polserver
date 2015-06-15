__author__ = 'tdgunes'

from django.conf.urls import patterns, url

from views import index_view

urlpatterns = patterns('',
    url(r'^$', index_view, name="map")
)
