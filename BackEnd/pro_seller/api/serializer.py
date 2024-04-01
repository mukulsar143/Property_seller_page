from rest_framework import serializers
from .models import Property
from accounts.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['role', 'mobile', 'email']

class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = '__all__'  
        
class PropertyGetSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer()

    class Meta:
        model = Property
        fields = '__all__'        