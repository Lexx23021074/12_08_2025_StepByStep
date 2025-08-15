"""
URL configuration for shop_SBS_12_08_25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin # Імпортуємо модуль для доступу до панелі адміністратора
from django.urls import path, include # Імпортуємо path для маршрутів і include для включення маршрутів інших додатків

urlpatterns = [ # Список, що містить усі маршрути нашого проекту
    path('admin/', admin.site.urls), # path('admin/') означає, що запити на URL-адресу '/admin/' будуть оброблятися панеллю адміністратора Django
    path('', include('shop.urls')), # path('') означає, що запити на головну сторінку будуть перенаправлені до файлу urls.py нашого додатку shop
]
