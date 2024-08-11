from django.contrib.auth.decorators import user_passes_test
from django.views import View
from django.shortcuts import (
    render,
    redirect
    )
from django.utils.decorators import method_decorator
from gestion_autos.admin import is_admin
from gestion_autos.forms import AutoForm
from gestion_autos.models import ImagenAuto
from gestion_autos.repositories.autos import AutoRepository
from gestion_autos.repositories.modelos import ModeloAutoRepository
from gestion_autos.repositories.combustibles import TipoCombustibleRepository
from gestion_autos.repositories.paises import PaisRepository
from gestion_autos.repositories.comentarios import ComentarioRepository

repo = AutoRepository()
repo_modelo = ModeloAutoRepository()
repo_tipo_combustible = TipoCombustibleRepository()
repo_pais_fabricacion = PaisRepository()
repo_comentarios = ComentarioRepository()

@method_decorator(user_passes_test(is_admin), name='dispatch')
class AutoCreate(View):
    def get(self, request):
        form = AutoForm()

        return render(
            request,
            'autos/create.html',
            {'form':form}
        )
    
    def post(self, request):
        data = request.POST
        modelo_id = data.get('modelo')
        modelo = repo_modelo.get_by_id(id=modelo_id)
        año_fabricacion = data.get('año_fabricacion')
        cantidad_puertas = data.get('cantidad_puertas')
        cilindrada = data.get('cilindrada')
        tipo_combustible_id = data.get('tipo_combustible')
        tipo_combustible = repo_tipo_combustible.get_by_id(id=tipo_combustible_id)
        pais_fabricacion_id = data.get('pais_fabricacion')
        pais_fabricacion = repo_pais_fabricacion.get_by_id(id=pais_fabricacion_id)
        precio_dolares = data.get('precio_dolares')

        auto = repo.create(
            modelo=modelo,
            año_fabricacion = año_fabricacion,
            cantidad_puertas = cantidad_puertas,
            cilindrada = cilindrada,
            tipo_combustible = tipo_combustible,
            pais_fabricacion = pais_fabricacion,
            precio_dolares = precio_dolares,
        )
        imagenes = request.FILES.getlist('imagenes')
        for imagen in imagenes:
            ImagenAuto.objects.create(auto=auto, image=imagen)
        return redirect("auto_detail", auto.id)


class AutoView(View):
    def get(self, request):
        marca_id = request.GET.get('marca_id')
        if marca_id:
            autos = repo.get_by_marca(marca_id=marca_id)
        else:
            autos = repo.get_all()

        return render(
            request,
            'autos/list.html',
            {
                'autos': autos,
                'selected_marca': marca_id
            } 
        )

@method_decorator(user_passes_test(is_admin), name='dispatch')
class AutoUpdate(View):
    def get(self, request, id):
        auto = repo.get_by_id(id=id)

        form = AutoForm(instance=auto)
        
        return render(
            request,
            "autos/update.html",
            {
                'auto': auto,
                'form': form,
            }
        )
    
    def post(self, request, id):
        auto = repo.get_by_id(id=id)
        data = request.POST

        modelo_id = data.get('modelo')
        modelo = repo_modelo.get_by_id(id=modelo_id)
        año_fabricacion = data.get('año_fabricacion')
        cantidad_puertas = data.get('cantidad_puertas')
        cilindrada = data.get('cilindrada')
        tipo_combustible_id = data.get('tipo_combustible')
        tipo_combustible = repo_tipo_combustible.get_by_id(id=tipo_combustible_id)
        pais_fabricacion_id = data.get('pais_fabricacion')
        pais_fabricacion = repo_pais_fabricacion.get_by_id(id=pais_fabricacion_id)
        precio_dolares = data.get('precio_dolares')
        repo.update(
            auto=auto,
            modelo=modelo,
            año_fabricacion=año_fabricacion,
            cantidad_puertas=cantidad_puertas,
            cilindrada=cilindrada,
            tipo_combustible=tipo_combustible,
            pais_fabricacion=pais_fabricacion,
            precio_dolares=precio_dolares,
        )
        imagenes = request.FILES.getlist('imagenes')
        if imagenes:
                ImagenAuto.objects.filter(auto=auto).delete()
                
                for imagen in imagenes:
                    ImagenAuto.objects.create(auto=auto, image=imagen)
        return redirect("auto_detail", id)

class AutoDelete(View):
    def get(self, request, id):
        auto = repo.get_by_id(id=id)
        repo.delete(auto=auto)
        return redirect("auto_list")
    
class AutoDetail(View):
    def get(self, request, id):   
        auto = repo.get_by_id(id=id)
        comentarios = repo.get_comments(id=id)
        imagen = ImagenAuto.objects.filter(auto=auto).first()
        return render(
            request,
            'autos/detail.html',
            {
                "auto":auto,
                "comentarios":comentarios,
                "imagen":imagen,
            }            
        )