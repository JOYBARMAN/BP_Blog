""""Serializers for category"""

from rest_framework import serializers

from category.models import Category
from sub_category.models import SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "uid", "name"]


class CategoryListSerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)

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

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
