from django.urls import path

from home.views import(
    index_view
)

urlpatterns = [
    path(route='', view=index_view, name='index'),
]