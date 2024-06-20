from django.db import models

# Create your models here. popsipatitas
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    catagoria = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.catagoria)

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