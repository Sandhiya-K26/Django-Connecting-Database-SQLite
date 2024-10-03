from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # List of products
    path('create/', views.product_create, name='product_create'),  # Create a new product
    path('update/<int:pk>/', views.product_update, name='product_update'),  # Update a product
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),  # Delete a product
]
