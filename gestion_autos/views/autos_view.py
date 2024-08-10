from django.shortcuts import (
    render,
    redirect
    )
from gestion_autos.repositories.autos import AutoRepository
from gestion_autos.repositories.modelos import ModeloAutoRepository
from gestion_autos.repositories.combustibles import TipoCombustibleRepository
from gestion_autos.repositories.paises import PaisRepository
from gestion_autos.repositories.comentarios import ComentarioRepository
from django.views import View
from gestion_autos.forms import AutoForm
#from django.contrib.auth.decorators import login_required

repo = AutoRepository()
repo_modelo = ModeloAutoRepository()
repo_tipo_combustible = TipoCombustibleRepository()
repo_pais_fabricacion = PaisRepository()
repo_comentarios = ComentarioRepository()

#@login_required(login_url="/login/")
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
        return redirect("auto_detail", auto.id)


#@login_required(login_url="/login/")
class AutoView(View):
    def get(self, request):
        autos = repo.get_all()
    
        return render(
            request,
            'autos/list.html',
            dict(
                autos=autos
            )
        )

#@login_required(login_url="/login/")
class AutoUpdate(View):
    def get(self, request, id):
        form = AutoForm()
        auto = repo.get_by_id(id=id)
        
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
        return redirect("auto_detail", id)

#@login_required(login_url="/login/")
class AutoDelete(View):
    def get(self, request, id):
        auto = repo.get_by_id(id=id)
        repo.delete(auto=auto)
        return redirect("auto_list")
    
#@login_required(login_url="/login/")
class AutoDetail(View):
    def get(self, request, id):   
        auto = repo.get_by_id(id=id)
        comentarios = repo.get_comments(id=id)
        return render(
            request,
            'autos/detail.html',
            {
                "auto":auto,
                "comentarios":comentarios,
                }
        )