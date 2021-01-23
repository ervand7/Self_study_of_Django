"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news.views import *  # чтобы не импортировать по отдельности каждую функцию из views, ставим *

"""
Соответственно из приложения news, а точнее из его модуля с контроллерами (<views>), мы импортируем
контроллер index. Редактор начинает жаловаться из-за неверной корневой директории. Мы через настройки
Pycharm меняем статус корневой директоии, присваивая для директории
</Users/USER/Desktop/Python/Dlango_project/my_site> статус корневой папки.
Провалившись в документацию функции _path мы увидим, что она принимает в себя несколько параметров:
def _path(route, view, kwargs=None, name=None, Pattern=None).
Итак, это первый вариант, без использования include.



urlpatterns = [
    path('admin/', admin.site.urls),
    полный адрес указывать не нужно, достаточно прописать news/ или test/
    path('news/', index),  # Обратите внимание, что тут прописывается функция index без вызова ().
    path('test/', test)
]



Вторым параметром у нас может идти не только функция, но и список вложенных маршрутов. Сейчас выше у нас всего
написано 2 адреса. Однако, со временем этих адресов может стать очень много. И помещать весь список адресов в
один список urlpatterns - это не самая хорошая практика. Кроме того, так мы нарушаем принцип Джанго, который 
советует создавать приложения как можно менее связанными. В данном случае, если у нас будет приложения news, 
а список адресов будет храниться вне этого приложения (в пакете конфигураций), то при копировании этого 
приложения news в другой проект, нам придется еще и переносить маршруты в новый проект. Чтобы этого не было, 
все маршруты мы можем хранить в намем приложении. И достигается это путем импорта этих маршрутов. Для этого нам 
нужно еще из модуля <urls> импортировать еще функцию include.
И тут вторым параметром для news мы будем передавать не функцию, которую необходимо вызвать, а список вложенных 
маршрутов, который необходимо включить (импортировать). Здесь мы передаем его в виде аргумента функции include, 
в виде строки. Пишем как аргумент <название нашего приложения><точка><файл urls без расширения py>. Этого файла 
<файл urls без расширения py> у нас по умолчанию нет, нам его нужно создать в нашем приложении.
Итак, это 2й вариант, с использованием include.



Итак. Когда маршрутизатор в адресной строке встречает 'news/', он встречает это и для такого адреса
http://127.0.0.1:8000/news/test/, и для такого адреса http://127.0.0.1:8000/news/. При этом он отбрасывает такие 
адреса: 'news/' и 'news/test/'. Поэтому для 'news/' у нас получается '', а для 'news/test' у нас получается 'test/'.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA__ROOT)
