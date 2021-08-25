from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import re
from django.core.exceptions import ValidationError

from django.contrib.auth.models import AbstractUser

class Point(models.Model):
    lat = models.DecimalField(
            'Широта',
            default=0,
            decimal_places = 7,
            max_digits = 10
            )
    lng = models.DecimalField(
            'Долгота',
            default=0,
            decimal_places = 7,
            max_digits = 10
            )
    #size = fields.IntegerRangeField(min_value=-100, max_value=100)
    fullness = models.IntegerField(
            'Заполненость',
            default=0,
            validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    capacity = models.IntegerField(
            'Вместимость',
            validators=[
            MinValueValidator(0)
        ])

    def __str__(self):
        return str("Широта:"+str(self.lat)+" Долгота:"+str(self.lng))

    class Meta:
        verbose_name = 'Точка сбора мусора'
        verbose_name_plural = 'Точки сбора мусора'


class Truck(models.Model):
    lat = models.DecimalField(
            'Широта',
            default=0,
            decimal_places = 7,
            max_digits = 10
            )
    lng = models.DecimalField(
            'Долгота',
            default=0,
            decimal_places = 7,
            max_digits = 10
            )
    registrationMark = models.CharField(
            'Номерной знак',
             max_length=10
             )
    points = models.ManyToManyField(
            Point,
            verbose_name = 'Обслуживаемые точки'
            )

    def __str__(self):
        return str(self.registrationMark)

    class Meta:
        verbose_name = 'Мусоровоз'
        verbose_name_plural = 'Мусоровозы'


class User(AbstractUser):
    truck = models.ForeignKey(
            Truck,
            verbose_name = 'Обслуживаемые мусоровозы',
            on_delete = models.CASCADE,
            null = True,
            blank = True,
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'
