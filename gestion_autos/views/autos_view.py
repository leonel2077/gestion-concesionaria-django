from django.shortcuts import (
    render,
    redirect
    )

from gestion_autos.models import ModeloAuto, TipoCombustible
from gestion_autos.repositories.autos import AutoRepository
#from django.contrib.auth.decorators import login_required
from gestion_autos.forms import AutoForm

repo = AutoRepository()


#@login_required(login_url="/login/")
def auto_list(request):
    autos = repo.get_all()
    return render(
        request,
        'autos/list.html',
        dict(
            autos=autos
        )
    )

#@login_required(login_url="/login/")
def auto_detail(request, id):
    auto = repo.get_by_id(id=id)
    return render(
        request,
        'autos/detail.html',
        {"auto":auto}
    )

#@login_required(login_url="/login/")
def auto_update(request, id):
    auto = repo.get_by_id(id=id)
    if request.method == "POST":
        modelo = request.POST.get('modelo')
        año_fabricacion = request.POST.get('año_fabricacion')
        cantidad_puertas = request.POST.get('cantidad_puertas')
        cilindrada = request.POST.get('cilindrada')
        tipo_combustible = request.POST.get('tipo_combustible')
        pais_fabricacion = request.POST.get('pais_fabricacion')
        precio_dolares = request.POST.get('precio_dolares')

        edited_auto = repo.update(
            auto=auto,
            modelo=modelo,
            año_fabricacion = año_fabricacion,
            cantidad_puertas = cantidad_puertas,
            cilindrada = cilindrada,
            tipo_combustible = tipo_combustible,
            pais_fabricacion = pais_fabricacion,
            precio_dolares = precio_dolares,
        )
        return redirect("auto_detail",edited_auto.id)

    return render(
        request,
        "autos/update.html",
        dict(
            auto = auto
        )
    )

#@login_required(login_url="/login/")
def auto_delete(request, id):
    auto = repo.get_by_id(id=id)
    repo.delete(auto=auto)
    return redirect("auto_list")

#@login_required(login_url="/login/")
def auto_create(request):
    form = AutoForm()
    if request.method == "POST":
        modelo = request.POST.get('modelo')
        año_fabricacion = request.POST.get('año_fabricacion')
        cantidad_puertas = request.POST.get('cantidad_puertas')
        cilindrada = request.POST.get('cilindrada')
        tipo_combustible = request.POST.get('tipo_combustible')
        pais_fabricacion = request.POST.get('pais_fabricacion')
        precio_dolares = request.POST.get('precio_dolares')

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
        return redirect("auto_detail",auto.id)
    
    return render(request, 'autos/create.html', dict(
        form=form
    ))