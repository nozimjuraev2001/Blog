from django.shortcuts import render
from .serializers import AuthorSerializer, PublisherSerializer, PostSerializer
from .models import AuthorModel, PublisherModel, PostModel
from rest_framework import generics

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer