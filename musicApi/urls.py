"""musicApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from .api import router

from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        default_version = 'v1',
        description = "A music api containing genres, albums, and users",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="igwep297@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('the-admin-area/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/music/', include('music.urls')),
    path('api/v1/user-playlists/', include('user_playlists.urls')),
    
    # 3RD PARTY APPS URLS
    # path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls.jwt')),
    # path("api/auth/", include("accounts.urls")),
    path("api/auth/", include("djoser.urls")),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
