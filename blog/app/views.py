from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def inicio(request):
    pub = Publicacion.objects.all()
    return render_to_response("index.html", {"publicacion":pub}, context_instance = RequestContext(request))

def recientes(request):
    pub = Publicacion.objects.all()
    return render_to_response("base.html", {"publicacion":pub}, context_instance = RequestContext(request))
