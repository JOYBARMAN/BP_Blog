"""Serializers for post reaction"""

from rest_framework import serializers

from post_reaction.models import PostReaction


class PostReactionCountSerializer(serializers.Serializer):
    like = serializers.DictField(required=False)
    dislike = serializers.DictField(required=False)
    haha = serializers.DictField(required=False)
    sad = serializers.DictField(required=False)
    cute = serializers.DictField(required=False)
    love = serializers.DictField(required=False)


class PostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = ["user", "post", "reaction_type"]

    def create(self, validated_data):
        user = validated_data["user"]
        post = validated_data["post"]
        reaction_type = validated_data["reaction_type"]

        # Check if a reaction exists with the same user, post, and reaction_type
        existing_reaction = PostReaction.objects.filter(
            user=user, post=post, reaction_type=reaction_type
        ).first()

        if existing_reaction:
            # If exists, delete the existing reaction
            existing_reaction.delete()
            return {"msg": "Reaction Removed Successfully"}
        else:
            # Check if a reaction exists with the same user and post but a different reaction_type
            existing_reaction_user_post = (
                PostReaction.objects.filter(user=user, post=post)
                .exclude(reaction_type=reaction_type)
                .first()
            )

            if existing_reaction_user_post:
                # User and post already exist, update the reaction_type
                existing_reaction_user_post.reaction_type = reaction_type
                existing_reaction_user_post.save()
                return {"msg": "Reaction Updated Successfully", "data": self.data}
            else:
                # Create a new PostReaction
                super().create(validated_data)
                return {"msg": "Reaction Created Successfully", "data": self.data}
