""""Serializers for category"""

from rest_framework import serializers

from category.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id",
            "uid",
            "name",
            "description",
            "photo",
            "sub_categories",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "uid",
            "created_at",
            "updated_at",
        ]

    def get_sub_categories(self, obj):
        return obj.sub_categories

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
