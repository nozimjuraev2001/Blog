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


    def create(self, validated_data):
        author = validated_data.pop('author')
        published_by = validated_data.pop('published_by')
        post = PostModel.objects.create(**validated_data)
        return post





