from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    is_main = models.BooleanField(default=False, verbose_name='Основной')


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles', verbose_name='Теги')

    class Meta:
        verbose_name = 'Связь статьи и тега'
        verbose_name_plural = 'Связи статей и тегов'

    def __str__(self):
        return f'{self.article.title} <-> {self.tag.name}'
