__author__ = 'tdgunes'

from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Policy, User, GlobalSettings, Beacon

class BeaconSerializer(ModelSerializer):
    class Meta:
        model = Beacon

class GlobalSettingsSerializer(ModelSerializer):
    class Meta:
        model = GlobalSettings

class PolicySerializer(ModelSerializer):
    class Meta:
        fields = ('text', 'color', 'author')
        model = Policy

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'is_staff')