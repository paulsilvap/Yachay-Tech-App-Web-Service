from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import serializers
from contextlib import contextmanager
from .models import Multimedia

import datetime

class MultiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=200)
    pub_date = serializers.DateTimeField(required=True)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    file_url= serializers.SerializerMethodField()
    
    def create(self, validated_data):
        return Multimedia.objects.create(**validated_data)

    def get_file_url(self, multi):
        request = self.context.get('request')
        file_url = multi.archivo.url
        return request.build_absolute_uri(file_url)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.description = validated_data.get('description', instance.description)
        instance.file_url = validated_data.get('file_url', instance.archivo)
        instance.save()
        return instance
