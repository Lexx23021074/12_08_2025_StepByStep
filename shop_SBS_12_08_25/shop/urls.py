from django.urls import path
from . import views

app_name = 'shop' # Додайте цей рядок

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
]