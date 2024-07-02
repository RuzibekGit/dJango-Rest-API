from rest_framework import serializers
from users.models import UserModel
# region signup
class SignUpSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        self.fields['email'] = serializers.CharField( max_length=128, required=False)
        
    password_confirmation = serializers.CharField( max_length=128)
    uuid = serializers.IntegerField(read_only=True)
    auth_status = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = UserModel
        fields = ['uuid', 'auth_status', 'first_name', 'last_name', 'username', 'password', 'password_confirmation']



    def validate(self, data):
        return self.auth_validate(data=data)
    
 

    @staticmethod
    def auth_validate(data):
        user_input = str(data['email']).lower()
        password1 = data['password']
        password2 = data['password_confirmation']

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
            data = {
                'email': user_input,
            }
        else:
            data = {
                'success': False,
                'message': "Please enter a valid phone number or email"
            }
            raise serializers.ValidationError(data)
        return data

   
# endregion    

class UpdateUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'password']

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            response = {
                "success": False,
                "message": "Passwords don't match"
            }
            raise serializers.ValidationError(response)

        # todo | min 8 length, numbers and letters
        return data

    def validate_username(self, username):
        if UserModel.objects.filter(username=username).exists():
            response = {
                "success": False,
                "message": "Username is already gotten"
            }
            raise serializers.ValidationError(response)
        return username

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)

        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
            instance.save()
        return instance
# endregion