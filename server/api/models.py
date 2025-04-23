from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class StuffType(models.TextChoices):
    HOODIE = 'hoodie', 'капюшонка'
    JEANS = 'jeans', 'жинсы'
    TSHIRT = 't-shirt', 'футболка'
    LONGSLEEVE = 'longsleeve', 'лонгслив'
    DRESS = 'dress', 'юбка'
    OUTERWEAR = 'outerwear', 'верхняя одежда'
    OTHERS = 'others', 'другое'


class StuffSize(models.TextChoices):
    XXS = 'xxs'
    XS = 'xs'
    S = 's'
    M = 'm'
    L = 'l'
    XL = 'xl'
    XXL = 'xxl'
    ONE_SIZE = 'one size', 'один размер'


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Почта",
        null=False,
        unique=True,
    )
    city = models.CharField(
        verbose_name="Город",
        max_length=32,
        null=True,
        unique=False,
    )

    USERNAME_FIELD = 'email'


class Item(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=32,
        null=False,
        unique=False,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=False,
    )
    color = models.CharField(
        verbose_name="Расцветка",
        max_length=32,
        null=False,
        unique=False,
    )
    stuff_type = models.CharField(
        verbose_name="Тип",
        max_length=16,
        choices=StuffType.choices,
        null=False,
        unique=False
    )
    stuff_size = models.CharField(
        verbose_name="Размер",
        max_length=16,
        choices=StuffSize.choices,
        null=False,
        unique=False   
    )
    price = models.PositiveBigIntegerField(
        verbose_name="Цена",
        null=False,
        unique=False, 
    )
