from re import S
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from .models import Dares, Dollars

class DollarsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField()
    anonymous = serializers.BooleanField()
    dares_id = serializers.IntegerField()
    supporter = serializers.ReadOnlyField(source='supporter.id')

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
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Dares.objects.create(**validated_data)

class DaresDetailSerializer(DaresSerializer):
    dollars = DollarsSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.dare_description = validated_data.get('dare_description',instance.dare_description)
        instance.rules = validated_data.get('rules',instance.rules)
        instance.goal = validated_data.get('goal',instance.goal)
        instance.image = validated_data.get('image',instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.created_at = validated_data.get('created_at',instance.created_at)
        instance.updated_at = validated_data.get('updated_at',instance.updated_at)
        instance.date_for_dare = validated_data.get('date_for_dare', instance.date_for_dare)
        instance.for_charity = validated_data.get('for_charity', instance.for_charity)
        instance.charity_url = validated_data.get('charity_url', instance.charity_url)
        instance.owner = validated_data.get('owner',instance.owner)
        instance.save()
        return instance

class DollarsDetailSerializer(DollarsSerializer):
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount',instance.amount)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.anonymous = validated_data.get('anonymous',instance.anonymous)
        instance.supporter = validated_data.get('supporter',instance.supporter)
        instance.dares_id = validated_data.get('dares_id',instance.dares_id)
        return instance