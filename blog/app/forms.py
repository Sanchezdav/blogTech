from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
	correo=forms.EmailField(label="Correo Electronico")
	asunto=forms.CharField(label='Asunto')
	mensaje=forms.CharField(widget=forms.Textarea, label='Mensaje')