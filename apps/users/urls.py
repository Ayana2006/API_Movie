from django.urls import path
from apps.users.views import RegisterAPIView, EmailCheckAPIView, ResetPasswordAPIView, UpdatePasswordAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('check_email/', EmailCheckAPIView.as_view()),
    path('reset_password/', ResetPasswordAPIView.as_view()),
    path('update_password/<int:pk>/', UpdatePasswordAPIView.as_view()),
]

