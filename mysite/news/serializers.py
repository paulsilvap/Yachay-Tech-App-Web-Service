from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import serializers
from contextlib import contextmanager
from .models import New

import datetime


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=200)
    pub_date = serializers.DateTimeField(required=True)
    summary = serializers.CharField(required=True, max_length=300)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    image_url = serializers.SerializerMethodField()

    def create(self, validated_data):
        return New.objects.create(**validated_data)

    def get_image_url(self, new):
        request = self.context.get('request')
        image_url = new.image.url
        return request.build_absolute_uri(image_url)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image_url =  validated_data.get('image_url', instance.image)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
