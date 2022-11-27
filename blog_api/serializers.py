from rest_framework import serializers
from .models import AuthorModel, PublisherModel, PostModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    published_by = PublisherSerializer()

    class Meta:
        model = PostModel
        fields = '__all__'