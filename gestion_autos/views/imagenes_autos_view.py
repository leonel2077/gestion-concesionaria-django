from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from gestion_autos.forms import ImagenAutoForm
from gestion_autos.models import ImagenAuto


class ImagenAutoView(View):
    def get(self, request):
        images = ImagenAuto.objects.all()
        return render(
            request,
            'imagenes_autos/list.html',
            dict(
                images=images
            )
        )