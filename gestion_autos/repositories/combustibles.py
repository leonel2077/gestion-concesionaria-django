from gestion_autos.models import TipoCombustible

class TipoCombustibleRepository:
    def get_all(self):
        return TipoCombustible.objects.all()

    def get_by_id(self, id):
        return TipoCombustible.objects.get(id=id)
