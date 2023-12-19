from django.contrib import admin

from .models import PostReaction, Comment


@admin.register(PostReaction)
class PostReactionAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post_title", "reaction_type")
    search_fields = ("reaction_type",)

    def user_name(self, obj):
        return obj.user.username

    def post_title(self, obj):
        return obj.post.title


@admin.register(Comment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post_title", "comment")
    search_fields = ("reaction_type",)
    list_filter = ("post__title",)

    def user_name(self, obj):
        return obj.user.username

    def post_title(self, obj):
        return obj.post.title
