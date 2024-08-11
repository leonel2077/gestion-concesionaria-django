from .repositories.autos import AutoRepository
from .repositories.marcas import MarcaRepository

def total_autos(request):
    repo = AutoRepository()
    total = repo.get_all().count()
    return {'total_autos': total}

def all_marcas(request):
    repo = MarcaRepository()
    marcas = repo.get_all()
    return {'all_marcas': marcas}