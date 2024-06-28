from django.urls import path
from users.views import (SignUpCreateAPIView, 
                         VerifyCodeAPIView, 
                         UpdateUserAPIView, 
                         ResendVerifyCodeAPIView, 
                         UpdateAvatarAPIView)

app_name = 'users'

urlpatterns = [
    path('register/', SignUpCreateAPIView.as_view(), name='register'),
    path('verify/', VerifyCodeAPIView.as_view(), name='verify'),
    path('update/', UpdateUserAPIView.as_view(), name='update'),
    path('resend_code/', ResendVerifyCodeAPIView.as_view(), name='resend'),
    path('update-avatar/', UpdateAvatarAPIView.as_view(), name='update_avatar'),

]
