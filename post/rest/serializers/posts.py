"""Serializers for user post """

from rest_framework import serializers

from post.models import Post
from category.models import Category
from sub_category.models import SubCategory
from category.rest.serializers.category import SubCategorySerializer

from ckeditor.fields import RichTextField


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "uid", "name"]


class PostBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "uid",
            "user",
            "title",
            "category",
            "sub_category",
            "content",
            "is_published",
            "status",
        ]
        read_only_fields = [
            "id",
            "uid",
        ]


class PostListSerializer(PostBaseSerializer):
    category = CategorySerializer(many=True)
    sub_category = SubCategorySerializer(many=True)

    class Meta(PostBaseSerializer.Meta):
        fields = PostBaseSerializer.Meta.fields + []
        read_only_fields = PostBaseSerializer.Meta.read_only_fields + []


class PostAddSerializer(PostBaseSerializer):
    class Meta(PostBaseSerializer.Meta):
        fields = PostBaseSerializer.Meta.fields + []
        read_only_fields = PostBaseSerializer.Meta.read_only_fields + []


class PostDetailSerializer(PostBaseSerializer):
    class Meta(PostBaseSerializer.Meta):
        fields = PostBaseSerializer.Meta.fields + [
            "created_at",
            "updated_at",
        ]
        read_only_fields = PostBaseSerializer.Meta.read_only_fields + [
            "created_at",
            "updated_at",
        ]
