from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from gestion_autos.views.autos_view import is_admin
from django.utils.decorators import method_decorator

from gestion_autos.views.autos_view import (
    AutoCreate,
    AutoView,
    AutoUpdate,
    AutoDelete,
    AutoDetail,
)

from gestion_autos.views.marcas_view import (
    MarcaCreate,
    MarcaUpdate,
    MarcaDelete,
    MarcaList,
)

from gestion_autos.views.modelos_view import (
    ModeloAutoCreate,
    ModeloAutoUpdate,
    ModeloAutoDelete,
    ModeloAutoList,
)

from gestion_autos.views.comentarios_view import (
    ComentarioCreate,
    ComentarioUpdate,
    ComentarioDelete,
)

from gestion_autos.views.imagenes_autos_view import (ImagenAutoView)

urlpatterns = [
    path(route='', view=AutoView.as_view(), name='auto_list'),
    path(route='create/',view=AutoCreate.as_view(), name='auto_create'),
    path(route='<int:id>/',view=AutoDetail.as_view(),name="auto_detail"),
    path(route='<int:id>/update/',view=AutoUpdate.as_view(),name="auto_update"),
    path(route='<int:id>/delete/',view=AutoDelete.as_view(),name="auto_delete"),

    path(route='marcas/', view=method_decorator(user_passes_test(is_admin))(MarcaList.as_view()), name='marca_list'),
    path(route='marcas/create/', view=method_decorator(user_passes_test(is_admin))(MarcaCreate.as_view()), name='marca_create'),
    path(route='marcas/<int:id>/update', view=method_decorator(user_passes_test(is_admin))(MarcaUpdate.as_view()), name='marca_update'),
    path(route='marcas/<int:id>/delete', view=method_decorator(user_passes_test(is_admin))(MarcaDelete.as_view()), name='marca_delete'),

    path(route='modelos/', view=method_decorator(user_passes_test(is_admin))(ModeloAutoList.as_view()), name='modelo_list'),
    path(route='modelos/create/', view=method_decorator(user_passes_test(is_admin))(ModeloAutoCreate.as_view()), name='modelo_create'),
    path(route='modelos/<int:id>/update', view=method_decorator(user_passes_test(is_admin))(ModeloAutoUpdate.as_view()), name='modelo_update'),
    path(route='modelos/<int:id>/delete', view=method_decorator(user_passes_test(is_admin))(ModeloAutoDelete.as_view()), name='modelo_delete'),
    
    path(route='comentarios/create/<int:auto_id>', view=ComentarioCreate.as_view(), name='comentario_create'),
    path(route='comentarios/edit/<int:id>', view=ComentarioUpdate.as_view(), name='comentario_edit'),
    path(route='comentarios/delete/<int:id>', view=ComentarioDelete.as_view(), name='comentario_delete'),

    path(route='imagenes_autos/', view=ImagenAutoView.as_view(), name='imagenes_autos'),
]
