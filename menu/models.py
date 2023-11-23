## -*- coding: utf-8 -*-
from django.db import models


class Pizza(models.Model):
    pizza_name = models.CharField(verbose_name='Название пиццы', max_length=20)
    pizza_img = models.TextField(verbose_name='Картинка')
    pizza_price = models.CharField(verbose_name='Цена', max_length=10)
    pizza_weight = models.TextField(verbose_name='Вес')
    pizza_description = models.TextField(verbose_name='Состав')

    def __str__(self):
        return self.pizza_name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['-id']  # сортировка(фильтр)
