from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product, Category


def base(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/base.html', context)


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'catalog/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)