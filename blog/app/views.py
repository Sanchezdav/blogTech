from .models import *
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic import CreateView
from .forms import PublicacionForm, LoginForm

def ingresar(request):
	if request.method=='POST':
		formulario=LoginForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/')
	else:
		formulario= LoginForm()
	return render(request, 'login.html', {'formulario':formulario})

@login_required(login_url='/')
def salir(request):
	logout(request)
	request.session.flush()
	return HttpResponseRedirect('/')

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

def up(request, id_pub):
	publicacion = Publicacion.objects.get(pk=id_pub)
	publicacion.votos = publicacion.votos + 1
	publicacion.save()
	return HttpResponseRedirect('/noticias/')

def down(request, id_pub):
	publicacion = Publicacion.objects.get(pk=id_pub)
	publicacion.votos = publicacion.votos - 1
	publicacion.save()
	return HttpResponseRedirect('/noticias/')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login/')
	else:
		form = UserCreationForm()
	return render(request, 'registrarse.html', {'form':form})

class PublicacionView(CreateView):
    template_name = 'publicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        self.publicacion = form.save(commit=False)

        form.instance.autor = self.request.user
        self.publicacion.titulo = form.cleaned_data['titulo']
        self.publicacion.subtitulo = form.cleaned_data['subtitulo']
        self.publicacion.link = form.cleaned_data['link']
        self.publicacion.contenido = form.cleaned_data['contenido']
        self.publicacion.categoria = form.cleaned_data['categoria']
        self.publicacion.imagen = form.cleaned_data['imagen']
        self.publicacion.save()
        return super(PublicacionView, self).form_valid(form)