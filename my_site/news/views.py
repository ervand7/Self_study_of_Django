from django.shortcuts import render
from django.http import HttpResponse

"""Create your views here.
Пропишем контроллер функции. Обычно такую функцию называют index.
Все контроллеры функций должны на вход принимать обязательный аргумент - экземпляр класса HttpRequest, который
называется request. В этом объекте хранятся данные о полученном запросе, о клиенте, о его браузере, куки,
данные сессии, заголовки и тд."""


def index(request):
    """Мы можем даже распечатать и посмотреть, что в этом request содержится.
    print(dir(request))  # в терминале этот request выглядит как <WSGIRequest: GET '/news/'>
    Итак, мы получили какой-то запрос. И нам нужно вернуть какой-то ответ. Возвращать мы будем Http-объект с помощью
    класса HttpResponse. Его мы импортируем from django.http import HttpResponse. И будем его же возвращать.
    Вызываем конструктор данного класса и в качестве параметра даем какой-то текст."""
    return HttpResponse('Hello world')


def test(request):
    """Создадим еще одну функцию, которая будет возвращать строку 'Тестовая страница'. Но обернем ее уже в теги."""
    return HttpResponse('<h1>Тестовая страница</h1>')