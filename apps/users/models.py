from django.db import models
from django.contrib.auth.models import AbstractUser
import random
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

class EmailCheckCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    code = models.CharField(
        max_length=6,
        blank=True, 
        null=True,
        unique=True
    )
    def generate_field_value(self):
        # Генерация случайной строки из цифр
        return ''.join(random.choices('0123456789', k=6))

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_field_value()
        super().save(*args, **kwargs)