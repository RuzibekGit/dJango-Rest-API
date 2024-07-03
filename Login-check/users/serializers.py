from rest_framework import serializers
from users.models import UserModel, ConfirmationModel
# region signup
class SignUpSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        self.fields['email'] = serializers.CharField( max_length=128, required=False)
        
    confirm_password = serializers.CharField( max_length=128)
    uuid = serializers.IntegerField(read_only=True)
    auth_status = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = UserModel
        fields = ['uuid', 'auth_status', 'first_name', 'last_name', 'username', 'password', 'confirm_password']

    def create(self, validated_data):
        
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name'),  
            last_name=validated_data.get('last_name'),  
            email=validated_data.get('email'),  
        )
        return user
    def validate(self, data):
        return self.auth_validate(data=data)

    

    @staticmethod
    def auth_validate(data):
        user_input = str(data['email']).lower()
        password1 = data['password']
        password2 = data['confirm_password']
        data.pop('confirm_password')

        if password1 == password2:
            data['password'] = password1
        else:
            data = {
                'success': False,
                'message': "Please enter correct password confirmation"
            }
            raise serializers.ValidationError(data)
        
        if user_input.endswith('@gmail.com'):
            if UserModel.objects.filter(email=user_input).exists():
                raise serializers.ValidationError("This email is already registered, use resend code api")
            data['email']= user_input
        
            
        else:
            data = {
                'success': False,
                'message': "Please enter a valid phone number or email"
            }
            raise serializers.ValidationError(data)
        
        
        return data

   
# endregion    

