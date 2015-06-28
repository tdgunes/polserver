from django.shortcuts import render
import requests

from django.views.decorators.http import require_GET
from models import Policy, GlobalSettings
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Policy, Beacon
from .serializers import PolicySerializer
from rest_framework import status
import urlparse, json, arrow


class GetAllPolicies(APIView):
    """
    Returns all policies of this server and its supers
    """
    queryset = Policy.objects.all()
    permission_classes = [AllowAny]

    @staticmethod
    def set_up_policies(name, url, policies):
        return {"name":name, "url":url, "policies":policies}

    def get_beacon_if_available(self, request):
        beacon_uuid = request.data.get("uuid", None)
        beacon = None
        if beacon_uuid:
            try:
                beacon = Beacon.objects.get(uuid=beacon_uuid)
            except Beacon.DoesNotExist:
                print "[Warning] Beacon does not exist on database"
                pass
        else:
            print "[Warning] Beacon UUID was not availabe on the request"

        return beacon

    def get_server_configuration(self):
        server_name = GlobalSettings.objects.get_setting("name").value
        server_url = GlobalSettings.objects.get_setting("url").value
        return server_name, server_url

    def get_supers_policies(self):
        """
        if cache is expired:
            get policies from super and
            save it to global_settings as key=cache value=policies(json)
            return policies(json)
        else
            return GlobalSettings.objects.get_setting("cache")

        :return:
        """

        identifier = GlobalSettings.objects.get_setting("id").value
        last_updated = int(GlobalSettings.objects.get_setting("cache_last_updated").value)
        update_inteval = int(GlobalSettings.objects.get_setting("cache_update_interval").value)

        now = arrow.utcnow().timestamp
        if (now - last_updated) >= update_inteval: # cache is expired
            payload = json.dumps({"id":identifier})
            full_url = urlparse.urljoin(GlobalSettings.objects.get_setting("router").value, "/api/area/super")
            headers = {'Content-type': 'application/json'}
            try:
                r = requests.post(full_url, data=payload, headers=headers)
            except requests.ConnectionError:
                print "[Warning] Unable to access to router", full_url
                return []

            print "[Info] Cache is expired, fetched from super"
            super_area = r.json()
            super_area_url = super_area["url"]
            payload = "{}"
            super_area_policy_url = urlparse.urljoin(super_area_url, "/api/policies/all")
            try:
                r = requests.post(super_area_policy_url, data=payload, headers=headers)
            except requests.ConnectionError:
                print "[Warning] Unable to access to super area on", super_area_url

            super_policies = r.json()

            GlobalSettings.objects.set_setting("cache", json.dumps(super_policies))
            GlobalSettings.objects.set_setting("cache_last_updated", str(now))

            return super_policies

        return json.loads(GlobalSettings.objects.get("cache"))

    def post(self, request, format=None):
        server_name, server_url = self.get_server_configuration()
        beacon = self.get_beacon_if_available(request)

        policies = []

        if beacon:
            policy = self.set_up_policies(beacon.name, server_url+"#"+beacon.uuid, PolicySerializer(beacon.get_all_policies(), many=True).data)
            policies.insert(0, policy)

        super_policies = self.get_supers_policies()
        my_policies = Policy.objects.get_general_policies()
        print "[Info] My Policies:", my_policies
        serializer = PolicySerializer(my_policies, many=True)
        my_policies = self.set_up_policies(server_name, server_url, serializer.data)
        policies.insert(0, my_policies)

        for super_policy in super_policies:
            policies.insert(0, super_policy)

        return Response(policies, status=status.HTTP_200_OK)



@require_GET
def index_view(request):
    data = {"name": GlobalSettings.objects.get_setting("name"),
            "url": GlobalSettings.objects.get_setting("url"),
            "policies":Policy.objects.all(),
            }
    return render(request, 'index.html', data)
