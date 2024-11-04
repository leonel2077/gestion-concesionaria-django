from rest_framework import generics
from gestion_autos.models import Auto, Marca, ModeloAuto
from django.contrib.auth.models import User
from api_v1.serializers.autos_serializer import AutoSerializer
from api_v1.serializers.autos_serializer import ModeloAutoSerializer
from api_v1.serializers.autos_serializer import MarcaSerializer
from api_v1.serializers.users_serializer import UserSerializer

class AutoListView(generics.ListAPIView):
    """
    get:
    Retorna un listado de todos los autos en el sistema.
    """
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class ModeloAutoListView(generics.ListAPIView):
    """
    get:
    Retorna un listado de todos los modelos de autos en el sistema.
    """
    queryset = ModeloAuto.objects.all()
    serializer_class = ModeloAutoSerializer

class MarcaListView(generics.ListAPIView):
    """
    get:
    Retorna un listado de todas las marcas de autos en el sistema.
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class UserListView(generics.ListAPIView):
    """
    get:
    Retorna un listado de todos los usuarios en el sistema.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
