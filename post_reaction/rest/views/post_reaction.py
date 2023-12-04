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
        queryset = self.get_queryset()
        reactions_count = queryset.values("reaction_type").annotate(count=Count("id"))
        result = {}

        for item in reactions_count:
            reaction_type = item["reaction_type"].lower()
            user_list = queryset.filter(
                reaction_type=item["reaction_type"]
            ).values_list("user__username", flat=True)

            result[reaction_type] = {"count": item["count"], "user": list(user_list)}

        # Ensure that each reaction type has a dictionary, even if it's empty
        for reaction_type in ReactionChoices.values:
            if reaction_type.lower() not in result:
                result[reaction_type.lower()] = {"count": 0, "user": []}

        return result

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)
