from django.conf.urls import patterns, url
#from django.conf.urls import include
from .views import ConsultarModelos, ConsultarExhibidos
from .views import AgregarModelo
from .views import EditarModelo
from .views import eliminar_modelo
from .views import agregar_exhibido
from .views import eliminar_exhibido
#from .views import agregar_modelo

urlpatterns = patterns('',
	url(r'^$' , ConsultarModelos.as_view(), name='consultar_modelos'),
	url(r'^exhibidos/$' , ConsultarExhibidos.as_view(), name="consultar_exhibidos"),
	#url(r'^nuevo/$' , agregar_modelo, name='agregar_modelo'),
	url(r'^nuevo/$' , AgregarModelo.as_view(), name='agregar_modelo'),	
	url(r'^editar/(?P<clave_modelo>\d+)/$' , EditarModelo.as_view(), name='editar_modelo'),
	url(r'^eliminar/(?P<clave_modelo>\d+)/$' , eliminar_modelo, name='eliminar_modelo'),	
	url(r'^exhibir/(?P<clave_modelo>\d+)/(?P<clave_color>\d+)/$' , agregar_exhibido, name='agregar_exhibido'),	
	url(r'^noexhibir/(?P<clave_modelo>\d+)/(?P<clave_color>\d+)/$' , eliminar_exhibido, name='eliminar_exhibido'),	
)