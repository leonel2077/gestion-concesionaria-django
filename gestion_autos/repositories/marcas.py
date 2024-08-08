from gestion_autos.models import Marca

class MarcaRepository:
    def get_all(self):
        return Marca.objects.all()

    def get_by_id(self, id):
        return Marca.objects.get(id=id)

    def create(self, nombre):
        return Marca.objects.create(nombre=nombre)

    def update(self, marca: Marca, nombre: str):
        marca.nombre = nombre
        marca.save()

    def delete(self, marca: Marca):
        marca.delete()
