from rest_framework import serializers

from gestion_autos.models import Auto, ModeloAuto

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'

    def get_marca(self, value):
        if value.modelo is None:
            return "No tiene marca"
        return value.modelo

    def update(self, instance, validated_data):
        modelo_data = validated_data.pop(
            'modelo', None
        )
        modelo, _= ModeloAuto.objects.get_or_create(
          **modelo_data
        )

        instance.modelo = modelo

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.marca = validated_data.get('marca', instance.marca)
        instance.año_fabricacion = models.IntegerField()
        instance.cantidad_puertas = models.IntegerField()
        instance.cilindrada = models.FloatField()
        instance.tipo_combustible = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
        instance.pais_fabricacion = models.ForeignKey(Pais, on_delete=models.CASCADE)
        instance.precio_dolares = models.DecimalField(max_digits=10, decimal_places=2)

        instance.save()
        return instance