from django.views.generic import ListView
#from django.views.generic import CreateView, FormView
from django.views.generic.base import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
#from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.forms.models import inlineformset_factory
# from django.template import RequestContext
#from django.http import HttpResponseRedirect
#from django.contrib import messages
from .models import Modelo, Exhibido, Color
from .forms import ModeloForm

class ConsultarModelos(ListView):
    template_name = 'modelos/todosModelos.html'
    model = Modelo
    context_object_name = 'modelos'

class ConsultarExhibidos(ListView):
	template_name = 'modelos/todosExhibidos.html'
	model = Exhibido
	context_object_name = 'exhibidos'

class AgregarModelo(View):
    def get(self, request):
        form = ModeloForm()
        return render(request, "modelos/agregarModelo.html", {'form':form})
    def post(self, request):        
        form = ModeloForm(request.POST, request.FILES)        
        if form.is_valid():            
            modelo = Modelo.objects.create(
                clave      = form.cleaned_data['clave'],
                nombre     = form.cleaned_data['nombre'],
                disponible = form.cleaned_data['disponible'],
                foto       = form.cleaned_data['foto'])
            for color_nombre in form.cleaned_data['color']:
                exhibido = Exhibido(
                    modelo_exhibido = modelo,
                    color_exhibido  = color_nombre,
                    exhibido = False)
                exhibido.save()
            return redirect(reverse('consultar_modelos'))
        else:
            return render(request, "modelos/agregarModelo.html", {'form':form})

class EditarModelo(View):
    def get(self, request, clave_modelo):
        modelo = get_object_or_404(Modelo, pk=clave_modelo)
        form = ModeloForm(instance=modelo)
        return render(request, 'modelos/editarModelo.html', {'form':form})
    def post(self, request, clave_modelo):
        modelo = get_object_or_404(Modelo, pk=clave_modelo)
        form = ModeloForm(request.POST, instance=modelo)
        if form.is_valid():
            modelo.nombre     = form.cleaned_data['nombre']
            modelo.disponible = form.cleaned_data['disponible']
            modelo.foto       = form.cleaned_data['foto']
            modelo.save()            
            old_exhibido = Exhibido.objects.filter(modelo_exhibido=modelo)
            old_exhibido.delete()
            for color_nombre in form.cleaned_data['color']:
                exhibido = Exhibido(
                    modelo_exhibido = modelo,
                    color_exhibido  = color_nombre,
                    exhibido = False)
                exhibido.save()
            return redirect(reverse('consultar_modelos'))
        else:
            return render(request, 'modelos/agregarModelo.html', {'form':form})


def eliminar_modelo(request, clave_modelo):
    modelo = get_object_or_404(Modelo, pk=clave_modelo)
    modelo.delete()
    return redirect(reverse('consultar_modelos'))  

def agregar_exhibido(request, clave_modelo, clave_color):    
    modelo = get_object_or_404(Modelo, pk=clave_modelo)    
    color = get_object_or_404(Color, pk=clave_color)
    exhibido = Exhibido.objects.filter(modelo_exhibido=modelo, color_exhibido=color)    
    exhibido.update(exhibido=True)
    return redirect(reverse('consultar_modelos'))

def eliminar_exhibido(request, clave_modelo, clave_color):
    modelo = get_object_or_404(Modelo, pk=clave_modelo)    
    color = get_object_or_404(Color, pk=clave_color)
    exhibido = Exhibido.objects.filter(modelo_exhibido=modelo, color_exhibido=color)    
    exhibido.update(exhibido=False)
    return redirect(reverse('consultar_modelos'))
    
# def agregar_modelo(request):        
#     if request.method == 'POST': 
#         form = ModeloForm(request.POST, request.FILES)
#         if form.is_valid():
#             modelo = Modelo.objects.create(
#                 clave      = form.cleaned_data['clave'],
#                 nombre     = form.cleaned_data['nombre'],
#                 disponible = form.cleaned_data['disponible'],
#                 foto       = form.cleaned_data['foto'])            
#             for color_nombre in form.cleaned_data['color']:
#                 exhibido = Exhibido(
#                     modelo_exhibido = modelo,
#                     color_exhibido = color_nombre,
#                     exhibido = False)
#                 exhibido.save()
#             return redirect('consultar_modelos')        

#     else:
#     	form = ModeloForm()
#     return render(request, "modelos/agregarModelo.html", {'form':form})

