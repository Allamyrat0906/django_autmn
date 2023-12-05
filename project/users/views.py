from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics
from .models import User

class UserCreateList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserUpdateDelte(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer