from re import template
from django import template
from grupoInmoApp.models import Inmueble

register = template.Library()

@register.filter
def parImpar(num):
    return num % 2