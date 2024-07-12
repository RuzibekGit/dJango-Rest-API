from rest_framework import serializers

from posts.serializers import UserSerializer
from story.models import StoryModel, StoryViewModel, StoryReactionModel, StoryReportModel


class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    expire_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = StoryModel
        fields = '__all__'


class StoryViewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = StoryViewModel
        fields = '__all__'


class StoryReactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = StoryReactionModel
        fields = '__all__'


class StoryReportSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = StoryReportModel
        fields = '__all__'
