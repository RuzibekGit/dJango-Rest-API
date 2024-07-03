from django.shortcuts import render
from users.serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response


from users.models import UserModel, ConfirmationModel, CODE_VERIFIED


class SignUpCreateAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    model = UserModel

    


class VerifyCodeAPIView(APIView):

    def post(self, request, *args, **kwargs):
        user = self.request.user
        code = request.data.get('code')

        verification_code = ConfirmationModel.objects.filter(
            user_id=user.id, code=code, is_confirmed=False, expiration_time__gte=timezone.now())
        
        if verification_code.exists():
            user.auth_status = CODE_VERIFIED
            user.save()

            verification_code.update(is_confirmed=True)

            response = {
                'success': True,
                'message': "Your code is successfully verified.",
                'auth_status': CODE_VERIFIED,
                'access_token': user.tokens()['access_token']
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'success': False,
                'message': "Your code is invalid or already expired"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
