from django.shortcuts import render
from .models import Usuarios
from .forms import Formulario
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request,'app_de_in3501/index.html')

def lista_usuarios(request):
    contexto = {}
    contexto['usuarios'] = Usuarios.objects.all()
    return render(request,'app_de_in3501/lista_usuarios.html', contexto)

def inputs(request):
    return render(request, 'app_de_in3501/inputs.html')

def formulario_dudas(request):
    return render(request, 'app_de_in3501/formulario_dudas.html')

def adduser(request):
    form=Formulario()
    info={'titulo':'Agregar Usuarios', 'intro':"Registrese, Entreguenos todos sus datos aqui",'form':form} # se escribe como atributo__condicion = valor_buscado # esto es del tipo where usuarios.puntaje_psu>740
    return render(request,'app_de_in3501/adduser.html', info)
   
def added(request):
	new_user=Usuarios(nombre=request.POST['nombre'],apellido=request.POST['apellido'],direccion=request.POST['direccion'], rut=request.POST['rut'], puntaje_psu=request.POST['puntaje_psu'], username=request.POST['username'], password=request.POST['password'], email=request.POST['email']);	new_user.save()
	new_user.save()
	context={'Titulo':'Formulario Correcto', 'comentario':'Gracias'}
	return render(request, 'app_de_in3501/added.html', context)