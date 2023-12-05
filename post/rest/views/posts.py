"""Views for post"""

from django.db.models import Prefetch

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from post.models import Post, PostImages
from category.models import Category
from sub_category.models import SubCategory
from post.rest.serializers.posts import (
    PostListSerializer,
    PostAddSerializer,
    PostDetailSerializer,
    PostImagesSerializer,
    PostImageAddSerializer,
)
from core.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsPostOwnerOrReadOnly,
    SAFE_METHODS,
)


class AdminPostList(ListAPIView):
    """Views for admin to see all posts"""

    serializer_class = PostListSerializer
    permission_classes = [
        IsAdminUser,
    ]

    def get_queryset(self):
        return Post.objects.select_related("user").prefetch_related(
            Prefetch("category", queryset=Category().get_all_actives()),
            Prefetch("sub_category", queryset=SubCategory().get_all_actives()),
            Prefetch(
                "images",
                queryset=PostImages().get_all_actives(),
            ),
        )


class UserPostList(ListAPIView):
    """Views for user to see user posts"""

    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AdminPostList().get_queryset().filter(user=self.request.user)


class UserPostCreate(CreateAPIView):
    """Views for user to create posts"""

    queryset = Post().get_all_actives()
    serializer_class = PostAddSerializer
    permission_classes = [IsAuthenticated]


class UserPostDetail(RetrieveAPIView):
    """Views for get detail of post"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailSerializer
    lookup_field = "uid"

    def get_object(self):
        return AdminPostList().get_queryset().get(uid=self.kwargs.get("uid"))


class UserPostUpdate(UpdateAPIView):
    """Views for user to update posts"""

    serializer_class = PostAddSerializer
    permission_classes = [IsAuthenticated, IsPostOwnerOrReadOnly]
    lookup_field = "uid"

    def get_object(self):
        return AdminPostList().get_queryset().get(uid=self.kwargs.get("uid"))


class UserPostImagesList(ListCreateAPIView):
    """Views for list and add images in a post"""

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return PostImagesSerializer
        else:
            return PostImageAddSerializer

    def get_queryset(self):
        return PostImages().get_all_actives().filter(post__uid=self.kwargs.get("uid"))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"uid": kwargs.get("uid")}
        )
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save()

        return Response(response_data, status=status.HTTP_201_CREATED)
