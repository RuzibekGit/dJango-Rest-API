from django.shortcuts import render
from users.serializers import SignUpSerializer
from rest_framework import generics, status

from users.models import UserModel


class SignUpCreateAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    model = UserModel
