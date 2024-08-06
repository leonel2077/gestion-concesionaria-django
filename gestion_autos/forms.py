from django import forms

from gestion_autos.models import (
    Auto,
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
            'precio_dolares'
        ]
        
        widgets = {
            'modelo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'color: red',
                    }
            ),
            'año_fabricacion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'cantidad_puertas': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'cilindrada': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'tipo_combustible': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'color: red',
                    }
            ),
            'pais_fabricacion': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'color: red',
                    }
            ),
            'precio_dolares': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
            
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