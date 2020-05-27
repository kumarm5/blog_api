from django.urls import path, re_path, include
from rest_framework import routers
from .views import (
    BlogViewSet,
    TagViewSet,
    ContactViewSet,
    SubscribeViewSet
)

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'tag', TagViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'subscribe', SubscribeViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
