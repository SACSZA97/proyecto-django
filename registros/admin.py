from django.contrib import admin
from .models import Alumnos
from .models import Comentarios
from .models import ComentarioContacto
# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields  = ('created', 'updated')
    list_display = ('matricula','nombre','carrera','turnno','created')
    search_fields = ('matricula','nombre','carrera','turnno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turnno')
    list_per_page=2
    list_display_links=('matricula','nombre')
    list_editable=('turnno',)

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    readonly_fields  = ('created', 'id')
    list_display = ('id','coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'

admin.site.register(Comentarios, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)