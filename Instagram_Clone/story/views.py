from django.shortcuts import render
from rest_framework import generics, status

from story.serializers import StorySerializer
from story.models import StoryModel

class StoryCreateAPIView(generics.CreateAPIView):
    # permission_classes = [AllowAny]
    serializer_class = StorySerializer
    model = StoryModel


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


