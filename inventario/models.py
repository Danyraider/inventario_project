from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    cantidad_minima = models.IntegerField()
    cantidad_maxima = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)

