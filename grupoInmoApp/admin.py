from django.contrib import admin

from grupoInmoApp.models import Archivo, Imagene, Inmueble, Noticia

class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'subtitulo', 'provincia', 'direccion', 'fecha_entrega', 'dormitorios', 'comercializa', 'precio', 'ventas', 'proximas', 'entregas')
    # search_fields = ('provincia', 'direccion', 'fecha_entrega')
    # fields = ['id', 'titulo', 'subtitulo', 'provincia', 'direccion', 'num_viviendas', 'fecha_entrega', 'dormitorios', 'superficie', 'detalles', 'comercializa', 'precio', 'ventas', 'proximas', 'entregas']
    pass   
admin.site.register(Inmueble, InmuebleAdmin)

class ImagenesAdmin(admin.ModelAdmin):
      list_display = ('id', 'imagen1')
admin.site.register(Imagene, ImagenesAdmin)

class ArchivoAdmin(admin.ModelAdmin):
      list_display = ('id', 'archivo1')
admin.site.register(Archivo, ArchivoAdmin)

class NoticiaAdmin(admin.ModelAdmin):
      pass
admin.site.register(Noticia, NoticiaAdmin)
