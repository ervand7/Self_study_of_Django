from django.urls import path
from .views import *

"""
Импортируем для списка построения маршрутов функцию path. Также создаем ту же самую переменную urlpatterns со
списком адресов. Но этот список адресов уже будет формировать функция path. Первым параметром мы должны указать маршрут.
Вспоминаем, что при нахождении, Джанго отбрасывает некоторые ненужные части маршрута. Когда мы нашли такой адрес 
'news/', мы в итоге (из-за того, что Джанго все время отбрасывает соответствие), мы получили '' вместо 'news/'. Именно 
эту пустую строку мы и должны указать первым параметром. Теперь импортируем функцию index.

Итак. Когда маршрутизатор в адресной строке встречает 'news/', он встречает это и для такого адреса
http://127.0.0.1:8000/news/test/, и для такого адреса http://127.0.0.1:8000/news/. При этом он отбрасывает такие 
адреса: 'news/' и 'news/test/'. Поэтому для 'news/' у нас получается '', а для 'news/test' у нас получается 'test/'.
"""

urlpatterns = [
    path('', index)
    # path('test/', test)  # Это у нас только для начальных уроков было.
]

