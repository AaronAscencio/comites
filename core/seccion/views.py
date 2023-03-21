from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def load_distritos(request):
    file = open('C:/Users/AaronAscencio/Documents/Comites de Transformacion/project/data/distritos.csv','r')
    for line in file.readlines():
        numero = int(line.strip('\n'))
        distrito = Distrito(numero = numero)
        print(distrito)
        #distrito.save()
    return render(request,'index.html',context={})

def load_municipios(request):
    file = open('C:/Users/AaronAscencio/Documents/Comites de Transformacion/project/data/municipios.csv','r',encoding='utf-8')
    for line in file.readlines():
        line = line.strip('\n').split('|')
        distrito = Distrito.objects.get(numero = int(line[0]))
        municipio = Municipio(distrito = distrito, nombre = line[1])
        #print(municipio)
        #municipio.save()
    return render(request,'index.html',context={}) 

def load_secciones(request):
    file = open('C:/Users/AaronAscencio/Documents/Comites de Transformacion/project/data/secciones.csv','r',encoding='utf-8')
    for line in file.readlines():
        line = line.strip('\n').split('|')
        municipio = Municipio.objects.get(nombre = line[1])
        seccion = Seccion(municipio = municipio,numero = int(line[2]))
        #seccion.save()
    return render(request,'index.html',context={}) 

@csrf_exempt
def index(request):
    if request.method == 'POST':
        municipio = Municipio.objects.get(id = request.POST['id'])
        print(municipio)
    return render(request,'index.html',context={})  
