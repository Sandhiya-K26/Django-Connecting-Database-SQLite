from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")  # Success message
            return redirect('product_list')  # Redirect to product list
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form': form})

def product_list(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'read.html', {'products': products})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")  # Success message
            return redirect('product_list')  # Redirect to product list
    else:
        form = ProductForm(instance=product)
    return render(request, 'update.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully!")  # Success message
        return redirect('product_list')  # Redirect to product list
    return render(request, 'delete.html', {'product': product})
