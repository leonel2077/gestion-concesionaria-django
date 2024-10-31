from rest_framework import serializers
from gestion_autos.models import Auto, ModeloAuto, Marca

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombre']

class ModeloAutoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()  

    class Meta:
        model = ModeloAuto
        fields = ['nombre', 'marca']

class AutoSerializer(serializers.ModelSerializer):
    modelo = ModeloAutoSerializer()  

    class Meta:
        model = Auto
        fields = ['modelo', 'año_fabricacion', 'cantidad_puertas', 'cilindrada', 'tipo_combustible', 'pais_fabricacion', 'precio_dolares']

    def get_marca(self, obj):
        return obj.modelo.marca.nombre if obj.modelo and obj.modelo.marca else "No tiene marca"

    def update(self, instance, validated_data):
        modelo_data = validated_data.pop(
            'modelo', None
        )
        if modelo_data:
            modelo, _ = ModeloAuto.objects.get_or_create(**modelo_data)
            instance.modelo = modelo

        instance.año_fabricacion = validated_data.get('año_fabricacion', instance.año_fabricacion)
        instance.cantidad_puertas = validated_data.get('cantidad_puertas', instance.cantidad_puertas)
        instance.cilindrada = validated_data.get('cilindrada', instance.cilindrada)
        instance.tipo_combustible = validated_data.get('tipo_combustible', instance.tipo_combustible)
        instance.pais_fabricacion = validated_data.get('pais_fabricacion', instance.pais_fabricacion)
        instance.precio_dolares = validated_data.get('precio_dolares', instance.precio_dolares)

        instance.save()
        return instance