# Generated by Django 5.0.7 on 2024-08-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_autos', '0003_alter_auto_pais_fabricacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='pais_fabricacion',
            field=models.CharField(max_length=110),
        ),
    ]
