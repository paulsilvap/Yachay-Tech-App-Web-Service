from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import New
from .serializers import NewsSerializer

# Create your views here.

@csrf_exempt
def news_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        news = New.objects.all()
        serializer = NewsSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False)