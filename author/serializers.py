from rest_framework import serializers

from author.models import AuthorModel



class AuthorSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    
    
    def create(self, validated_data):
        return AuthorModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name   = validated_data.get('first_name', instance.first_name)
        instance.last_name    = validated_data.get('last_name', instance.last_name)
        instance.email        = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.age          = validated_data.get('age', instance.age)
        instance.save()

        return instance

    def validate(self, attrs):
        age   = attrs.get('age')
        email = attrs.get('email')
        phone = attrs.get('phone_number')

        user_id = self.instance.id if self.instance else None


        if age and not isinstance(age, int):
            raise serializers.ValidationError('Age must be an integer')
        
        if AuthorModel.objects.filter(email=email).exclude(id=user_id).exists():
            raise serializers.ValidationError('This email already exists.')

        if AuthorModel.objects.filter(phone_number=phone).exclude(id=user_id).exists():
            raise serializers.ValidationError('This phone number already exists.')

        return attrs
