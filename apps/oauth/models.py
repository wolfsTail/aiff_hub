from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser

from apps.base.services import get_path_upload_avatar, validate_size_image


class AuthUser(AbstractUser):
    """
    Extended user model
    """
    email = models.EmailField(max_length=128,
                              unique=True, 
                              verbose_name='Email')
    join_date = models.DateTimeField(auto_now_add=True, 
                                     verbose_name='Дата регистрации')
    country = models.CharField(max_length=32, 
                               verbose_name='Страна проживания', 
                               blank=True, 
                               null=True)
    city = models.CharField(max_length=32, 
                            verbose_name='Город проживания', 
                            blank=True, 
                            null=True)
    bio = models.TextField(verbose_name='О себе', 
                           blank=True, 
                           null=True)
    username = models.CharField(max_length=32, 
                                    verbose_name='Username', 
                                    blank=True, 
                                    null=True)
    avatar = models.ImageField(verbose_name='Аватар', 
                               blank=True, 
                               null=True, 
                               upload_to=get_path_upload_avatar, 
                               validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']),
                                           validate_size_image])

    class Meta:
        verbose_name = 'Пользователя приложения'
        verbose_name_plural = 'Пользователи приложения'

    def __str__(self):
        return self.email

    @property
    def is_authenticated(self):
        """All time return True. This is required by Django"""
        return True
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]    


class Followers(models.Model):
    """
    Followers model
    """
    user = models.ForeignKey(AuthUser, 
                             on_delete=models.CASCADE, 
                             related_name='owner',
                             verbose_name='Владелец')
    subscriber = models.ForeignKey(AuthUser, 
                                on_delete=models.CASCADE,
                                related_name='subscribers',
                                verbose_name='Подписчик')
    
    class Meta:
        verbose_name = 'Подписчика'
        verbose_name_plural = 'Подписчики'
    
    def __str__(self) -> str:
        return f"{self.subscriber} -> {self.user}"


class SocialLink(models.Model):
    """
    User's social link model
    """
    user = models.ForeignKey(AuthUser, 
                             on_delete=models.CASCADE, 
                             related_name='social_links',
                             verbose_name='Владелец')
    link = models.URLField(max_length=255)

    def __str__(self) -> str:
        return f"{self.user}"
