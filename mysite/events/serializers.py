from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import serializers
from .models import Event
from contextlib import contextmanager

import datetime

class EventsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=200)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    pub_date = serializers.DateTimeField(required=True)
    image_url = serializers.SerializerMethodField()

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def get_image_url(self, event):
        request = self.context.get('request')
        image_url = event.image.url
        return request.build_absolute_uri(image_url)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image_url =  validated_data.get('image_url', instance.image)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
