from django.db import models
from django.urls import reverse

# Модель для категорії товарів.
# Вона буде використовуватися для групування продуктів.
class Category(models.Model):
    # 'name' - це назва категорії, наприклад, 'Електроніка' або 'Одяг'.
    # db_index=True створює індекс в базі даних, що прискорює пошук за цим полем.
    name=models.CharField(max_length=200, db_index=True)
    # 'slug' - це коротка мітка для URL, яка складається тільки з букв, цифр,
    # дефісів та підкреслень. unique=True гарантує, що slug буде унікальним.
    # Наприклад, для 'Електроніка' slug буде 'elektronika'.
    slug = models.SlugField(max_length=200, unique = True)

    class Meta:
        # ordering=('name',) - сортує категорії за назвою в алфавітному порядку.
        ordering = ('name',)

        # verbose_name - це назва моделі в однині, як вона буде відображатися в адмін-панелі.
        verbose_name = 'category'

        # verbose_name_plural - це назва моделі в множині.
        verbose_name_plural = 'categories'
    # Метод __str__ повертає рядкове представлення об'єкта.
    # Він використовується в адмін-панелі та інших місцях для відображення назви об'єкта.
    def __str__(self):
        return self.name

# Модель для продукту.
# Тут ми описуємо всі характеристики товару.
class Product(models.Model):
    # 'category' - це зовнішній ключ (ForeignKey). Він створює зв'язок
    # "багато-до-одного" (many-to-one), де багато продуктів належать до однієї категорії.
    # related_name='products' дозволить легко отримувати список товарів для кожної категорії.
    # on_delete=models.CASCADE означає, що якщо категорія буде видалена, то всі
    # пов'язані з нею продукти також будуть видалені.
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    # 'name' - назва товару.
    name=models.CharField(max_length=200, db_index=True)

    # 'slug' - унікальна мітка для URL товару.
    slug=models.SlugField(max_length=200, db_index=True)

    # 'image' - поле для завантаження зображення.
    # upload_to='products/%Y/%m/%d' вказує, що зображення будуть
    # зберігатися в папці 'media/products/рік/місяць/день/'.
    # blank=True означає, що це поле не є обов'язковим.
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    # 'description' - текстовий опис товару.
    # blank=True дозволяє залишити це поле пустим.
    description = models.TextField(blank=True)

    # 'price' - ціна товару.
    # max_digits=10 означає, що загальна кількість цифр не може перевищувати 10.
    # decimal_places=2 означає, що після коми буде 2 цифри (для копійок)
    price= models.DecimalField(max_digits=10, decimal_places=2)

    # 'available' - логічне поле (True/False), яке вказує, чи є товар в наявності.
    # default=True встановлює значення за замовчуванням.
    available = models.BooleanField(default=True)

    # 'created' - дата і час створення запису товару.
    # auto_now_add=True автоматично встановлює поточну дату і час при створенні об'єкта.
    created = models.DateTimeField(auto_now_add=True)

    # 'updated' - дата і час останнього оновлення товару.
    # auto_now=True автоматично оновлює дату і час при кожному збереженні об'єкта.
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
    ]

    def __str__(self):
        return self.name








