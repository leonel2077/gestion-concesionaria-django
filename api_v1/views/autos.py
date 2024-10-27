from rest_framework.viewsets import ModelViewSet
from api_v1.serializers.autos_serializer import AutoSerializer
from gestion_autos.models import Auto

class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer