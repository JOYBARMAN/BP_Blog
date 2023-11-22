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
        read_only_fields = PostBaseSerializer.Meta.read_only_fields + ["user"]

    def create(self, validated_data):
        # Extract category and sub-category data from validated_data
        categories_data = validated_data.pop("category", [])
        sub_categories_data = validated_data.pop("sub_category", [])

        # Create the Post instance with the authenticated user
        post_instance = Post.objects.create(
            user=self.context["request"].user, **validated_data
        )

        # Set the categories and sub-categories for the created post_instance
        post_instance.category.set(categories_data)
        post_instance.sub_category.set(sub_categories_data)

        return post_instance


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
