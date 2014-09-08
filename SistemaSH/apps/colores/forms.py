from django import forms
from .models import Color
#from django.forms.fields import DateField


class ColorForm(forms.ModelForm):   

    class Meta:
        model = Color        
#        exclude
        fields = ('nombre', 'exacolor')
        
    def save(self, commit=False):
    	color = super(ColorForm, self).save(commit=True)
    	return color