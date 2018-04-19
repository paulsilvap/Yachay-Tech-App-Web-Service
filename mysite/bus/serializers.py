from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Schedule, Stop, Time

import datetime

class ScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    day = serializers.CharField(required=True, max_length=200)
    location = serializers.CharField(required=True, max_length=200)
    time = serializers.CharField(required=True, max_length=200)
    # TimeField(required=True)

    def create(self, validated_data):
        return Shedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.day = validated_data.get('day', instance.day)
        instance.location = validated_data.get('stop', instance.location)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance
