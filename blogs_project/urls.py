
# from django.contrib import admin
# from django.urls import path, include
# from .yasg import urlpatterns as doc_urls

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blogs.urls')),
# ]

# urlpatterns+=doc_urls

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
       title="BitCamp RedberryBlogs list App",
       default_version='v1',
       description="API documentation for my App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('blogs.urls')),
]

