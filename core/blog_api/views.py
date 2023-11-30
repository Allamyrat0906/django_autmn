from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostDetail(generics.ListCreateAPIView):
    queryset=Post.postobjects.all()
    serializer_class=PostSerializer    

class ListDetail(generics.RetrieveDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer    

