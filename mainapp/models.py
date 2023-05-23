from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1024, verbose_name='Интро')

    body = models.TextField(verbose_name='Содержание')
    body_as_markdown = models.BooleanField(default=False)

    #   Служебные
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    deleted_at = models.BooleanField(default=False, verbose_name='Удалено')
