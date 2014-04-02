from django.forms import ModelForm
from django import forms
from .models import Publicacion
from django.contrib.auth.models import User

class ContactoForm(forms.Form):
	correo=forms.EmailField(label="Correo Electronico")
	asunto=forms.CharField(label='Asunto')
	mensaje=forms.CharField(widget=forms.Textarea, label='Mensaje')

class PublicacionForm(ModelForm):
	class Meta:
		model = Publicacion
		exclude = ('fechaPub', 'votos', 'autor')

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=True)

