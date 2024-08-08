from gestion_autos.models import ModeloAuto, Marca

class ModeloAutoRepository:
    def get_all(self):
        return ModeloAuto.objects.all()

    def get_by_id(self, id):
        return ModeloAuto.objects.get(id=id)

    def create(self, nombre, marca_id):
        marca = Marca.objects.get(id=marca_id)
        return ModeloAuto.objects.create(nombre=nombre, marca=marca)

    def update(self, modelo: ModeloAuto, nombre:str, marca_id):
        modelo.nombre = nombre
        modelo.marca = Marca.objects.get(id=marca_id)
        modelo.save()

    def delete(self, modelo: ModeloAuto):
        modelo.delete()
