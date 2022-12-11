from distutils.command.upload import upload
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from ckeditor.fields import RichTextField

class Inmueble(models.Model):
    id=models.AutoField(blank=False, primary_key=True)
    titulo=models.CharField(blank=False, max_length=50, default="")
    subtitulo=models.CharField(blank=False, max_length=50, default="")
    localidad=models.CharField(blank=False, max_length=50, default="")
    provincia=models.CharField(blank=False, max_length=50, default="")
    direccion=models.CharField(blank=False, max_length=100, default="")
    num_viviendas=models.CharField(blank=False, max_length=100, default="")
    fecha_entrega=models.CharField(blank=False, max_length=50, default="")
    dormitorios=models.TextField(blank=False, max_length=100, default="")
    superficie=models.TextField(blank=False, max_length=100, default="")
    detalles=models.TextField(blank=False, max_length=10000, default="")
    comercializa=models.CharField(blank=False, max_length=100, default="")
    portada=models.ImageField(blank=False, upload_to='portadas', default="")
    #precio=models.DecimalField(blank=False, max_digits=8,decimal_places=2)
    correo=models.CharField(blank=False, max_length=50, default="")
    telefono=models.CharField(blank=False, max_length=50, default="")
    precio=models.CharField(blank=False, max_length=20, default="")
    ventas=models.BooleanField(default=False)
    proximas=models.BooleanField(default=False)
    entregas=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "    Inmueble"

    def __str__(self):
        return f'{self.id, self.titulo, self.subtitulo, self.localidad, self.provincia, self.direccion}'
    #, self.titulo, self.subtitulo, self.localidad, self.provincia, self.direccion, self.num_viviendas, self.fecha_entrega, self.dormitorios, self.superficie, self.detalles, self.comercializa, self.precio, self.ventas, self.proximas, self.entregas

@receiver(pre_delete, sender=Inmueble)
def mymodel_delete(sender, instance, **kwargs):
    instance.portada.delete(False)

class Imagene(models.Model):
    imagen1=models.ImageField(upload_to='detalles')  
    imagen2=models.ImageField(upload_to='detalles')
    imagen3=models.ImageField(upload_to='detalles')
    imagen4=models.ImageField(upload_to='detalles')
    imagen5=models.ImageField(upload_to='detalles')
    imagen6=models.ImageField(upload_to='detalles')
    inmueble=models.ForeignKey(Inmueble, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = "   Imagenes"

    def __str__(self):
        return f'{self.imagen1, self.imagen2, self.imagen3, self.imagen4, self.imagen5, self.imagen6}'

@receiver(pre_delete, sender=Imagene)
def mymodel_delete(sender, instance, **kwargs):
    instance.imagen1.delete(False)
    instance.imagen2.delete(False)
    instance.imagen3.delete(False)
    instance.imagen4.delete(False)
    instance.imagen5.delete(False)
    instance.imagen6.delete(False)

class Archivo(models.Model):
    id=models.AutoField(blank=False, primary_key=True)
    archivo1 = models.FileField(blank=True, null=True, upload_to='detalles-archivos')
    archivo2 = models.FileField(blank=True, null=True, upload_to='detalles-archivos')
    archivo3 = models.FileField(blank=True, null=True, upload_to='detalles-archivos')
    archivo4 = models.FileField(blank=True, null=True, upload_to='detalles-archivos')
    archivo5 = models.FileField(blank=True, null=True, upload_to='detalles-archivos')
    inmueble=models.ForeignKey(Inmueble, on_delete=models.CASCADE, null=False, default="")

    class Meta:
        verbose_name_plural = "  Archivos"
    
    def __str__(self):
        return str(self.inmueble.titulo)
    
class Noticia(models.Model):
    id=models.AutoField(blank=False, primary_key=True)
    titulo=models.TextField(blank=False, max_length=200, default="")
    subtitulo=models.TextField(blank=False, max_length=300, default="")
    texto=RichTextField()
    time = models.DateTimeField(auto_now=True) 
    imagen=models.ImageField(upload_to='noticias', default="")
    bibliografia = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = " Noticias"
    
    def __str__(self):
        return self.titulo
