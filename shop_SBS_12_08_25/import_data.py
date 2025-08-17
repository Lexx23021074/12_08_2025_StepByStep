import os
import django
import json
import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_SBS_12_08_25.settings')
django.setup()

from products.models import Category, Product

# Завантажуємо дані з JSON-файлу
with open('products_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for category_data in data:
    category_name = category_data['category']
    # Створюємо slug для категорії
    category_slug = slugify.slugify(category_name)
    # Отримуємо або створюємо категорію
    category, created = Category.objects.get_or_create(
        name=category_name,
        slug=category_slug
    )
    print(f"Категорія '{category.name}' {'створена' if created else 'вже існує'}.")
    
    for product_data in category_data['products']:
        product_name = product_data['name']
        product_slug = slugify.slugify(product_name)
        
        # Перевіряємо, чи існує товар
        if not Product.objects.filter(slug=product_slug).exists():
            Product.objects.create(
                category=category,
                name=product_name,
                slug=product_slug,
                description=product_data['description'],
                price=product_data['price'],
                image=product_data['image']
            )
            print(f"   Товар '{product_name}' додано.")
        else:
            print(f"   Товар '{product_name}' вже існує.")

print("\nЗавантаження даних завершено!")