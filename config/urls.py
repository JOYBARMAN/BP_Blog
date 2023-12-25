from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    # user urls
    path("api/v1/users", include("core.rest.urls.base")),
    # profile urls
    path("api/v1/users/profile", include("user_profile.rest.urls.profile")),
    # authentication urls
    path("api/v1/auth/", include("authentication.rest.urls.authentications")),
    # category urls
    path("api/v1/category", include("category.rest.urls.category")),
    # subcategory urls
    path("api/v1/subcategory", include("sub_category.rest.urls.sub_category")),
    # post urls
    path("api/v1/posts", include("post.rest.urls.posts")),
    # post reaction urls
    path("api/v1/posts/<uuid:uid>/reaction", include("post_reaction.rest.urls.post_reaction")),
    # post tag urls
    path("api/v1/tags", include("tag.rest.urls.tag")),
    # silk url
    path("silk/", include("silk.urls", namespace="silk")),
    # Spectacular url
    path('', SpectacularSwaggerView.as_view(), name='api-docs'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
