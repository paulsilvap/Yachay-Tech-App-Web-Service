from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Event
from .serializers import EventsSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def events_list(request):
    
    if request.method == 'GET':
        event = Event.objects.all()
        serializer = EventsSerializer(event, many=True)
        return JsonResponse(serializer.data, safe=False)