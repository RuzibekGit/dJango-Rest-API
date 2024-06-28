from django.utils import timezone
from django.core.exceptions import ValidationError

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FileUploadParser

from shared.utils import send_code_to_email, send_code_to_phone
from users.models import UserModel, ConfirmationModel, CODE_VERIFIED, DONE, VIA_EMAIL
from users.serializers import SignUpSerializer, UpdateUserSerializer



class SignUpCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer
    model = UserModel


class VerifyCodeAPIView(APIView):
    permission_classes = [IsAuthenticated]

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
        

        


class UpdateUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UpdateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(user, serializer.validated_data)
            serializer.save()

            user.auth_status = DONE
            user.save()

            response = {
                "success": True,
                "message": "Updated successfully",
                "auth_status": DONE,
                "access_token": user.tokens()['access_token'],
                "refresh_token": user.tokens()['refresh_token']
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                "success": True,
                "message": "Invalid request body",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ResendVerifyCodeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user

        if user.auth_status == CODE_VERIFIED:
            response = {
                'success': False,
                'message': "Your account is already verified."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        code = user.create_verify_code(user.auth_type)

        if user.auth_type == VIA_EMAIL:
            send_code_to_email(user.email, code)
        else:
            send_code_to_phone(phone_number=user.phone_number, code=code)

        user.confirmation_model.code = code
        user.confirmation_model.save()

        response = {
            'success': True,
            'message': "Verification code has been resent to your " + user.auth_type
        }
        return Response(response, status=status.HTTP_200_OK)



class UpdateAvatarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FileUploadParser]

    def put(self, request, *args, **kwargs):
        user = self.request.user

        if 'avatar' not in request.data:
            return Response({'message': 'No avatar provided.'}, status=status.HTTP_400_BAD_REQUEST)

        avatar_file = request.data['avatar']

        try:
            avatar_file.validate(limit_value=1024 * 1024)
        except ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Update user avatar
        user.avatar = avatar_file
        user.save()

        response = {
            'success': True,
            'message': 'Avatar updated successfully.'
        }
        return Response(response, status=status.HTTP_200_OK)
