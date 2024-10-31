from rest_framework import generics
from gestion_autos.models import Auto, Marca, ModeloAuto
from django.contrib.auth.models import User
from api_v1.serializers.autos_serializer import AutoSerializer
from api_v1.serializers.autos_serializer import ModeloAutoSerializer
from api_v1.serializers.autos_serializer import MarcaSerializer
from api_v1.serializers.users_serializer import UserSerializer

class AutoListView(generics.ListAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class ModeloAutoListView(generics.ListAPIView):
    queryset = ModeloAuto.objects.all()
    serializer_class = ModeloAutoSerializer

class MarcaListView(generics.ListAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
