from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'date_of_birth','profile_image','description', 'email')
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password])
    confirm_password = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = User
        fields = ('username','password', 'confirm_password' )
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':"Пароли отличаются"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 
            
        