# Generated by Django 5.0.7 on 2024-08-08 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_autos', '0005_alter_auto_pais_fabricacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='pais_fabricacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_autos.pais'),
        ),
    ]
