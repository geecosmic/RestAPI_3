# from rest_framework import serializers
# from .models import Members
# from rest_framework.authtoken.models import Token


# from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password')


# class MemberSerializers(serializers.ModelSerializer):
#   class Meta:
#     model = Members
#     fields = ["id","keynum","name","degree","status","phone","address","office","tac","hm"]









from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Members, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

