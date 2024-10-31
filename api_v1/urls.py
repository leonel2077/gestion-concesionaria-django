from rest_framework.routers import DefaultRouter
from django.urls import path
from .views.autos import AutoListView, MarcaListView, UserListView
from .views.comentarios import ComentariosPorAutoList
from .views.clientes import CrearClienteView

router = DefaultRouter()

urlpatterns = [
    path('autos/', AutoListView.as_view(), name='auto-list'),
    path('marcas/', MarcaListView.as_view(), name='marca-list'),
    path('usuarios/', UserListView.as_view(), name='user-list'),
    path('autos/<int:auto_id>/comentarios/', ComentariosPorAutoList.as_view(), name='comentarios-por-auto'),
    path('clientes/crear/', CrearClienteView.as_view(), name='crear-cliente'),
]

urlpatterns += router.urls