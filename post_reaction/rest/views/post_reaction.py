""""Views for post reaction"""

from django.db.models import Count, F

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
from post_reaction.rest.serializers.post_reaction import (
    PostReactionCountSerializer,
    PostReactionSerializer,
)
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

        # Use annotate to get the user list and count in a single query
        reactions_data = queryset.values("reaction_type").annotate(
            count=Count("id"),
            user_list=F("user__username"),
        )

        result = {}

        for item in reactions_data:
            reaction_type = item["reaction_type"].lower()
            user_list = [item["user_list"]] if item["user_list"] else []

            result[reaction_type] = {"count": item["count"], "user": user_list}

        # Ensure that each reaction type has a dictionary, even if it's empty
        for reaction_type in ReactionChoices.values:
            if reaction_type.lower() not in result:
                result[reaction_type.lower()] = {"count": 0, "user": []}

        return result

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostReactionCreate(CreateAPIView):
    serializer_class = PostReactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={"uid": kwargs.get("uid"), "user": self.request.user},
        )
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()
        return Response(response_data, status=status.HTTP_200_OK)
