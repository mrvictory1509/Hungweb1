from django.shortcuts import render, redirect
from .models import User, Category, Sex, Shoes, Cart, Product, Bill
from django.db.models import F

# Create your views here.
def homepage(request):
    trend = Shoes.objects.all().order_by(F('NumberBuy').desc())[:6]
    categoryID = Category.objects.filter(Name = "Recycling")[0].id
    recycling = Shoes.objects.filter(CategoryID = categoryID)
    shoes = {'trend' : trend, 'recycling': recycling, 'page' : 'index'}
    return render(request, 'index.html', shoes)
def sale(request):
    sale = Shoes.objects.filter(Sales = True)
    shoes = {'sale' : sale, 'page' : 'sale'}
    return render(request, 'index.html', shoes)
def man(request):
    sexID = Sex.objects.filter(Name = "Man")
    man = Shoes.objects.filter(SexID = sexID[0].id)
    shoes = {'man' : man, 'page' : 'man'}
    return render(request, 'index.html', shoes)
def women(request):
    sexID = Sex.objects.filter(Name = "Women")
    women = Shoes.objects.filter(SexID = sexID[0].id)
    shoes = {'women' : women, 'page' : 'women'}
    return render(request, 'index.html', shoes)
def about_us(request):
    shoes = {'page' : 'about_us'}
    return render(request, 'index.html', shoes)
def View(request, id):
    view = Shoes.objects.filter(id = id)
    shoes = {'page' : 'detail_product', 'view' : view}
    return render(request, 'index.html', shoes)
def sign_up(request):
    return render(request, 'sign_up.html')
def sign_in(request):
    return render(request, 'sign_in.html')
