from django.contrib import admin

from .models import Post, PostImages


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user_name", "title", "is_published")
    search_fields = ("title",)

    def user_name(self, obj):
        return obj.user.username

    user_name.short_description = "Username"  # Set a custom column header


@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "image",
    )
    search_fields = ("post__title",)

    def post(self, obj):
        return obj.post.title

    post.short_description = "Post Title"
