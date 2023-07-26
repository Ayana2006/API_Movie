from rest_framework import generics, viewsets
from apps.users.models import User
from apps.users.serializers import UserSerializer, RegisterSerializer
# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['posts']
    
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer