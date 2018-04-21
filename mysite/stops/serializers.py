from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Stop

import datetime

class StopsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    route = serializers.CharField(required=True, max_length=200)
    stops = serializers.ListField(child=serializers.CharField( max_length=200, allow_blank=True), max_length=20)

    def create(self, validated_data):
        return New.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.route = validated_data.get('route', instance.route)
        instance.stops = validated_data.get('stops', instance.stops)
        instance.save()
        return instance