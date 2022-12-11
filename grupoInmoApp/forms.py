from logging import PlaceHolder
from django import forms


class FormularioContacto(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control', 'placeholder': 'ejemplo@ejemplo.com'}), label="Email", error_messages={'blank': 'Por favor escriba su email', 'null': 'Por favor escriba su email', 'invalid': 'Escribe un email válido'})
    mensaje = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'rows': 6, 'class': 'form-control', 'placeHolder':"Comentarios..."}))


# def clean_mensaje(self):
#     mensaje = self.cleaned_data['mensaje']
#     if len(mensaje.split()) < 5:
#         raise forms.ValidationError(
#             "No son suficientes palabras.Por favor, especifique más")
#     return mensaje
