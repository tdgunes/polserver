from django.shortcuts import render
import requests

from django.views.decorators.http import require_GET
from models import Policy, GlobalSettings
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Policy
from .serializers import PolicySerializer
from rest_framework import status
import urlparse, json

class GetAllPolicies(APIView):
    """
    Returns all policies of this server and its supers
    """
    queryset = Policy.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        identifier = GlobalSettings.objects.get_setting("id").value
        payload = json.dumps({"id":identifier})
        full_url = urlparse.urljoin(GlobalSettings.objects.get_setting("router").value, "/api/area/super")
        headers = {'Content-type': 'application/json'}
        r = requests.post(full_url, data=payload, headers=headers)
        print r.text
        super_areas = r.json()

        server_name = GlobalSettings.objects.get_setting("name").value
        server_url = GlobalSettings.objects.get_setting("url").value
        if len(super_areas)>0:
            policies = []
            for area in super_areas:
                full_url = urlparse.urljoin(area["url"], "/api/policies/")
                request = requests.get(full_url)
                policy_obj = {"name": server_name,
                "url": server_url,
                "policies": request.json()}
                policies.append(policy_obj)
            serializer = PolicySerializer(self.queryset, many=True)
            response = {"name": server_name,
                        "url": server_url,
                        "policies": serializer.data}
            policies.append(response)
            return Response(policies, status=status.HTTP_200_OK)
        else:
            serializer = PolicySerializer(self.queryset, many=True)
            response = {"name": server_name,
                        "url": server_url,
                        "policies": serializer.data}
            return Response(response, status=status.HTTP_200_OK)


@require_GET
def index_view(request):
    data = {"name": GlobalSettings.objects.get_setting("name"),
            "url": GlobalSettings.objects.get_setting("url"),
            "policies":Policy.objects.all(),
            }
    return render(request, 'index.html', data)
