from django.urls import path
from users.views import SignUpCreateAPIView

app_name = 'users'

urlpatterns = [
    path('register/', SignUpCreateAPIView.as_view(), name='register'),

]
