# Default
from django.shortcuts import render
############ added object ################
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


# Create your views here.
class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

