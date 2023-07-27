from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password
from apps.users.models import User, EmailCheckCode

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
            
class EmailCheck(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    code = serializers.CharField(read_only=True)
    class Meta:
        model = EmailCheckCode
        fields = ['email', 'code']
        
    def create(self, validated_data):
        if User.objects.filter(email=validated_data['email']).exists():
            user = User.objects.get(email = validated_data['email'])
            code = EmailCheckCode.objects.create(user = user, email=validated_data['email'])
            code.save()
            email_body = f"""
                Здравствуйте,
                вот ваш ферифиционный код {code.code}
            """
            send_mail(
                #subject 
                    f"Код подтверждения", 
                    #message 
                    email_body, 
                    #from email 
                    'noreply@somehost.local', 
                    #to email 
                    [user.email] 
            )
            return code
        
class ResetPasswordSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password])
    confirm_password = serializers.CharField(write_only = True, required = True)
    
    class Meta:
        model = User
        fields = ['code', 'password', 'confirm_password']
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':"Пароли отличаются"})
        if EmailCheckCode.objects.all().filter(code = attrs['code']).exists() == False:
            raise serializers.ValidationError({'code':"Такого кода нет"})
        return attrs
     
    def create(self, validated_data):
        email_check = EmailCheckCode.objects.all().filter(code = validated_data['code'])
        user = User.objects.get(email = email_check[0].email)
        user.set_password(validated_data['password'])
        user.save()
        for i in email_check:
            i.delete()
        return user
    
    
class UpdatePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only = True, required = True)
    new_password = serializers.CharField(write_only = True, required = True, validators = [validate_password])
    confirm_password = serializers.CharField(write_only = True, required = True)
    
    class Meta:
        model = User
        fields = [ 'old_password', 'new_password', 'confirm_password']
        
    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'new_password':"Пароли отличаются"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.get(username = validated_data['username'] )
        user.set_password(validated_data['new_password'])
        user.save()
        return user 