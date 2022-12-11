# Generated by Django 4.0.3 on 2022-08-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupoInmoApp', '0003_inmueble_localidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='comercializa',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='detalles',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='direccion',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='dormitorios',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='localidad',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='num_viviendas',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='provincia',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='subtitulo',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='superficie',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='titulo',
            field=models.CharField(default='', max_length=50),
        ),
    ]
