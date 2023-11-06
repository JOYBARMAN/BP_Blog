from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # user urls
    path("api/v1/users", include("core.rest.urls.base")),
    # profile urls
    path("api/v1/users/profile", include("user_profile.rest.urls.profile")),
    # authentication urls
    path("api/v1/auth/", include("authentication.rest.urls.authentications")),
    # silk url
    path("silk/", include("silk.urls", namespace="silk")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
