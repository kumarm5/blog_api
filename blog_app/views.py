from .models import (
    Blog,
    Tags,
    Contact,
    Subscribe
)

from .serializers import (
    BlogSerializer,
    TagSerializer,
    ContactSerializer,
    SubscribeSerializer
)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .pagination import BlogPagination


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    pagination_class = BlogPagination
    # queryset = Blog.objects.all()

    def get_queryset(self):
        queryset = Blog.objects.all()
        query = self.request.query_params.get('query', None)
        tag = self.request.query_params.get('tag', None)

        if query is not None:
            queryset = Blog.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(short_description__icontains=query)
            ).distinct()
        elif tag is not None:
            queryset = Blog.objects.filter(
                tag_id=tag
            )

        return queryset


class TagViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tags.objects.all()


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class SubscribeViewSet(viewsets.ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()


class LatestBlogViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    # queryset = Blog.objects.all()

    def get_queryset(self):
        queryset = Blog.objects.all().order_by('-id')[:1]
        return queryset
