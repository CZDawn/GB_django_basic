from django.shortcuts import render
from mainapp.models import Product, Contact

def main(request):
    title = 'Главная'
    content = {'title': title}
    return render(request, 'mainapp/index.html', content)

def products(request):
    title = 'Продукты'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/products.html', content)

def contact(request):
    title = 'Контакты'
    contacts = Contact.objects.all()
    content = {'title': title, 'contacts': contacts}
    return render(request, 'mainapp/contact.html', content)

