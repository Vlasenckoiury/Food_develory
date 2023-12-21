## -*- coding: utf-8 -*-
from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20)
    img = models.TextField(verbose_name='Картинка')
    price = models.CharField(verbose_name='Цена', max_length=10)
    weight = models.TextField(verbose_name='Вес')
    description = models.TextField(verbose_name='Состав')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-id']  # сортировка(фильтр)
