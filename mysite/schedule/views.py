from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Schedule
from .serializers import ScheduleSerializer

# Create your views here.

@csrf_exempt
def schedule_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return JsonResponse(serializer.data, safe=False)