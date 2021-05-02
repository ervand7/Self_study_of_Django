from django.db import models


class News(models.Model):
    title = models.CharField(  # https://django.fun/docs/django/ru/3.0/ref/models/fields/#charfield
        max_length=150,
        verbose_name='Наименование'
    )
    content = models.TextField(
        blank=True,  # означает, что данный атрибут необязателен к заполнению. По умолчанию все поля обязательны
        verbose_name='Контент'  # к заполнению. Если ничего не напишем, то Джанго подставит пустую строку.
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  # дата будет обновляться не более 1 раза
        verbose_name='Дата публикации'
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # в отличие от auto_now_add тут дата будет обновляться при каждом редактировании новости
        verbose_name='Обновлено'
    )
    photo = models.ImageField(  # этот класс провалидирует, чтобы файл был именно изображением
        upload_to='photos/%Y/%m/%d/',  # указывает, куда загружается файл, например: photos/2021/01/24
        verbose_name='Фото',
        blank=True
    )
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,  # защищает категорию от удаления. # Внимание! PROTECT здесь должен быть без ()
        null=True,  # null=True позволит не заполнять поля
        verbose_name='Категория'
    )

    def __str__(self):
        """Это мы прописываем, чтобы в консоли при распечатке News.objects.all()
        мы получали строковое представление объекта."""
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
