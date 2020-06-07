from rest_framework import serializers
from .models import (
    Blog,
    Tags,
    Contact,
    Subscribe
)
from datetime import datetime


class BlogSerializer(serializers.ModelSerializer):

    tag_id = serializers.SerializerMethodField(source='get_tag_id')

    def get_tag_id(self, obj):
        return obj.tag.id

    def to_representation(self, instance):
        data = super(BlogSerializer, self).to_representation(instance)

        created_at = datetime.strftime(instance.created_at, '%d-%m-%Y')
        updated_at = datetime.strftime(instance.updated_at, '%d-%m-%Y')

        data.update({'created_at': created_at})
        data.update({'updated_at': updated_at})
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
