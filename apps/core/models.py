from django.db import models

# Create your models here.


class CategoriaProducto(models.Model):
	
	categoria = models.CharField(max_length=45L, db_column='Categoria', blank=True) # Field name made lowercase.
	
	
	class Meta:
		db_table = 'categoria_producto'

class Producto(models.Model):
	
	categoria_producto = models.ForeignKey(CategoriaProducto, db_column='categoria_producto') # Field name made lowercase.
	codigo = models.CharField(max_length=45L, blank=True)
	descripcion = models.CharField(max_length=45L, blank=True)
	
	
	class Meta:
		db_table = 'producto'

class Sucursal(models.Model):
	
	nombre = models.CharField(max_length=150L, blank=True)
	estado = models.CharField(max_length=100L, blank=True)
	pais = models.CharField(max_length=50L, blank=True)
	tel = models.CharField(max_length=50L, blank=True)
	almacen_admipaq = models.CharField(max_length=100L, blank=True)
	concepto_admipaq = models.CharField(max_length=100L, blank=True)
	iva = models.CharField(max_length=50L, blank=True)
	direccion = models.CharField(max_length=100L, blank=True)
	num_int = models.CharField(max_length=50L, blank=True)
	num_ext = models.CharField(max_length=45L, blank=True)
	folio_sucursal = models.CharField(max_length=50L, blank=True)
	descuento = models.CharField(max_length=10L, blank=True)
	hora_entrada = models.DateTimeField( db_column = "hora_entrada", blank = True , null = True )
	zona_horario = models.IntegerField(default=0)
	
	
	class Meta:
		db_table = 'sucursal'

class Kardex(models.Model):
	
	fecha = models.DateTimeField( auto_now_add = True, db_column = "fecha" )
	folio = models.IntegerField()
	sucursal = models.ForeignKey(Sucursal, db_column='sucursal') # Field name made lowercase.
	tipo_registro = models.CharField(max_length=45L)
	inventario_inicial = models.IntegerField() 
	entradas = models.IntegerField()
	salidas = models.IntegerField() 
	existencia = models.IntegerField()
	descripcion = models.TextField()
	producto = models.ForeignKey(Producto, db_column='producto') # Field name made lowercase.                                                                       


	class Meta:
		db_table = 'kardex'
