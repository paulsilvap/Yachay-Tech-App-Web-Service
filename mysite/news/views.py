from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.postgres.search import (
#     SearchQuery, SearchRank, SearchVector
# )
#from django.views.generic import ListView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import New
from .serializers import NewsSerializer
from rest_framework import viewsets
#from django.db import models

# Create your views here.

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewsSerializer

#class NewSearchListView(models.Manager):
    """
    Display a News List page filtered by the search query.
    """
    #model = New
    #paginate_by = 10

#    def search(self, text):
#        query = SearchQuery(text, config='english')
#        title_vector = SearchVector('title', weight='A')
#        description_vector = SearchVector('description', weight='B')
#        vectors = (title_vector + description_vector)
#        search_rank = SearchRank(vectors, query)
#        return self.get_queryset().annotate(
#            search=vectors
#        ).filter(
#            search=query
#        ).annotate(
#            rank=search_rank
#        ).order_by('-rank')
        