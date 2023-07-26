from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateTimeField(
        auto_now_add=False,
        blank=True, 
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='proflie_image/'
    )
    description = models.TextField(
        max_length=555
    )
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
