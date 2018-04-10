from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import New

import datetime

class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=200)
    image = serilizers.ImageField(required=True)
    pub_date = serializers.DateTimeField(required=True)
    description = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return New.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('news_title', instance.title)
        instance.image = validated_data.get('news_image', instance.image)
        instance.pub_date = validated_data.get('news_pub_date', instance.pub_date)
        instance.description = validated_data.get('news_description', instance.description)
        instance.save()
        return instance
