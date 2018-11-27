from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	# formato: dirección_pag, función_asociada , name=nombre
    	path('',views.index, name='index'),
		path('lista_usuarios',views.lista_usuarios, name='lista_usuarios'),
		path('inputs', views.inputs, name='inputs'),
		path('formulario_dudas', views.formulario_dudas, name='formulario_dudas'),
		path('adduser', views.adduser, name='adduser'),
    	path('added', views.added, name='added'),
]