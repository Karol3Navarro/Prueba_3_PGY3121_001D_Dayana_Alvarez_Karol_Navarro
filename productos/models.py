from django.db import models

# Create your models here. popsipatitas
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)

class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(null=False)
    imagen = models.ImageField(upload_to='producto', null=False)
    cantidad = models.IntegerField(null=False)
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.precio)+" "+str(self.imagen)+" "+str(self.cantidad)+" "+str(self.id_categoria)+" "+str(self.activo)

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    usuario = models.CharField(max_length=100)
    comprado = models.BooleanField(default=False)

    def subtotal(self):
        return self.producto.precio * self.cantidad
    def imagen_producto(self):
        return self.producto.imagen.url
