from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

# Create your views here.

def load_distritos(request):
    file = open('C:/Users/AaronAscencio/Documents/Comites de Transformacion/project/data/distritos.csv','r')
    for line in file.readlines():
        numero = int(line.strip('\n'))
        distrito = Distrito(numero = numero)
        #print(distrito)
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

def load_colonias_v1(request):
    file = open('C:/Users/AaronAscencio/Documents/Comites de Transformacion/project/data/colonias.csv','r',encoding='utf-8')
    secciones = []
    for line in file.readlines():
        line = line.strip('\n').split('|')
        try:
            seccion = Seccion.objects.get(numero = int(line[0]))
            colonia = Colonia(
                seccion = seccion,
                tipo_de_seccion = line[1],
                tipo_de_colonia = line[2],
                nombre = line[3],
                cp = '' if line[4] == '' else int(line[4])
            )
            print(colonia)
        except Exception as e:
            if int(line[0]) not in secciones:
                secciones.append(int(line[0]))
    secciones.sort()
    print(secciones)
        #seccion.save()
    return render(request,'index.html',context={}) 


def load_complemento(request):
    file = open('C:/Users/AaronAscencio/Documents/Comites de Transformacion/project/data/complemento.txt','r',encoding='utf-8')
    secciones = []
    for line in file.readlines():
        line = line.strip('\n').split('|')
        try:
            municipio = Municipio.objects.get(nombre = line[0])
            #print(municipio)
        except Exception as e:
            print(line)

    return render(request,'index.html',context={}) 

def load_colonias(request):
        
    file = open('C:/Users/AaronAscencio/Documents/Comites de Transformacion/project/data/colonias.csv', 'r', encoding='utf-8')
    lines = file.readlines()
    print(len(lines))

    colonias = []  # Lista para almacenar los objetos de colonia


    seccion_95 = Seccion.objects.get(
        numero = 95
    )
    print(seccion_95)
    for line in lines:
        try:
            line = line.strip('\n').split('|')
            seccion = Seccion.objects.get(numero=int(line[0]))
            colonia = Colonia(
                seccion=seccion,
                tipo_de_seccion=line[1],
                tipo_de_colonia=line[2],
                nombre=line[3],
                cp='' if line[4] == '' else int(float(line[4]))
            )

            

            #Colonia.objects.all().delete()
            #colonia.save()
        
        except Exception as e:
            print(str(e),line)
            #colonias.append(colonia)  # Agregar el objeto de colonia a la lista
    # Guardar todos los objetos de colonia en la base de datos
    #with transaction.atomic():
    #    Colonia.objects.bulk_create(colonias)


    return render(request, 'index.html', context={})
    
