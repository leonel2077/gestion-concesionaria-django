from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from gestion_autos.admin import is_admin
from gestion_autos.repositories.marcas import MarcaRepository
from gestion_autos.forms import MarcaForm

repo = MarcaRepository()

@method_decorator(user_passes_test(is_admin), name='dispatch')
class MarcaCreate(View):
    def get(self, request):
        form = MarcaForm()
        return render(
            request, 
            'marcas/create.html',
            {'form': form}
        )
    
    def post(self, request):
        data = request.POST
        nombre = data.get('nombre')

        repo.create(
            nombre=nombre
        )
        return redirect("marca_list")

@method_decorator(user_passes_test(is_admin), name='dispatch')
class MarcaList(View):
    def get(self, request):
        marcas = repo.get_all()
        return render(
            request, 
            'marcas/list.html', 
            {'marcas': marcas}
        )
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class MarcaUpdate(View):
    def get(self, request, id):
        marca = repo.get_by_id(id=id)

        return render(
            request,
            "marcas/update.html",
            {'marca': marca}
        )
    
    def post(self, request, id):
        marca = repo.get_by_id(id=id)
        data = request.POST
        nombre = data.get('nombre')
        repo.update(marca=marca, nombre=nombre)
        return redirect('marca_list')

@method_decorator(user_passes_test(is_admin), name='dispatch')
class MarcaDelete(View):
    def get(self, request, id):
        marca = repo.get_by_id(id=id)
        repo.delete(marca=marca)
        return redirect('marca_list')

