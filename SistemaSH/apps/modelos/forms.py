from django import forms
from .models import Modelo
#from django.forms.fields import DateField


class ModeloForm(forms.ModelForm):   
    class Meta:
        model = Modelo

        #exclude
        #fields = ('clave', 'nombre', 'disponible', 'color', 'foto',)
        #widgets = {'clave': forms.TextInput(attrs={'class':'form-control','placeholder':'Clave'}),
        #   'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
        #   'color': forms.CheckboxSelectMultiple(attrs={'name':'color'})}         
        #   'foto': forms.FileInput(attrs={'class':'form-control'})}    

    
    #def save(self, commit=True):
    #    modelo = super(ModeloForm, self).save()
    #     color = self.cleaned_data['color']
    #     Exhibido.objects.create(modelo_exhibido=modelo, color_exhibido=color)
    #    return modelo


    #def clean(self):
        # color_nombre = self.cleaned_data['color']
        # modelo_nombre = self.cleaned_data['nombre']        
        #exhibido.modelo_exhibido = modelo_nombre
        # modelo = modelo_nombre
        # return modelo
        # cleaned_data = super(ModeloForm, self).clean()
        # return cleaned_data

    