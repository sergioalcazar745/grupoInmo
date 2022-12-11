from django.conf import settings
from django.shortcuts import render
from grupoInmoApp.forms import FormularioContacto
from django.core.mail import send_mail

from grupoInmoApp.models import Archivo, Imagene, Inmueble, Noticia

def home(request):
    if request.POST:
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():  
            send_mail('Peticion cliente', formulario_contacto.cleaned_data['mensaje'] + "/" + formulario_contacto.cleaned_data ['email'], settings.EMAIL_HOST_USER, ['sergioalcazar745@gmail.com'])
            formulario_contacto=FormularioContacto()    
            return render(request, "home.html", {'nbar': 'home', 'response':'true', 'mensaje':'El correo se ha enviado correctamente','form':formulario_contacto}) 
        else:
            return render(request, "home.html", {'nbar': 'home', 'response':'false', 'mensaje':'El correo no se ha podido enviar', 'form':formulario_contacto})  
    else:
        formulario_contacto=FormularioContacto()       
        return render(request, "home.html", {'nbar': 'home', 'response':'none', 'form':formulario_contacto}) 
    

def ventas(request):
    ventas_list = Inmueble.objects.filter(ventas=True)
    #imagenes_list = Imagene.objects.values('imagen1', 'inmueble_id')
    if request.POST:
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():  
            send_mail('Peticion cliente', formulario_contacto.cleaned_data['mensaje'] + "/" + formulario_contacto.cleaned_data ['email'], settings.EMAIL_HOST_USER, ['sergioalcazar745@gmail.com'])
            formulario_contacto=FormularioContacto()    
            return render(request, "ventas.html", {'nbar': 'ventas', 'lista_ventas': ventas_list, 'response':'true', 'mensaje':'El correo se ha enviado correctamente','form':formulario_contacto})
        else:
            return render(request, "ventas.html", {'nbar': 'ventas', 'lista_ventas': ventas_list, 'response':'false', 'mensaje':'El correo no se ha podido enviar', 'form':formulario_contacto})  
    else:
        formulario_contacto=FormularioContacto()       
        return render(request, "ventas.html", {'nbar': 'ventas', 'lista_ventas': ventas_list, 'response':'none', 'form':formulario_contacto}) 

def proximas(request):
    proximas_list = Inmueble.objects.filter(proximas=True)
    #imagenes_list = Imagene.objects.values('imagen1', 'inmueble_id')
    if request.POST:
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():  
            send_mail('Peticion cliente', formulario_contacto.cleaned_data['mensaje'] + "/" + formulario_contacto.cleaned_data ['email'], settings.EMAIL_HOST_USER, ['sergioalcazar745@gmail.com'])
            formulario_contacto=FormularioContacto()    
            return render(request, "proximas.html", {'nbar': 'proximas', 'lista_proximas': proximas_list, 'response':'true', 'mensaje':'El correo se ha enviado correctamente','form':formulario_contacto})
        else:
            return render(request, "proximas.html", {'nbar': 'proximas', 'lista_proximas': proximas_list, 'response':'false', 'mensaje':'El correo no se ha podido enviar', 'form':formulario_contacto})  
    else:
        formulario_contacto=FormularioContacto()       
        return render(request, "proximas.html", {'nbar': 'proximas', 'lista_proximas': proximas_list, 'response':'none', 'form':formulario_contacto}) 

def entregadas(request):
    entregadas_list = Inmueble.objects.filter(entregas=True)
    #imagenes_list = Imagene.objects.values('imagen1', 'inmueble_id')
    if request.POST:
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():  
            send_mail('Peticion cliente', formulario_contacto.cleaned_data['mensaje'] + "/" + formulario_contacto.cleaned_data ['email'], settings.EMAIL_HOST_USER, ['sergioalcazar745@gmail.com'])
            formulario_contacto=FormularioContacto()    
            return render(request, "entregadas.html", {'nbar': 'entregadas', 'lista_entregadas': entregadas_list, 'response':'true', 'mensaje':'El correo se ha enviado correctamente','form':formulario_contacto})
        else:
            return render(request, "entregadas.html", {'nbar': 'entregadas', 'lista_entregadas': entregadas_list, 'response':'false', 'mensaje':'El correo no se ha podido enviar', 'form':formulario_contacto})  
    else:
        formulario_contacto=FormularioContacto()       
        return render(request, "entregadas.html", {'nbar': 'entregadas', 'lista_entregadas': entregadas_list, 'response':'none', 'form':formulario_contacto}) 

