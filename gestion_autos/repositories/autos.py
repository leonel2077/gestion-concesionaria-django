#import logging
from typing import List, Optional
from gestion_autos.models import Auto, ModeloAuto, TipoCombustible, Pais
from gestion_autos.repositories.comentarios import ComentarioRepository
#logger = logging.getLogger(__name__)

comentarios_repo = ComentarioRepository()

class AutoRepository:

    def get_all(self) -> List[Auto]:
        return Auto.objects.all()

    def filter_by_id(self, id: int) -> Optional[Auto]:
        return Auto.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Auto]:
        try:
            auto = Auto.objects.get(id=id)
        except:
            auto = None
        return auto

    def get_auto_on_price_range(
        self,
        min_price: float,
        max_price: float,
    ) -> List[Auto]:
        autos = Auto.objects.filter(
            price__range=(min_price, max_price)
        )

        return autos

    def create(
        self,
        año_fabricacion: int,
        cantidad_puertas: int,
        cilindrada: float,
        precio_dolares: float,
        pais_fabricacion: Optional[Pais] = None,
        modelo: Optional[ModeloAuto] = None,
        tipo_combustible: Optional[TipoCombustible] = None,
    ) -> Auto:
        return Auto.objects.create(
            modelo=modelo,
            año_fabricacion=año_fabricacion,
            cantidad_puertas=cantidad_puertas,
            cilindrada=cilindrada,
            tipo_combustible=tipo_combustible,
            pais_fabricacion=pais_fabricacion,
            precio_dolares=precio_dolares,
        )
 
    def delete(self, auto: Auto):
        return auto.delete()

    def update(
        self,
        auto: Auto,
        año_fabricacion = float,
        cantidad_puertas = float,
        cilindrada = float,
        precio_dolares = float,
        pais_fabricacion: Optional[Pais] = None,
        modelo: Optional[ModeloAuto] = None,
        tipo_combustible: Optional[TipoCombustible] = None,
        ) -> Auto:
        auto.modelo = modelo
        auto.año_fabricacion = año_fabricacion
        auto.cantidad_puertas = cantidad_puertas
        auto.cilindrada = cilindrada
        auto.tipo_combustible = tipo_combustible
        auto.pais_fabricacion = pais_fabricacion
        auto.precio_dolares = precio_dolares
        auto.save()

    def get_comments(self, id):
        all_comentarios = comentarios_repo.get_all()
        comentarios = []
        for comentario in all_comentarios:
            if comentario.auto.id == id:
                comentarios.append(comentario)
        return comentarios

'''
 def filter_by_category(
     self,
     categoria: Category,
 ) -> List[Auto]:
     return Auto.objects.filter(category=categoria
 def filter_by_category_name(
     self,
     nombre_categoria: str,
 ) -> List[Auto]:
     return Auto.objects.filter(
         category__name=nombre_categoria
     )
 '''