from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    context={}
    return render (request, 'productos/index.html', context)

def nuevos_prod(request):
    producto = Producto.objects.all()
    context={'producto':producto}
    return render(request,'productos/nuevos_prod.html', context)
def adopta(request):
    context={}
    return render (request, 'productos/adopta.html', context)
def registro(request):
    context={}
    return render (request, 'productos/registro.html', context)
def nosotros(request):
    context={}
    return render (request, 'productos/nosotros.html', context)
def bandana(request):
    context={}
    return render (request, 'productos/bandana.html', context)
def correa(request):
    context={}
    return render (request, 'productos/correa.html', context)
def identificacion(request):
    context={}
    return render (request, 'productos/identificacion.html', context)
def contacto(request):
    context={}
    return render (request, 'productos/contacto.html', context)
def carrito(request):
    context={}
    return render (request, 'productos/carrito.html', context)
def socio(request):
    context={}
    return render (request, 'productos/socio.html', context)

