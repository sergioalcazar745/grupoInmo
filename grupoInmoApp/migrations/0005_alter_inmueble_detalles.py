# Generated by Django 4.0.3 on 2022-08-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupoInmoApp', '0004_alter_inmueble_comercializa_alter_inmueble_detalles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='detalles',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
