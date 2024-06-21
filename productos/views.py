from django.shortcuts import render
from .models import Producto, Categoria

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

def productosAdd(request):
    if request.method != "POST":
        categorias=Categoria.objects.all()
        context={'categorias':categorias}
        return render(request, 'productos/productos_add.html', context)
    else:
        # id_producto=request.POST["id_producto"]
        nombre=request.POST["nombre"]
        precio=request.POST["precio"]
        imagen=request.POST["imagen"]
        cantidad=request.POST["cantidad"]
        categoria=request.POST["categoria"]
        activo="1"

        objCategoria=Categoria.objects.get(id_categoria = categoria)
        obj=Producto.objects.create(  #id_producto=id_producto,
                                    nombre=nombre,
                                    precio=precio,
                                    imagen=imagen,
                                    cantidad=cantidad,
                                    id_categoria=objCategoria,
                                    activo=1  )
        obj.save()
        context={'mensaje':"Ok, producto grabado..."}
        return render(request, 'productos/productos_add.html', context)

def productos_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto=pk)

        producto.delete()
        mensaje="Bien, datos eliminados..."
        productos=Producto.objects.all()
        context={'productos':productos, 'mensaje':mensaje}
        return render(request, 'productos/nuevos_prod.html', context)
    except:
        mensaje="Error, producto no existe..."
        productos=Producto.objects.all()
        context={'productos':productos, 'mensaje':mensaje}
        return render(request, 'productos/nuevos_prod.html',context)

def productos_findEdit(request, pk):
    if pk != "":
        producto=Producto.objects.get(id_producto=pk)
        categorias=Categoria.objects.all()

        # print(type(producto.id_categoria.categoria))

        context={'producto':producto, 'categorias':categorias}
        if producto:
            return render(request, 'productos/productos_edit.html', context)
        else:
            context={'mensaje':'Error, producto no existe...'}
            return render(request, 'productos/nuevos_prod.html', context)

def productosUpdate(request):
    if request.method == "POST":
        id_producto=request.POST["id_producto"]
        nombre=request.POST["nombre"]
        precio=request.POST["precio"]
        imagen=request.POST["imagen"]
        cantidad=request.POST["cantidad"]
        categoria=request.POST["categoria"]
        activo="1"

        objCategoria = Categoria.objects.get(id_categoria = categoria)
        producto = Producto()
        producto.id_producto = id_producto
        producto.nombre = nombre
        producto.precio = precio
        producto.imagen = imagen
        producto.cantidad = cantidad
        producto.id_categoria = objCategoria
        producto.activo = 1
        producto.save()

        categorias= Categoria.objects.all()
        context={'mensaje': "Ok, datos actualizados...", 'categorias':categorias, 'producto':producto}
        return render(request, 'productos/productos_edit.html',context)
    else:
        productos = Producto.objects.all()
        context={'productos':productos}
        return render(request, 'productos/nuevos_prod.html', context)

