from django.shortcuts import render, HttpResponse

# Create your views here.

def Productos(request):
    return render(request,"productos/productos.html")