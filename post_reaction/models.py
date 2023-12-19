"""Models for user post reaction and comment"""

from django.db import models

from common.models import BaseModelWithUID
from core.models import User
from post.models import Post
from post_reaction.choices import ReactionChoices


class PostReaction(BaseModelWithUID):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reactions"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_reactions"
    )
    reaction_type = models.CharField(
        max_length=20,
        choices=ReactionChoices.choices,
        default=ReactionChoices.UNDEFINED,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"], name="unique_user_post_reaction"
            )
        ]

    def __str__(self):
        return f"post--{self.post.title} user--{self.user.username} reaction--{self.reaction_type}"


class Comment(BaseModelWithUID):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment", db_index=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_comment_user", db_index=True
    )
    comment = models.TextField()

    def __str__(self):
        return f"post---{self.post.title} user---{self.user.username} comment{self.comment}"
