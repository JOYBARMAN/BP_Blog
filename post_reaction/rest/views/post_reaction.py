""""Views for post reaction"""

from django.db.models import Count

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from post_reaction.models import PostReaction
from post_reaction.choices import ReactionChoices
from post_reaction.rest.serializers.post_reaction import PostReactionCountSerializer
from core.permissions import (
    IsAuthenticated,
    IsAdminUser,
    SAFE_METHODS,
)


class PostReactionCount(RetrieveAPIView):
    serializer_class = PostReactionCountSerializer

    def get_queryset(self):
        return PostReaction.objects.filter(post__uid=self.kwargs["uid"])

    def get_object(self):
        reactions_count = (
            self.get_queryset().values("reaction_type").annotate(count=Count("id"))
        )
        return {
            item["reaction_type"].lower(): item["count"] for item in reactions_count
        }

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)
