__author__ = 'tdgunes'

from django.conf.urls import patterns, url, include
from rest_framework import routers
from .viewsets import UserViewSet, PolicyViewSet, GlobalSettingsViewSet, BeaconViewSet
from .views import GetAllPolicies

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'policies', PolicyViewSet)
router.register(r'settings', GlobalSettingsViewSet)
router.register(r'beacons', BeaconViewSet)

from views import index_view

urlpatterns = patterns('',
    url(r'^api/policies/all$', GetAllPolicies.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^$', index_view, name="map")
)
