from django.urls import path
from grupoInmoApp import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name="home"),
    path('ventas', views.ventas, name="ventas"),
    path('proximas', views.proximas, name="proximas"),
    path('entregadas', views.entregadas, name="entregadas"),
    path('noticias', views.noticias, name="noticias"),
    path('detalles/<str:id>', views.detalles, name="detalles"),
    path('detalle-noticia/<str:id>', views.detalleNoticias, name="detalle-noticia"),
    path('politica-privacidad', views.politicaPrivacidad, name="politica")
]

handler404 = "grupoInmoApp.views.error_404"
