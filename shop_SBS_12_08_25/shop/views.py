from django.shortcuts import render
from products.models import Product 

def home(request):
    products = Product.objects.filter(available=True).order_by('-created')[:4]
    return render(request, 'shop/home.html', {'products': products})

# Додайте цю функцію
def product_list(request):
    # Логіка для відображення списку продуктів
    return render(request, 'shop/product/list.html')