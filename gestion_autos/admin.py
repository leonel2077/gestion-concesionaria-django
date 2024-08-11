from django.contrib import admin
from django.utils.html import format_html
from .models import Marca, TipoCombustible, ModeloAuto, Auto, Pais, ImagenAuto

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(TipoCombustible)
class TipoCombustibleAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

@admin.register(ModeloAuto)
class ModeloAutoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca',)
    search_fields = ('nombre', 'marca__nombre',)
    list_filter = ('marca',)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    ordering = ('modelo__nombre', 'año_fabricacion',)
    search_fields = ('modelo__nombre', 'año_fabricacion', 'tipo_combustible__tipo',)
    list_filter = ('modelo__marca', 'tipo_combustible', 'pais_fabricacion')
    empty_value_display = 'No disponible'

    list_display = (
        'modelo',
        'año_fabricacion',
        'cantidad_puertas',
        'cilindrada',
        'tipo_combustible',
        'pais_fabricacion',
        'precio_dolares',
        'get_precio_en_colores',
    )

    def get_precio_en_colores(self, obj):
        ALTO = '#FF0000'
        MEDIO = '#FFD700'
        BAJO = '#008F39'
        color = ''

        if obj.precio_dolares > 50000:
            color = ALTO
        elif 20000 <= obj.precio_dolares <= 50000:
            color = MEDIO
        else:
            color = BAJO

        return format_html(
            '<span style="color: {}">${}</span>', color, obj.precio_dolares
        )

    fieldsets = [
        (
            "Información del Auto",
            {
                "fields": ["modelo", "año_fabricacion", "cantidad_puertas", "cilindrada", "tipo_combustible", "pais_fabricacion", "precio_dolares"],
            },
        ),
    ]


@admin.register(ImagenAuto)
class AutoAdmin(admin.ModelAdmin):
    list_display = (
        'auto',
        'image',
    )

def is_admin(user):
    return user.is_staff