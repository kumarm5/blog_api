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


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


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
