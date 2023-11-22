"""Views for post"""

from django.db.models import Prefetch

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    CreateAPIView,
)

from post.models import Post
from category.models import Category
from sub_category.models import SubCategory
from post.rest.serializers.posts import (
    PostListSerializer,
    PostAddSerializer,
    PostDetailSerializer,
)
from core.permissions import (
    IsAuthenticated,
    IsAdminUser,
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
