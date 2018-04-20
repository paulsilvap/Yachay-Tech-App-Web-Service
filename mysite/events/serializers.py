from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Event


import datetime

class EventsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=200)
    image = serializers.FileField(required='127.0.0.1:8000')
    pub_date = serializers.DateTimeField(required=True)
    description = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image =  validated_data.get('image', instance.image)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
