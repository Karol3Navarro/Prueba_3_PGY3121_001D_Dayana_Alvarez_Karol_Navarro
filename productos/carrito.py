from .models import Producto, ItemCarrito

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def agregar(self, producto, cantidad):
        producto_id = str(producto.id_producto)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {'cantidad': 0, 'precio': str(producto.precio)}
        self.carrito[producto_id]['cantidad'] += cantidad
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, item):
        producto_id = str(item.producto.id_producto)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar_carrito()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True

    def get_items(self):
        productos_ids = self.carrito.keys()
        productos = Producto.objects.filter(id_producto__in=productos_ids)
        carrito = self.carrito.copy()
        for producto in productos:
            carrito[str(producto.id_producto)]['producto'] = producto
        items = []
        for item in carrito.values():
            item_obj = ItemCarrito()
            item_obj.producto = item['producto']
            item_obj.cantidad = item['cantidad']
            item_obj.precio = item['precio']
            items.append(item_obj)
        return items
    def incrementar_cantidad(self, producto_id):
        producto_id = str(producto_id)
        if producto_id in self.carrito:
            self.carrito[producto_id]['cantidad'] += 1
            self.guardar_carrito()

    def decrementar_cantidad(self, producto_id):
        producto_id = str(producto_id)
        if producto_id in self.carrito and self.carrito[producto_id]['cantidad'] > 0:
            self.carrito[producto_id]['cantidad'] -= 1
            if self.carrito[producto_id]['cantidad'] == 0:
                del self.carrito[producto_id]
            self.guardar_carrito()

    def get_total(self):
        return sum(int(item['precio']) * item['cantidad'] for item in self.carrito.values())
   