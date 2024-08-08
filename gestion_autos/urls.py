from django.urls import path

from gestion_autos.views.autos_view import (
    AutoCreate,
    AutoView,
    AutoUpdate,
    AutoDelete,
    AutoDetail
)

from gestion_autos.views.marcas_view import (
    MarcaCreate,
    MarcaUpdate,
    MarcaDelete,
    MarcaList,
)

urlpatterns = [
    path(route='', view=AutoView.as_view(), name='auto_list'),
    path(route='create/',view=AutoCreate.as_view(), name='auto_create'),
    path(route='<int:id>/',view=AutoDetail.as_view(),name="auto_detail"),
    path(route='<int:id>/update/',view=AutoUpdate.as_view(),name="auto_update"),
    path(route='<int:id>/delete/',view=AutoDelete.as_view(),name="auto_delete"),

    path(route='marcas/', view=MarcaList.as_view(), name='marca_list'),
    path(route='marcas/create/', view=MarcaCreate.as_view(), name='marca_create'),
    path(route='marcas/<int:id>/update', view=MarcaUpdate.as_view(), name='marca_update'),
    path(route='marcas/<int:id>/delete', view=MarcaDelete.as_view(), name='marca_delete'),
]
