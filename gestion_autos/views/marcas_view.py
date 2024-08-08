from django.shortcuts import render, redirect
from gestion_autos.repositories.marcas import MarcaRepository
from django.views import View
from gestion_autos.forms import MarcaForm

repo = MarcaRepository()

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
    
class MarcaList(View):
    def get(self, request):
        marcas = repo.get_all()
        return render(
            request, 
            'marcas/list.html', 
            {'marcas': marcas}
        )
    
    
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

class MarcaDelete(View):
    def get(self, request, id):
        marca = repo.get_by_id(id=id)
        repo.delete(marca=marca)
        return redirect('marca_list')

