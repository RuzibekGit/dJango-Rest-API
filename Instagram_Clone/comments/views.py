from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


from comments.models import CommentsModel, CommentLikeModel
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


class CommentLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        comment_like = CommentLikeModel.objects.filter(pk=pk, user=request.user)

        if comment_like.exists():
            comment_like.delete()
            response = {
                "status": True,
                "message": "Comment unliked"
            }
            return Response(response, status=status.HTTP_200_OK)

        else:
            CommentLikeModel.objects.create(user=request.user, post_id=pk)
            response = {
                "status": True,
                "message": "Comment liked"
            }
            return Response(response, status=status.HTTP_200_OK)
