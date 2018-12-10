# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your models here.
from django.db import models



class Country(models.Model):
    name = models.CharField(max_length=100,verbose_name = 'Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = '1.Страны'

class Oblast(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name = 'Номер области')
    name = models.CharField(max_length=100, verbose_name = 'Область')
    country = models.ForeignKey(Country,on_delete=models.CASCADE, verbose_name = 'Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = '2.Области'

class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Регион')
    oblast = models.ForeignKey(Oblast,on_delete=models.CASCADE, verbose_name = 'Область')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = '3.Регионы'

class RuralDistrict(models.Model):
    name =  models.CharField(max_length=100,verbose_name = 'Сельский округ')
    region = models.ForeignKey(Region, on_delete=models.CASCADE,verbose_name = 'Регион')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сельский округ'
        verbose_name_plural = '4.Сельские округи'

class Village(models.Model):
    name = models.CharField(max_length=100,verbose_name = 'Поселок')
    ruraldistrict = models.ForeignKey(RuralDistrict,on_delete=models.CASCADE,verbose_name = 'Сельский округ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поселки'
        verbose_name_plural = '5.Поселок'

class Farmer(models.Model):
    id = models.CharField(max_length=50,primary_key=True,verbose_name = 'ИИН')
    name = models.CharField(max_length=50,verbose_name = 'ФИО')
    phone = models.CharField(max_length=20,verbose_name = 'Номер телефона')
    email = models.EmailField(max_length=40,verbose_name = 'почта')
    address = models.CharField(max_length=50,verbose_name = 'Адрес')
    coordinate = models.CharField(max_length=1000,verbose_name = 'Координаты',help_text="Координаты дома(можно посмотреть в google map)")
    village = models.ForeignKey(Village,on_delete=models.CASCADE, verbose_name = 'Поселок')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Фермер'
        verbose_name_plural = '6.Фермеры'



