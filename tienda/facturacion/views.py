from django.shortcuts import render,HttpResponse

# Create your views here.

def Facturacion(request):
    return render(request, "facturacion/facturacion.html")
