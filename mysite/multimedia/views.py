from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Multimedia
from .serializer import MultiSerializer

# Create your views here.

@csrf_exempt
def multimedia_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        multi = Multimedia.objects.all()
        serializer = MultiSerializer(multi, many=True)
        return JsonResponse(serializer.data, safe=False)