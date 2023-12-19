"""Serializers for user post """

from rest_framework import serializers

from post.models import Post, PostImages
from category.models import Category
from sub_category.models import SubCategory
from category.rest.serializers.category import SubCategorySerializer
from post_reaction.rest.serializers.post_reaction import UserSerializer

from ckeditor.fields import RichTextField


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "uid", "name"]


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ["id", "uid", "image"]


class PostImageAddSerializer(serializers.ModelSerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=None, allow_empty_file=False),
        write_only=True,
    )

    class Meta:
        model = PostImages
        fields = ["uploaded_images"]

    def create(self, validated_data):
        # Extract uploaded images data from validated_data
        uploaded_images = validated_data.pop("uploaded_images", [])

        # Ectract uid from context and get post
        uid = self.context.get("uid")
        post = Post.objects.get(uid=uid)

        # Create PostImages instance with post_instance and uploaded images
        post_images = [PostImages(post=post, image=image) for image in uploaded_images]

        # Bulk insert all related objects at once
        created_instances = PostImages.objects.bulk_create(post_images)

        # Serialize the created instances
        serializer = PostImagesSerializer(created_instances, many=True)
        serialized_data = serializer.data

        # Return the serialized data
        return serialized_data


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
    images = PostImagesSerializer(many=True)
    user = UserSerializer(read_only=True)

    class Meta(PostBaseSerializer.Meta):
        fields = PostBaseSerializer.Meta.fields + ["images"]
        read_only_fields = PostBaseSerializer.Meta.read_only_fields + []


class PostAddSerializer(PostBaseSerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=None, allow_empty_file=False),
        required=False,
        write_only=True,
    )

    class Meta(PostBaseSerializer.Meta):
        fields = PostBaseSerializer.Meta.fields + ["uploaded_images"]
        read_only_fields = PostBaseSerializer.Meta.read_only_fields + ["user"]

    def create(self, validated_data):
        # Extract category , sub-category and uploaded images data from validated_data
        categories_data = validated_data.pop("category", [])
        sub_categories_data = validated_data.pop("sub_category", [])
        uploaded_images = validated_data.pop("uploaded_images", [])

        # Create the Post instance with the authenticated user
        post_instance = Post.objects.create(
            user=self.context["request"].user, **validated_data
        )

        # Create PostImages instance with post_instance and uploaded images
        post_images = [
            PostImages(post=post_instance, image=image) for image in uploaded_images
        ]

        # Bulk insert all related objects at once
        PostImages.objects.bulk_create(post_images)

        # Set the categories and sub-categories for the created post_instance
        post_instance.category.set(categories_data)
        post_instance.sub_category.set(sub_categories_data)

        return post_instance


class PostDetailSerializer(PostBaseSerializer):
    category = CategorySerializer(many=True)
    sub_category = SubCategorySerializer(many=True)
    images = PostImagesSerializer(many=True)

    class Meta(PostBaseSerializer.Meta):
        fields = PostBaseSerializer.Meta.fields + [
            "images",
            "created_at",
            "updated_at",
        ]
        read_only_fields = PostBaseSerializer.Meta.read_only_fields + [
            "created_at",
            "updated_at",
        ]
