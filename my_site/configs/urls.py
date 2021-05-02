from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news_project.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news_project/', include('news_project.urls'))
]

if settings.DEBUG:  # обращаемся к нашему же модулю settings
    # с помощью функции static пока наш проект еще settings.DEBUG is True,
    # мы будем дозаписывать в urlpatterns медиа данные
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
