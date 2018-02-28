from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Schedule

import datetime

class ScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=200)
    subject = serializers.CharField(required=True, max_length=200)
    time = serializers.CharField(required=True, max_length=200)
    day = serializers.CharField(required=True, max_length=200)

    def create(self, validated_data):
        return Shedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.time = validated_data.get('time', instance.time)
        instance.day = validated_data.get('day', instance.day)
        instance.save()
        return instance
