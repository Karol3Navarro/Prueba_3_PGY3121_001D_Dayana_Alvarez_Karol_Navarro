from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Producto, Categoria, ItemCarrito
from .carrito import Carrito
from .forms import CategoriaForm

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
def contacto(request):
    context={}
    return render (request, 'productos/contacto.html', context)

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
        imagen=request.FILES["imagen"]
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
        imagen=request.FILES["imagen"]
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

def crud_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias':categorias}
    return render(request, 'productos/categorias_list.html', context)

def categoriasAdd(request):
    context={}
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            form=CategoriaForm()
            context={'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, 'productos/categorias_add.html', context)
    else:
        form = CategoriaForm()
        context={'form':form}
        return render(request, 'productos/categorias_add.html', context)

def categorias_del(request,pk):
    mensajes = []
    errores = []
    categorias = Categoria.objects.all()
    try:
        categoria= Categoria.objects.get(id_categoria=pk)

        context={}
        if categoria:
            categoria.delete()
            mensajes.append=("Bien, datos eliminados...")
            context={'categorias':categorias, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'productos/categorias_list.html', context)
    except:
        mensaje="Error, id no existe..."
        categorias = Categoria.objects.all()
        context={'mensaje':mensaje, 'categorias':categorias}
        return render(request, 'productos/categorias_list.html',context)

def categorias_edit(request, pk):
    try:
        categoria= Categoria.objects.get(id_categoria=pk)
        context={}
        if categoria:
            if request.method == "POST":
                form =CategoriaForm(request.POST, instance=categoria)
                form.save()
                mensaje = "Bien, datos actualizados..."
                print(mensaje)
                context={'categoria':categoria, 'form':form, 'mensaje': mensaje}
                return render(request, 'productos/categorias_edit.html', context)
            else:
                form =CategoriaForm(instance=categoria)
                mensaje=""
                context={'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request, 'productos/categorias_edit.html', context)
    except:
        categorias= Categoria.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'categorias': categorias}
        return render(request, 'productos/categorias_list.html', context)
    
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        carrito = Carrito(request)
        carrito.agregar(producto=producto, cantidad=cantidad)
        return redirect('nuevos_prod')

    return render(request, 'productos/agregar_al_carrito.html', {'producto': producto})

def ver_carrito(request):
    carrito = Carrito(request)
    items = carrito.get_items()
    total = carrito.get_total()
    return render(request, 'productos/ver_carrito.html', {'items': items, 'total': total})

def eliminar_del_carrito(request, item_id):
    carrito = Carrito(request)
    item = get_object_or_404(ItemCarrito, id=item_id)
    carrito.eliminar(item)
    return redirect('ver_carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('ver_carrito')
def ingresar_datos(request):
    return render(request, 'productos/ingresar_datos.html')
def procesar_datos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        context = {
            'usuario': {
                'nombre': nombre,
                'direccion': direccion,
                'telefono': telefono,
            },
            'items': obtener_items_del_carrito(request), 
            'total': calcular_total_del_carrito(request),  
        }
        return render(request, 'productos/checkout.html', context)
def obtener_items_del_carrito(request):
    carrito = Carrito(request)
    items = carrito.get_items()
    return items

def calcular_total_del_carrito(request):
    carrito = Carrito(request)
    total = carrito.get_total()
    return total

def checkout(request):
    carrito = Carrito(request)
    items = carrito.get_items()
    total = carrito.get_total()
    return render(request, 'productos/checkout.html', {'items': items, 'total': total})
def incrementar_cantidad(request, producto_id):
    producto = Producto.objects.get(id_producto=producto_id)
    carrito = Carrito(request)
    carrito.incrementar_cantidad(producto_id)
    return redirect('ver_carrito')

def decrementar_cantidad(request, producto_id):
    producto = Producto.objects.get(id_producto=producto_id)
    carrito = Carrito(request)
    carrito.decrementar_cantidad(producto_id)
    return redirect('ver_carrito')

