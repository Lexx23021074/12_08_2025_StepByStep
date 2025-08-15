from django.shortcuts import render
# Імпортуємо клас HttpResponse з модуля django.http.
# HttpResponse дозволяє нам повернути просту текстову відповідь
# у вигляді HTML-коду, без використання HTML-шаблонів.
from django.http import HttpResponse
# Визначаємо функцію відображення (view).
# Вона називається 'home', тому що вона відповідає за відображення
# головної сторінки (домашньої).
# Кожна функція відображення має приймати аргумент 'request',
# який є об'єктом, що містить інформацію про поточний веб-запит
def home(request):
   return render(request, 'shop/home.html')
   ''' Цей рядок вказує Django, що він має завантажити та відобразити шаблон home.html з папки shop.
   Django автоматично шукатиме цей файл у папці templates нашого додатку.'''
