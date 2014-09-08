from django.conf.urls import patterns, url
#from django.conf.urls import include
from .views import ConsultarColores

urlpatterns = patterns('',
	url(r'^$' , ConsultarColores.as_view(), name="consultar_colores"),
)