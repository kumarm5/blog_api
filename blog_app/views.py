from .models import (
    Blog,
    Tags
)

from .serializers import (
    BlogSerializer,
    TagSerializer
)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tags.objects.all()
