from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150)  # https://django.fun/docs/django/ru/3.0/ref/models/fields/#charfield
    content = models.TextField(blank=True)  # означает, что данный атрибут необязателен к заполнению. По умолчанию все
    # поля обязательны к заполнению. Если ничего не напишем, то Джанго подставит пустую строку.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # атрибут upload_to указывает на то, куда загружать фото.
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
