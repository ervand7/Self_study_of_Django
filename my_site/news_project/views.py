from django.http import HttpResponse
from django.shortcuts import render
from .models import News

"""
Пропишем контроллер функции. Обычно такую функцию называют index. 
Все контроллеры функций должны на вход принимать 
обязательный аргумент - экземпляр класса HttpRequest, который называется request. 
В этом объекте хранятся данные о полученном запросе, о клиенте, о его браузере, 
куки, данные сессии, заголовки и тд.
"""


def index(request):
    news = News.objects.all()
    context = {
        'news_project': news,
        'title': 'Список новостей'
    }
    return render(
        request, template_name='news_project/index.html', context=context
    )
