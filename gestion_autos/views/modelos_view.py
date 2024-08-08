from django.shortcuts import render, redirect
from gestion_autos.repositories.modelos import ModeloAutoRepository
from django.views import View
from gestion_autos.forms import ModeloAutoForm

repo = ModeloAutoRepository()

class ModeloAutoCreate(View):
    def get(self, request):
        form = ModeloAutoForm()
        return render(
            request, 
            'modelos/create.html',
            {'form': form}
        )

    def post(self, request):
        data = request.POST
        marca = data.get('marca')
        nombre = data.get('nombre')

        repo.create(
            nombre=nombre,
            marca_id=marca,
        )
        return redirect("modelo_list")

class ModeloAutoList(View):
    def get(self, request):
        modelos = repo.get_all()
        return render(
            request,
            'modelos/list.html',
            {'modelos': modelos}
        )
    
class ModeloAutoUpdate(View):
    def get(self, request, id):
        form = ModeloAutoForm()
        modelo = repo.get_by_id(id=id)

        return render(
            request,
            "modelos/update.html",
            {
                'modelo': modelo,
                'form': form
            }
        )
    
    def post(self, request, id):
        modelo = repo.get_by_id(id=id)
        data = request.POST
        nombre = data.get('nombre')
        marca = data.get('marca')
        repo.update(modelo=modelo, nombre=nombre, marca_id=marca)
        return redirect('modelo_list')
    
class ModeloAutoDelete(View):
    def get(self, request, id):
        modelo = repo.get_by_id(id=id)
        repo.delete(modelo=modelo)
        return redirect('modelo_list')


