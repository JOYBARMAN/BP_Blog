"""Models for post content"""

from django.db import models

from common.models import BaseModelWithUID
from core.models import User
from category.models import Category
from sub_category.models import SubCategory
from tag.models import Tag
from .utils import custom_upload_to

from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField


class Post(BaseModelWithUID):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_user", db_index=True
    )
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(
        Category, related_name="post_category", blank=True, db_index=True
    )
    sub_category = models.ManyToManyField(
        SubCategory, related_name="post_subcategory", blank=True
    )
    content = RichTextField()
    tag = models.ManyToManyField(
        Tag, related_name="post_tag", blank=True
    )
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "User Post"
        verbose_name_plural = "User posts"

    def __str__(self):
        return f"{self.user.username} post {self.title}"


class PostImages(BaseModelWithUID):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = VersatileImageField(
        "image_post",
        upload_to="images/post/",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Post Image"
        verbose_name_plural = "Post Images"

    def __str__(self):
        return f"{self.post.title}"
