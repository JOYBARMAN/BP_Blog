"""Serializer for Tag"""
from rest_framework import serializers

from tag.models import Tag


base_fields = [
    "id",
    "uid",
    "name",
    "description",
    "status",
]

base_read_only_fields = [
    "id",
    "uid",
]


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = base_fields
        read_only_fields = base_read_only_fields


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = base_fields + [
            "created_at",
            "updated_at",
        ]
        read_only_fields = base_read_only_fields + [
            "created_at",
            "updated_at",
        ]
