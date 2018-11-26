from django.shortcuts import render
from .models import Usuarios

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