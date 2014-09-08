from django.db import models
#from apps.modelos.models import Modelo

class Color(models.Model):
	nombre = models.CharField(max_length=15, unique=True)
	exacolor = models.CharField(max_length=8, unique=True)
	#modelo_color = models.ManyToManyField('Modelo', through='Exhibido', related_name='modelos')

	def __unicode__(self):
		return self.nombre
