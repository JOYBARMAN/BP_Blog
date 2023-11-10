""""Serializers for subcategory"""

from rest_framework import serializers

from sub_category.models import SubCategory
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "uid", "name"]


class SubCategoryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            "id",
            "uid",
            "name",
            "description",
            "photo",
            "status",
        ]
        read_only_fields = [
            "id",
            "uid",
        ]


class SubCategoryListSerializer(SubCategoryBaseSerializer):
    category = CategorySerializer(read_only=True)

    class Meta(SubCategoryBaseSerializer.Meta):
        fields = SubCategoryBaseSerializer.Meta.fields + [
            "category",
            "created_at",
            "updated_at",
        ]
        read_only_fields = SubCategoryBaseSerializer.Meta.read_only_fields + []


class SubCategoryPostSerializer(SubCategoryBaseSerializer):
    class Meta(SubCategoryBaseSerializer.Meta):
        fields = SubCategoryBaseSerializer.Meta.fields + ["category"]
        read_only_fields = SubCategoryBaseSerializer.Meta.read_only_fields + []

    def create(self, validated_data):
        return SubCategory.objects.create(**validated_data)
