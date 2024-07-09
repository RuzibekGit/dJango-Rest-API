from django.urls import path

from comments.views import PostCommentListView, PostCommentCreateView, CommentLikeView

app_name = 'comment'

urlpatterns = [
    path('<int:pk>/', PostCommentListView.as_view(), name='comments-list'),
    path('<int:pk>/create/', PostCommentCreateView.as_view(), name='comments-create'),
    path('<int:pk>/like/', CommentLikeView.as_view(), name='comments-like'),

]
