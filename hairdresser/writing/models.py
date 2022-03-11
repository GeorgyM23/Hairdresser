# coding=utf-8
from django.db import models


class Records(models.Model):
    name_user = models.CharField('Имя', max_length=50)
    surname_user = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('Почта')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.name_user

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

