from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from comments.models import CommentsModel
from comments.serializers import  CommentSerializer
from shared.pagination import CustomPagination


class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return CommentsModel.objects.filter(post_id=post_id)


class PostCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # if (parent_id := serializer.data['parent']):
        #     serializer.save(parent_id=parent_id)
        post_id = self.kwargs.get('pk')
        serializer.save(user=self.request.user, post_id=post_id)
