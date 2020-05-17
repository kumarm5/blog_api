from django.urls import path, re_path, include
from rest_framework import routers
from .views import (
    BlogViewSet,
    TagViewSet
)

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
