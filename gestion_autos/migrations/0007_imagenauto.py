# Generated by Django 5.0.7 on 2024-08-09 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_autos', '0006_alter_auto_pais_fabricacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='imagenes_autos/')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Auto', to='gestion_autos.auto', verbose_name='Autos')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
    ]