from django.views.generic import ListView
from .models import Color
#from django.core.urlresolvers import reverse_lazy

class ConsultarColores(ListView):
	template_name = 'colores/todosColores.html'
	model = Color
	context_object_name = 'colores'

