from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length = 100)
	
	def __str__(self):
		return f"{self.nombre}"
		
#producto
class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	precio = models.DecimalField(max_digits=10, decimal_places= 2)
	stock = models.BooleanField(default=True)
	categoria_producto = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
	
	def __str__(self):
		return f"{self.nombre}"
	