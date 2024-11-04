# Crear cliente si el usuario es STAFF
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api_v1.serializers.clientes_serializer import ClienteSerializer

class CrearClienteView(APIView):
    """
    post:
    Crea un nuevo cliente en el sistema. Solo accesible para usuarios STAFF.
    """
    def post(self, request):
        if not request.user.is_staff:
            return Response({'error': 'No tiene permisos para crear clientes'}, status=status.HTTP_403_FORBIDDEN)

        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)