def detalles(request, id):
    inmueble = Inmueble.objects.filter(id=id)
    imagenes = Imagene.objects.filter(inmueble_id=id)
    archivos = Archivo.objects.filter(inmueble_id=id)
    imagenes_list = []
    for img in imagenes:
        imagenes_list.append(img.imagen1)
        imagenes_list.append(img.imagen2)
        imagenes_list.append(img.imagen3)
        imagenes_list.append(img.imagen4)
        imagenes_list.append(img.imagen5)
        imagenes_list.append(img.imagen6)
    archivos_list = []
    for arch in archivos:
        archivos_list.append(arch.archivo1)
        archivos_list.append(arch.archivo2)
        archivos_list.append(arch.archivo3)
        archivos_list.append(arch.archivo4)
        archivos_list.append(arch.archivo5)
        
    if request.POST:
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():  
            send_mail('Peticion cliente', formulario_contacto.cleaned_data['mensaje'] + "/" + formulario_contacto.cleaned_data ['email'], settings.EMAIL_HOST_USER, ['sergioalcazar745@gmail.com'])
            formulario_contacto=FormularioContacto()    
            return render(request, "detalle.html", {'inmueble': inmueble, 'imagenes': imagenes_list, 'archivos': archivos_list, 'response':'true', 'mensaje':'El correo se ha enviado correctamente','form':formulario_contacto})
        else:
            return render(request, "detalle.html", {'inmueble': inmueble, 'imagenes': imagenes_list, 'archivos': archivos_list, 'response':'false', 'mensaje':'El correo no se ha podido enviar', 'form':formulario_contacto})  
    else:
        formulario_contacto=FormularioContacto()       
        return render(request, "detalle.html", {'inmueble': inmueble, 'imagenes': imagenes_list, 'archivos': archivos_list, 'response':'none', 'form':formulario_contacto}) 

def noticias(request):
    noticias = Noticia.objects.all()
    if request.POST:
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():  
            send_mail('Peticion cliente', formulario_contacto.cleaned_data['mensaje'] + "/" + formulario_contacto.cleaned_data ['email'], settings.EMAIL_HOST_USER, ['sergioalcazar745@gmail.com'])
            formulario_contacto=FormularioContacto()    
            return render(request, "noticias.html", {'nbar': 'home', 'lista_noticias':noticias, 'response':'true', 'mensaje':'El correo se ha enviado correctamente','form':formulario_contacto}) 
        else:
            return render(request, "noticias.html", {'nbar': 'home', 'lista_noticias':noticias, 'response':'false', 'mensaje':'El correo no se ha podido enviar', 'form':formulario_contacto})  
    else:
        formulario_contacto=FormularioContacto()       
        return render(request, "noticias.html", {'nbar': 'noticias', 'lista_noticias':noticias, 'response':'none', 'form':formulario_contacto})
    
def detalleNoticias(request, id):
    noticia = Noticia.objects.get(id=int(id))
    if request.POST:
        formulario_contacto=FormularioContacto(request.POST)
        if formulario_contacto.is_valid():  
            send_mail('Peticion cliente', formulario_contacto.cleaned_data['mensaje'] + "/" + formulario_contacto.cleaned_data ['email'], settings.EMAIL_HOST_USER, ['sergioalcazar745@gmail.com'])
            formulario_contacto=FormularioContacto()    
            return render(request, "detalle-noticia.html", {'noticia': noticia, 'response':'true', 'mensaje':'El correo se ha enviado correctamente','form':formulario_contacto}) 
        else:
            return render(request, "detalle-noticia.html", {'noticia': noticia, 'response':'false', 'mensaje':'El correo no se ha podido enviar', 'form':formulario_contacto})  
    else:
        formulario_contacto=FormularioContacto()       
        return render(request, "detalle-noticia.html", {'noticia': noticia, 'response':'none', 'form':formulario_contacto}) 

def politicaPrivacidad(request):
    return render(request, "politica-privacidad.html")

def error_404(request, exception):
    return render(request, '404.html')
