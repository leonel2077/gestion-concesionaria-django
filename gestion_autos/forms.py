from django import forms

from gestion_autos.models import (
    Auto,
    Marca,

)

class AutoForm(forms.ModelForm):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    modelo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Auto
        fields = [
            'marca',
            'modelo',
            'año_fabricacion',
            'cantidad_puertas',
            'cilindrada',
            'tipo_combustible',
            'pais_fabricacion',
            'precio_dolares',
        ]
        widgets = {
            'año_fabricacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_puertas': forms.NumberInput(attrs={'class': 'form-control'}),
            'cilindrada': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_combustible': forms.Select(attrs={'class': 'form-control'}),
            'pais_fabricacion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_dolares': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = [
            'nombre'
        ]
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
        }
'''
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = [
            'product',
            'image',
            'description',
        ]
'''