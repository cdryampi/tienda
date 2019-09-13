from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.

def Productos(request):
    productos = Product.objects.all()
    return render(request,"productos/productos.html",{'productos':productos})