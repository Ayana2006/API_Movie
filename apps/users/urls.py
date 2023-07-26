from django.urls import path
from apps.users.views import RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
]