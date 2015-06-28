__author__ = 'tdgunes'

from .serializers import PolicySerializer, GlobalSettingsSerializer, UserSerializer, BeaconSerializer
from rest_framework import viewsets
from .models import User, Policy, GlobalSettings, Beacon
from rest_framework.permissions import AllowAny

class BeaconViewSet(viewsets.ModelViewSet):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer
    permission_classes = [AllowAny]

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [AllowAny]

class GlobalSettingsViewSet(viewsets.ModelViewSet):
    queryset = GlobalSettings.objects.all()
    serializer_class = GlobalSettingsSerializer
    permission_classes = [AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

