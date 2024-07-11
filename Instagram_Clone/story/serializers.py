from rest_framework import serializers
from posts.models import PostModel
from likes.models import LikesModel
from users.models import UserModel
from users.serializers import SignUpSerializer
from story.models import StoryModel


class StorySerializer(serializers.ModelSerializer):
    user = SignUpSerializer(read_only=True)

    class Meta:
        fields = ['__all__']
        model = StoryModel

    # def create(self, validated_data):
    #     user = super(SignUpSerializer, self).create(validated_data)

        
    #     return user
