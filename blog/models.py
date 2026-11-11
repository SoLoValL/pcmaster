from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    """Статья для блога"""
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True)
    content = models.TextField('Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    is_published = models.BooleanField('Опубликована', default=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
