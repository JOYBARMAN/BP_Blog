""""Serializers for subcategory"""

from rest_framework import serializers

from sub_category.models import SubCategory


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
    category = serializers.CharField(source="category.name")

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
