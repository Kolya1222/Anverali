from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Metric_name_CHOICES = [
        ('is_admin', 'Администратор'),
        ('is_executor', 'Исполнитель'),
        ('is_employer', 'Заказчик')
    ]
    Metric_name = models.CharField(max_length=70,choices=Metric_name_CHOICES,default="",verbose_name='Выберите роль')
    aboutme = models.CharField(max_length=500,default="", verbose_name='О себе')