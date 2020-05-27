from rest_framework import serializers
from .models import (
    Blog,
    Tags,
    Contact,
    Subscribe
)


class BlogSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super(BlogSerializer, self).to_representation(instance)
        data.update({'user': instance.user.username})
        data.update({'tag': instance.tag.tag_name})
        return data

    class Meta:
        model = Blog
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
