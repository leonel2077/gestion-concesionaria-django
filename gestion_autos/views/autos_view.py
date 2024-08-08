from django.shortcuts import (
    render,
    redirect
    )
from gestion_autos.repositories.autos import AutoRepository
from django.views import View
from gestion_autos.forms import AutoForm
#from django.contrib.auth.decorators import login_required

repo = AutoRepository()


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
        modelo = data.get('modelo')
        año_fabricacion = data.get('año_fabricacion')
        cantidad_puertas = data.get('cantidad_puertas')
        cilindrada = data.get('cilindrada')
        tipo_combustible = data.get('tipo_combustible')
        pais_fabricacion = data.get('pais_fabricacion')
        precio_dolares = data.get('precio_dolares')

        auto = repo.create(
            auto=auto,
            modelo=modelo,
            año_fabricacion = año_fabricacion,
            cantidad_puertas = cantidad_puertas,
            cilindrada = cilindrada,
            tipo_combustible = tipo_combustible,
            pais_fabricacion = pais_fabricacion,
            precio_dolares = precio_dolares,
        )
        return redirect("auto_detail" ,auto.id)


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
        auto = repo.get_by_id(id=id)
        
        return render(
            request,
            "autos/update.html",
            {
                'auto': auto
            }
        )
    
    def post(self, request, id):
        auto = repo.get_by_id(id=id)
        data = request.POST

        modelo = data.get('modelo')
        año_fabricacion = data.get('año_fabricacion')
        cantidad_puertas = data.get('cantidad_puertas')
        cilindrada = data.get('cilindrada')
        tipo_combustible = data.get('tipo_combustible')
        pais_fabricacion = data.get('pais_fabricacion')
        precio_dolares = data.get('precio_dolares')
        edited_auto = repo.update(
            auto=auto,
            modelo=modelo,
            año_fabricacion=año_fabricacion,
            cantidad_puertas=cantidad_puertas,
            cilindrada=cilindrada,
            tipo_combustible=tipo_combustible,
            pais_fabricacion=pais_fabricacion,
            precio_dolares=precio_dolares,
        )
        return redirect("auto_detail",edited_auto.id)

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
        return render(
            request,
            'autos/detail.html',
            {"auto":auto}
        )