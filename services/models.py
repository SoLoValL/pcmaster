from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Service(models.Model):
    """Каталог услуг"""
    DEVICE_CHOICES = [
        ('pc', 'Настольный ПК'),
        ('laptop', 'Ноутбук'),
        ('monitor', 'Монитор'),
        ('printer', 'Принтер/МФУ'),
        ('peripheral', 'Периферия'),
        ('other', 'Другое'),
    ]

    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    device_type = models.CharField('Тип устройства', max_length=50, choices=DEVICE_CHOICES)
    price = models.DecimalField('Цена, ₽', max_digits=10, decimal_places=2, default=0)
    duration_hours = models.FloatField('Длительность, часы', default=1)
    is_published = models.BooleanField('Опубликована', default=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-is_published', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_device_type_display()})"


class Skill(models.Model):
    """Навык мастера"""
    name = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name
