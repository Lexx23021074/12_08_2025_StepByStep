from django.shortcuts import render, get_object_or_404
from .models import Category, Product 

# View для відображення списку товарів
# Вона може приймати необов'язковий параметр category_slug для фільтрації
def product_list(request, category_slug=None):
    # Спочатку отримуємо всі категорії, щоб відобразити їх на боковій панелі
    categories = Category.objects.all()

    # Визначаємо початковий запит для товарів: спочатку всі доступні товари
    products = Product.objects.filter(available=True)

    # Створюємо змінну для поточної категорії
    current_category = None

    # Якщо в URL-адресі є slug категорії
    if category_slug:
        # get_object_or_404 - це допоміжна функція Django, яка намагається отримати
        # об'єкт (у цьому випадку - категорію) за slug.
        # Якщо категорія не знайдена, поверне помилку 404.
        current_category = get_object_or_404(Category, slug=category_slug)
        
        # Фільтруємо товари, щоб відображати лише ті, що належать до поточної категорії
        products = products.filter(category=current_category)
    
    # Формуємо словник context, який буде переданий у шаблон.
    # Шаблон зможе отримати доступ до всіх цих даних.
    context = {
        'current_category': current_category,
        'categories': categories,
        'products': products
    }

    # render - це функція Django, яка поєднує шаблон з даними (context)
    # та повертає готовий HTML-код.
    return render(request, 'shop/product/list.html', context)

# View для відображення деталей конкретного товару
def product_detail(request, id, slug):
    # Отримуємо об'єкт Product за двома параметрами: id та slug.
    # get_object_or_404 гарантує, що якщо товар не знайдено, буде повернута помилка 404.
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    # Передаємо об'єкт товару в шаблон
    context = {
        'product': product
    }
    
    return render(request, 'shop/product/detail.html', context)