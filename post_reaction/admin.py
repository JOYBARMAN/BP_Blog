from django.contrib import admin

from .models import PostReaction


@admin.register(PostReaction)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user_name", "title", "reaction_type")
    search_fields = ("reaction_type",)

    def user_name(self, obj):
        return obj.user.username

    def title(self, obj):
        return obj.post.title

    # user_name.short_description = "User"
