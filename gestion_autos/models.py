from django.db import models

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

class Auto(models.Model):
    modelo = models.ForeignKey(ModeloAuto, on_delete=models.CASCADE)
    año_fabricacion = models.IntegerField()
    cantidad_puertas = models.IntegerField()
    cilindrada = models.FloatField()
    tipo_combustible = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    pais_fabricacion = models.CharField(max_length=100)
    precio_dolares = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.modelo} ({self.año_fabricacion})'
