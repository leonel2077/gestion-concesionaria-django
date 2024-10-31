from rest_framework import serializers
from gestion_autos.models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()

    class Meta:
        model = Comentario
        fields = ['usuario', 'contenido', 'fecha_creacion']
