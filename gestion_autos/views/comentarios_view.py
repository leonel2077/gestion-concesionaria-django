from django.views import View
from django.shortcuts import render, redirect
from gestion_autos.forms import ComentarioForm
from gestion_autos.repositories.autos import AutoRepository
from gestion_autos.repositories.comentarios import ComentarioRepository

repo = ComentarioRepository()
repo_auto = AutoRepository()

class ComentarioCreate(View):
    def get(self, request, auto_id):
        form = ComentarioForm()
        auto = repo_auto.get_by_id(id=auto_id)
        return render(
            request,
            'autos/detail.html',
            {
                'auto': auto,
                'form': form,
            }
        )
    
    def post(self, request, auto_id):
        data = request.POST
        auto = repo_auto.get_by_id(id=auto_id)
        usuario = request.user
        contenido = data.get('contenido')

        comentario = repo.create(
            auto=auto,
            usuario=usuario,
            contenido=contenido
        )
        return redirect("auto_detail", comentario.auto.id)
    
class ComentarioUpdate(View):
    def get(self, request, id):
        comentario = repo.get_by_id(id=id)
        if comentario.usuario != request.user:
            return redirect("auto_detail", comentario.auto.id)

        form = ComentarioForm(initial={'contenido': comentario.contenido})

        return render(
            request,
            'comentarios/update.html',
            {'form': form, 'comentario': comentario}
        )

    def post(self, request, id):
        comentario = repo.get_by_id(id=id)
        auto = repo_auto.get_by_id(id=comentario.auto.id)
        if comentario.usuario != request.user:
            return redirect("auto_detail", comentario.auto.id)

        data = request.POST
        contenido = data.get('contenido')

        comentario = repo.update(
            comentario=comentario,
            contenido=contenido
        )
        return redirect("auto_detail", auto.id)

class ComentarioDelete(View):
    def get(self, request, id):
        comentario = repo.get_by_id(id=id)

        if comentario.usuario != request.user:
            return redirect("auto_detail", comentario.auto.id)

        repo.delete(comentario=comentario)
        return redirect("auto_detail", comentario.auto.id)

