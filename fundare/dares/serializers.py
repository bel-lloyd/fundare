from rest_framework import serializers
from .models import Dares

class DaresSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    dare_description = serializers.CharField(max_length=None)
    rules = serializers.CharField()
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    date_for_dare = serializers.DateTimeField()
    for_charity = serializers.CharField()
    charity_url = serializers.URLField()
    owner = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Dares.objects.create(**validated_data)