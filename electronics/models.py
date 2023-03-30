from django.conf import settings
from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house = models.PositiveIntegerField(verbose_name='Номер дома')


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.email}'


class Product(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title} ({self.model})'


class TradeNetwork(models.Model):

    FACTORY = 'Factory'
    RETAIL = 'Retail'
    SELLER = 'Seller'

    NETWORK_LEVEL = (
        ('Factory', 'Завод'),
        ('Retail', 'Розничная сеть'),
        ('Seller', 'Индивидуальный предприниматель'))

    level = models.CharField(max_length=50, choices=NETWORK_LEVEL, verbose_name='уровень иерархии')
    title = models.CharField(max_length=50, verbose_name='Название')
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, verbose_name='Контакт', **NULLABLE)
    products = models.ForeignKey(Product, verbose_name='Продукты', on_delete=models.SET_NULL, **NULLABLE)
    supplier = models.ForeignKey("self", verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    debt = models.FloatField(verbose_name='Задолженность перед поставщиком', **NULLABLE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Торговая сеть'
        verbose_name_plural = 'Торговые сети'

    def __str__(self):
        return f'{self.title}'


