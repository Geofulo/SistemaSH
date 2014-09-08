from django.db import models
from apps.colores.models import Color

class Modelo(models.Model):
	clave = models.CharField(max_length=25, unique=True)
	nombre = models.CharField(max_length=30)
	fecha = models.DateField(auto_now=True)
	disponible = models.BooleanField(default=True)
	color = models.ManyToManyField(Color, through="Exhibido")
	foto = models.ImageField(upload_to='foto_modelo')
		
	def __unicode__(self):
	 	return self.clave

class Exhibido(models.Model):
	modelo_exhibido = models.ForeignKey(Modelo)	
	color_exhibido = models.ForeignKey(Color)
	exhibido = models.BooleanField(default=True)		

	def __unicode__(self):
		clave  = self.modelo_exhibido.clave
		modelo = self.modelo_exhibido.nombre
		color  = self.color_exhibido.nombre
		exhibido_nombre = clave + " - " + modelo + " - " + color
	 	return exhibido_nombre

