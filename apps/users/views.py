from rest_framework import generics, viewsets
from apps.users.models import User, EmailCheckCode
from apps.users.serializers import UserSerializer, RegisterSerializer, EmailCheck, ResetPasswordSerializer, UpdatePasswordSerializer
# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['posts']
    
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class EmailCheckAPIView(generics.CreateAPIView):
    queryset = EmailCheckCode.objects.all()
    serializer_class = EmailCheck
    
class ResetPasswordAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer
    
class UpdatePasswordAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdatePasswordSerializer