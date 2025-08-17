from django.contrib import admin
from .models import Category, Product

# Реєстрація моделі Category в адмін-панелі Django.
# Використання декоратора @admin.register - це сучасний і зручний спосіб.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 'list_display' визначає, які поля моделі будуть відображатися
    # у списку об'єктів у адмін-панелі.
    list_display = ['name', 'slug']

    # 'prepopulated_fields' автоматично заповнює поле 'slug'
    # на основі вмісту поля 'name', як тільки ти його вводиш.
    # Це допомагає створити "чисті" URL-адреси.
    # Помилку виправлено: додано кому після 'name'
    prepopulated_fields = {'slug': ('name',)}

# Реєстрація моделі Product в адмін-панелі.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Помилку виправлено: 'list_display' замість 'list_dispaly'
    # Помилку виправлено: 'available' замість 'avialable'
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']

    # 'list_filter' додає фільтри на бічну панель,
    # що дозволяє легко відфільтрувати товари за наявністю, датою створення тощо.
    # Помилку виправлено: 'available' замість 'avialable'
    list_filter = ['available', 'created', 'updated']

    # 'list_editable' дозволяє редагувати поля прямо зі сторінки списку,
    # без необхідності переходити на сторінку кожного товару
    # Помилку виправлено: 'available' замість 'avialable'
    list_editable = ['price', 'available']

    # 'prepopulated_fields' також автоматично заповнює slug для товару.
    prepopulated_fields = {'slug': ('name',)}
