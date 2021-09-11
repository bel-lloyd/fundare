from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from .models import Dares
from .models import Dollars

class DollarsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField()
    anonymous = serializers.BooleanField()
    dare = serializers.IntegerField()
    supporter = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Dollars.objects.create(**validated_data)

class DaresSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    dare_description = serializers.CharField()
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
    dollars = DollarsSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Dares.objects.create(**validated_data)

class DaresDetailSerializer(DaresSerializer):
    dollars = DollarsSerializer(many=True, read_only=True)