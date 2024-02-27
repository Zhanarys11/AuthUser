from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(
        upload_to = 'users_images/',
        null=True,
        blank=True,
        verbose_name='Изображение',
        help_text='Изображение пользователя'
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        null =True,
        verbose_name='Биография',
        help_text='Краткая информация о пользователе'
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Местоположение',
        help_text='Местоположение пользователя'
    )
    phone_number= models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Номер телефона',
        help_text='Введите номер телефона пользователя'
    )

    def __str__(self) -> str:
        if self.username:
            return self.username
        return f"{self.id}: Анонимный пользователь"
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural='Пользователи'
        ordering = ["-date_joined"]