from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Ticket(models.Model):
    """Заявка клиента на ремонт"""
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('assigned', 'Назначена'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнена'),
        ('closed', 'Закрыта'),
        ('cancelled', 'Отменена'),
    ]

    DEVICE_CHOICES = [
        ('pc', 'Настольный ПК'),
        ('laptop', 'Ноутбук'),
        ('monitor', 'Монитор'),
        ('printer', 'Принтер/МФУ'),
        ('peripheral', 'Периферия'),
        ('other', 'Другое'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    device_type = models.CharField('Тип устройства', max_length=50, choices=DEVICE_CHOICES)
    problem = models.TextField('Описание проблемы')
    preferred_at = models.DateTimeField('Удобное время', null=True, blank=True)
    address = models.CharField('Адрес (если выезд)', max_length=255, blank=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    diagnosis = models.TextField('Диагностика', blank=True)
    final_price = models.DecimalField('Итоговая цена, ₽', max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка #{self.pk} — {self.get_device_type_display()}"

    @property
    def is_active(self):
        return self.status in ['new', 'assigned', 'in_progress']
