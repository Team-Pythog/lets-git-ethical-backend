from django.contrib.auth.models import User
from rest_framework import  serializers
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'image', 'header', 'bio')
