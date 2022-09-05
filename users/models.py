from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(
        verbose_name=_('Номер телефона'),
    )
    full_name = models.CharField(
        verbose_name=_('ФИО'),
        max_length=60,
    )

    class Meta:
        ordering = ['full_name']
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.full_name
