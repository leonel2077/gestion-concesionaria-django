from gestion_autos.models import Comentario

class ComentarioRepository:
    def get_all(self):
        return Comentario.objects.all()

    def get_by_id(self, id):
        return Comentario.objects.get(id=id)

    def create(self, auto, usuario, contenido):
        comentario = Comentario.objects.create(
            auto=auto,
            usuario=usuario,
            contenido=contenido
        )
        return comentario

    def update(self, comentario: Comentario, contenido: str):
        comentario.contenido = contenido
        comentario.save()

    def delete(self, comentario: Comentario):
        comentario.delete()
