from django.db import models
from django.contrib.auth.models import User

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoCombustible(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

class ModeloAuto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.marca} {self.nombre}'
    
class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'

class Auto(models.Model):
    modelo = models.ForeignKey(ModeloAuto, on_delete=models.CASCADE)
    año_fabricacion = models.IntegerField()
    cantidad_puertas = models.IntegerField()
    cilindrada = models.FloatField()
    tipo_combustible = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    pais_fabricacion = models.ForeignKey(Pais, on_delete=models.CASCADE)
    precio_dolares = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.modelo} ({self.año_fabricacion})'
    
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de: {self.usuario.username} sobre: {self.auto.modelo}'

class ImagenAuto(models.Model):
    auto = models.ForeignKey(
        Auto,
        on_delete=models.CASCADE,
        related_name='Auto',
        verbose_name='Autos',
    )
    image = models.ImageField(upload_to='imagenes_autos/', null=True)

    class Meta:
            verbose_name = "Imagen"
            verbose_name_plural = "Imagenes"
