# Generated by Django 4.0.3 on 2022-08-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupoInmoApp', '0002_rename_imaganes_imagene_inmueble_subtitulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='localidad',
            field=models.CharField(default='inmueble', max_length=50),
        ),
    ]
