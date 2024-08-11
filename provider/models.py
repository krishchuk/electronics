from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта', **NULLABLE)
    country = models.CharField(max_length=60, verbose_name='страна')
    city = models.CharField(max_length=60, verbose_name='город')
    street = models.CharField(max_length=60, verbose_name='улица')
    house = models.CharField(max_length=10, verbose_name='дом')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель')
    release_date = models.DateField(default=timezone.now, verbose_name='дата выхода на рынок')

    def __str__(self):
        return f'{self.name} {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Provider(models.Model):
    TYPE = [
        ('завод', 'завод'),
        ('розничная сеть', 'розничная сеть'),
        ('ип', 'индивидуальный предприниматель'),
    ]
    name = models.CharField(max_length=150, verbose_name='название')
    type = models.CharField(max_length=20, choices=TYPE, default='завод', verbose_name='тип')
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, primary_key=False, verbose_name='контакты')
    product = models.ManyToManyField(Product, verbose_name='продукты', **NULLABLE)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    debt = models.FloatField(default=0, verbose_name='задолженность перед поставщиком')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='время создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
