from django.db import models
from django.db.models import Q


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    tag = models.ForeignKey('Tag', related_name='scopes', on_delete=models.PROTECT)
    article = models.ForeignKey('Article', related_name='scopes', on_delete=models.PROTECT)
    is_main = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('article',), condition=Q(is_main=True), name='one_main_per_user')
        ]
        ordering = ['-is_main']

class Tag(models.Model):
    name = models.CharField(max_length=15, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


