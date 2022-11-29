from django.shortcuts import render
from .serializers import AuthorSerializer, PublisherSerializer, PostSerializer
from .models import AuthorModel, PublisherModel, PostModel
from rest_framework import generics
from .pagination import PostPagination
from rest_framework import filters

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__first_name']

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer