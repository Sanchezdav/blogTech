from .models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

def inicio(request):
    pub = Publicacion.objects.all()[:6]
    return render_to_response("index.html", {"publicacion":pub}, context_instance = RequestContext(request))

def recientes(request):
    pub = Publicacion.objects.all()
    return render_to_response("base.html", {"publicacion":pub}, context_instance = RequestContext(request))

def noticias(request):
    pub = Publicacion.objects.all()[:6]
    return render_to_response("noticias.html", {"publicacion":pub}, context_instance = RequestContext(request))

def categorias(request):
    categoria = Categoria.objects.all()
    pub = Publicacion.objects.all()[:6]
    return render_to_response("categorias.html", {"categorias":categoria, "publicacion":pub }, context_instance = RequestContext(request))

def detalle_noticia(request, id_noticia):
	dato=get_object_or_404(Publicacion, pk=id_noticia)
	pub = Publicacion.objects.all()[:6]
	return render_to_response('detalle_noticia.html',{'noticia':dato, "publicacion":pub}, context_instance=RequestContext(request))


from app.forms import ContactoForm
from django.core.mail import EmailMessage
def contacto(request):
	pub = Publicacion.objects.all()[:6]
	if request.method=='POST':
		formulario=ContactoForm(request.POST)
		if formulario.is_valid():
			titulo='Correo de Contacto Pagina Web USI'
			contenido=formulario.cleaned_data['mensaje']+ "\n"
			contenido +='Correo de Contacto: ' + formulario.cleaned_data['correo']
			contenido +='Asunto: ' + formulario.cleaned_data['asunto']
			correo=EmailMessage(titulo, contenido, to=['sanchez.dav90@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/exitoso/')
	else:
		formulario=ContactoForm()
	return render_to_response('contacto.html',{'formulario':formulario, 'publicacion':pub}, context_instance=RequestContext(request))

def exitoso(request):
	pub = Publicacion.objects.all()[:6]
	return render_to_response('exitoso.html',{'publicacion':pub}, context_instance=RequestContext(request))