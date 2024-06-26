from rest_framework import serializers

from users.models import UserModel, VIA_EMAIL, VIA_PHONE
from shared.utils import send_code_to_email, send_code_to_phone



class SignUpSerializer(serializers.Serializer):
    def __init__(self):
        super(SignUpSerializer, self).__init__()
        self.fields['email_phone_number'] = serializers.CharField(max_length=256)
    
    class Meta:
        model = UserModel
        fields = ['uuid', 'auth_type', 'auth_status','email_phone_number']

    def create(self, validated_data):
        user = super(SignUpSerializer, self).create(validated_data)
        code= user.create_verify_code(verify_type=user.verify_type)
        if user.verify_type == VIA_EMAIL:
            send_code_to_email(user.email, code)
        else:
            send_code_to_phone(user.phone_number, code)
        
        user.save()
        return user
    


    def validate(self, attrs):
        return self.auth_validate(attrs)
    
    @staticmethod
    def auth_validate(data):
        user_input = str(data.get('email_phone_number', None))
        if user_input.endswith('@gmail.com'):
            data['email'] = user_input
            data['auth_type'] = VIA_EMAIL
        elif user_input.startswith('+'):
            data['phone_number'] = user_input
            data['auth_type'] = VIA_PHONE
        else:
            response = {
                'success': False,
                'message': 'Invalid email or phone number'
            }
            raise serializers.ValidationError(response)