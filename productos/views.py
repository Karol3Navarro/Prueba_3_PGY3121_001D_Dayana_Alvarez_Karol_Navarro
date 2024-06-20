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
