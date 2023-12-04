"""Serializers for post reaction"""

from rest_framework import serializers


class PostReactionCountSerializer(serializers.Serializer):
    like = serializers.DictField(required=False)
    dislike = serializers.DictField(required=False)
    haha = serializers.DictField(required=False)
    sad = serializers.DictField(required=False)
    cute = serializers.DictField(required=False)
    love = serializers.DictField(required=False)
