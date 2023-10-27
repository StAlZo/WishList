from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name='Почтовый адрес', unique=True)
    login = models.CharField(max_length=100, verbose_name="Логин")
    #password =
    status_id =

    def __str__(self):
        return self.name