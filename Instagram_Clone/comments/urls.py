from django.urls import path

from comments.views import PostCommentListView, PostCommentCreateView

app_name = 'comment'

urlpatterns = [
    path('<int:pk>/', PostCommentListView.as_view(), name='comments-list'),
    path('<int:pk>/create/', PostCommentCreateView.as_view(), name='comments-create'),

]
