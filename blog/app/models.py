from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User)
    avatar = models.ImageField(upload_to = 'Avatar', null=True, blank=True)
    descripcion = models.TextField(max_length = 255, null=True, blank=True, verbose_name = 'Sobre ti')
    
    class Meta():
        verbose_name_plural = 'Perfil'
        
    def __unicode__(self):
        return self.usuario.username
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.categoria
    
class Publicacion(models.Model):
    autor = models.ForeignKey(Perfil)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=60, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    contenido = models.TextField(max_length = 255)
    categoria = models.ManyToManyField(Categoria)
    fechaPub = models.DateTimeField(auto_now_add = True)
    imagen = models.ImageField(upload_to="img-pub", null=True, blank=True)
    
    class Meta():
        verbose_name_plural = 'Publicaciones'
    
    def __unicode__(self):
        return self.titulo
    
class Comentario(models.Model):
    autor = models.ForeignKey(User)
    publicacion = models.ForeignKey(Publicacion)
    comentario = models.TextField(max_length = 255)
    
    def __unicode__(self):
        return self.comentario
    
class Like(models.Model):
    publicacion = models.ForeignKey(Publicacion)
    usuario = models.ForeignKey(User)
    like = models.BooleanField()
    
    def __unicode__(self):
        return unicode(self.id)
    
    

