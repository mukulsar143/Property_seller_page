from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import *


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def validate(self, validated_data):
        if User.objects.filter(email = validated_data['email']).exists():
            raise serializers.ValidationError('Username already exists..')
        
        return validated_data
 
    
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            mobile = validated_data['mobile'],
            role = validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data   

  
  
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    role = serializers.CharField()
    
    def validate(self, validated_data):

        if not User.objects.filter(email = validated_data['email']).exists():
            raise serializers.ValidationError('email not exists...')
        
        return validated_data
    
    def get_token(self, validated_data):
        role = validated_data.get('role')
        
        user = authenticate(email = validated_data['email'], password = validated_data['password'])
        

        if user.role != role:
            raise serializers.ValidationError('Role does not match for registered user.')        
        
        token,_ = Token.objects.get_or_create(user = user)
        
        return {'success' : True, 'token' : str(token.key)}
        
          
        
        