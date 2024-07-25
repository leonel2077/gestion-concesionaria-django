import csv
from gestion_autos.models import Marca, TipoCombustible, ModeloAuto, Auto

file_path = 'gestion_autos/vehiculos.csv'

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        marca, _ = Marca.objects.get_or_create(nombre=row['Marca'])
        tipo_combustible, _ = TipoCombustible.objects.get_or_create(tipo=row['Tipo de Combustible'])
        modelo_auto, _ = ModeloAuto.objects.get_or_create(nombre=row['Modelo'], marca=marca)
        
        Auto.objects.create(
            modelo=modelo_auto,
            año_fabricacion=row['Año de Fabricacion'],
            cantidad_puertas=row['Cantidad de Puertas'],
            cilindrada=row['Cilindrada'],
            tipo_combustible=tipo_combustible,
            pais_fabricacion=row['Pais de Fabricacion'],
            precio_dolares=row['Precio en dolares']
        )
