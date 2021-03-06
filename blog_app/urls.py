from django.urls import path, re_path, include
from rest_framework import routers
from .views import (
    BlogViewSet,
    TagViewSet,
    ContactViewSet,
    SubscribeViewSet,
    LatestBlogViewSet
)

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'tag', TagViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'subscribe', SubscribeViewSet)
router.register(r'latestblog', LatestBlogViewSet, basename='lastest-blog')

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
