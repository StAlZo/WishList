from django.db import models
from django.contrib.auth.models import AbstractUser
from wishlist.models import Status
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name='Почтовый адрес', unique=True)
    login = models.CharField(max_length=100, verbose_name="Логин")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.name