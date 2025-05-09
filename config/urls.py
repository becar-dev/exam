from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from configapp.views import TeacherViewSet

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='teacher')

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenBlacklistView)

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Admin-only API for Teachers and Students",  #O'qituvchilar va talabalar uchun faqat administrator API
    ),
    public=True,

    permission_classes=(permissions.AllowAny,),

)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('configapp.urls')),
    path('tokenref', TokenRefreshView.as_view(), name='token'),
    path('tokenac', TokenBlacklistView.as_view(), name='token'),
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

