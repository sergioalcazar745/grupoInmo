# Generated by Django 4.0.3 on 2022-09-13 12:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupoInmoApp', '0014_archivo_inmueble'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='titular',
        ),
        migrations.AddField(
            model_name='noticia',
            name='subtitulo',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='texto',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
