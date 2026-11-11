from django.db import models


class ContactMessage(models.Model):
    """Сообщение из формы обратной связи"""
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20, blank=True)
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Отправлено', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']

    def __str__(self):
        return f"От {self.name}"
