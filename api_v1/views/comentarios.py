from rest_framework import generics
from gestion_autos.models import Comentario
from api_v1.serializers.comentarios_serializer import ComentarioSerializer

class ComentariosPorAutoList(generics.ListAPIView):
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        auto_id = self.kwargs['auto_id']
        return Comentario.objects.filter(auto_id=auto_id)