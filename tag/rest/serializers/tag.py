"""Serializer for Tag"""
from rest_framework import serializers

from tag.models import Tag


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "uid",
            "name",
            "description",
            "status"
        ]
        read_only_fields = [
            "id",
            "uid",
        ]


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "uid",
            "name",
            "description",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "uid",
            "created_at",
            "updated_at"
        ]
