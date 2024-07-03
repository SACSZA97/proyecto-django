from django.shortcuts import render, HttpResponse
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from .models import Comentarios
from django.shortcuts import get_object_or_404

# Create your views here.
def registros(request):
    alumnos= Alumnos.objects.all()
    return  render(request,"registros/principal.html",{'9B':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios = ComentarioContacto.objects.all()
            return render(request,'registros/consultarContacto.html',
                {'comentarios':comentarios})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

def comentario(request):
    comentario= Comentarios.objects.all()
    return  render(request,"registros/consultarComentarios.html",{'comentario':comentario})

def contacto(request):
    return render(request,"registros/contacto.html")

def eliminarComentarioContacto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
         comentario.delete()
         comentarios=ComentarioContacto.objects.all()
         return render(request,"registros/consultaContacto.html",

            {'comentarios':comentarios})

    return render(request, confirmacion, {'object':comentario})