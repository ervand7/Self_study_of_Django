from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name='Наименование')  # https://django.fun/docs/django/ru/3.0/ref/models/fields/#charfield
    content = models.TextField(blank=True,
                               verbose_name='Контент')  # означает, что данный атрибут необязателен к заполнению. По умолчанию все
    # поля обязательны к заполнению. Если ничего не напишем, то Джанго подставит пустую строку.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото',
                              blank=True)  # атрибут upload_to указывает на то, куда загружать фото.
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')  #
    # on_delete=models.PROTECT защищает категорию от удаления. Внимание! PROTECT здесь должен быть без ()
    # null=True позволит не заполнять поля

    def __str__(self):
        return self.title

    class Meta:
        """verbose_name - это наименование модели в единственном числе
        verbose_name - это наименование модели во множественном числе"""
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')  # атрибут

    # db_index индексирует это поле

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
