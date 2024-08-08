from django import forms

from gestion_autos.models import (
    Auto,
    Marca,
    ModeloAuto,
)

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
            'modelo',
            'año_fabricacion',
            'cantidad_puertas',
            'cilindrada',
            'tipo_combustible',
            'pais_fabricacion',
            'precio_dolares',
        ]
        widgets = {
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'año_fabricacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_puertas': forms.NumberInput(attrs={'class': 'form-control'}),
            'cilindrada': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_combustible': forms.Select(attrs={'class': 'form-control'}),
            'pais_fabricacion': forms.Select(attrs={'class': 'form-control'}),
            'precio_dolares': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = [
            'nombre',
        ]
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ModeloAutoForm(forms.ModelForm):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = ModeloAuto
        fields = [
            'marca',
            'nombre',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
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