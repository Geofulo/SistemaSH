from django.views.generic import ListView, TemplateView
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
    queryset = Modelo.objects.all().order_by('-fecha', '-clave')
    context_object_name = 'modelos'


class ConsultarExhibidos(ListView):
    #queryset = Modelo.color.through.objects.filter(exhibido=True).values('modelo_exhibido').distinct()    
    #queryset = Modelo.objects.filter(color__in=Exhibido.objects.all(), exhibido=True).annotate()
    #queryset = Exhibido.objects.prefetch_related('modelo_exhibido').all()
    #queryset = Modelo.objects.filter().prefetch_related('color')
    queryset1 = Exhibido.objects.select_related('modelo', 'color').filter(exhibido=True).values_list('modelo_exhibido', flat=True).distinct()
    #model = Model
    queryset = Modelo.objects.filter(id__in = queryset1)
    #queryset = Modelo.objects.filter(id=queryset1)
    context_object_name = 'exhibidos'
    template_name = 'modelos/todosExhibidos.html'

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

class BuscarModelo(TemplateView):        
    def post(self, request):
        buscar = request.POST['buscalo']        
        modelos = Modelo.objects.filter(nombre__contains = buscar)    
        print modelos
        return render(request, 'modelos/todosModelos.html', {'modelos':modelos})    

class FiltrarModelos(ListView):
    model = Modelo
    context_object_name = 'modelos'
    template_name = 'modelos/todosModelos.html'

    def get_queryset(self):
        queryset = super(FiltrarModelos, self).get_queryset()
        clave_filtro = self.kwargs['clave_filtro']        
        if (clave_filtro   == '1'):            
            queryset = Modelo.objects.all().order_by('nombre')
        elif (clave_filtro == '2'):
            queryset = Modelo.objects.all().order_by('-nombre')
        elif (clave_filtro == '3'):
            queryset = Modelo.objects.all().order_by('-fecha', '-clave')
        elif (clave_filtro == '4'):
            queryset = Modelo.objects.all().order_by('fecha')
        elif (clave_filtro == 'existentes'):
            queryset = Modelo.objects.filter(disponible=True).order_by('-fecha', '-clave')
        elif (clave_filtro == 'exhibidos'):
            exhibidos = Exhibido.objects.select_related('modelo', 'color').filter(exhibido=True).values_list('modelo_exhibido', flat=True).distinct()
            queryset = Modelo.objects.filter(id__in = exhibidos).order_by('-fecha', '-clave')
        elif (clave_filtro == 'no_exhibidos'):
            exhibidos = Modelo.color.through.objects.filter(exhibido=False).values('modelo_exhibido').distinct()            
            queryset = Modelo.objects.filter(id__in = exhibidos).order_by('-fecha', '-clave')
        return queryset
        


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

