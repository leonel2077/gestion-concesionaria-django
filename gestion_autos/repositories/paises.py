from gestion_autos.models import Pais

class PaisRepository:
    def get_all(self):
        return Pais.objects.all()

    def get_by_id(self, id):
        return Pais.objects.get(id=id)
