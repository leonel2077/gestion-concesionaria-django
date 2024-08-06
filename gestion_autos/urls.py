from django.urls import path

from gestion_autos.views.autos_view import *

urlpatterns = [
    path(route='', view=auto_list, name='auto_list'),
    path(route='create/',view=auto_create, name='auto_create'),
    path(route='<int:id>/',view=auto_detail,name="auto_detail"),
    path(route='<int:id>/update/',view=auto_update,name="auto_update"),
    path(route='<int:id>/delete/',view=auto_delete,name="auto_delete")
]
