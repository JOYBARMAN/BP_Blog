"""Serializers for post reaction"""

from rest_framework import serializers


class PostReactionCountSerializer(serializers.Serializer):
    like = serializers.IntegerField(default=0)
    dislike = serializers.IntegerField(default=0)
    haha = serializers.IntegerField(default=0)
    sad = serializers.IntegerField(default=0)
    cute = serializers.IntegerField(default=0)
    love = serializers.IntegerField(default=0)
