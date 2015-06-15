from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET
from models import Policy, GlobalSettings

@require_GET
def index_view(request):
    data = {"name": GlobalSettings.objects.get_setting("name"),
            "url": GlobalSettings.objects.get_setting("url"),
            "policies":Policy.objects.all(),
            }
    return render(request, 'index.html', data)
