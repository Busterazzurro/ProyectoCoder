from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cliente, Auto, Viaje

#INICIO
def inicio(request):
    
    return render(request, 'AppCoder/Inicio.html', {})

#CLIENTES
def lista_clientes(request):
    
    if request.method == 'GET':
        numero = request.GET.get('numero', None)
        try:
            numero = int(numero)
        except:
            error = 'Debes ingresar un numero entero'
        clientes = Cliente.objects.filter(numero=numero)
        
    
    clientes = Cliente.objects.all()
    return render(request, 'AppCoder/lista_clientes.html', {'clientes': clientes, 'error': error})

#AUTOS
def lista_autos(request):
    
    if request.method == 'GET':
        numero = request.GET.get('numero', None)
        try:
            numero = int(numero)
        except:
            error = 'Debes ingresar un numero entero'
        autos = Auto.objects.filter(numero=numero)
    
    autos = Auto.objects.all()
    return render(request, 'AppCoder/lista_autos.html', {'autos': autos, 'error': error})

#VIAJES
def lista_viajes(request):
    
    if request.method == 'GET':
        numero = request.GET.get('numero', None)
        try:
            numero = int(numero)
        except:
            error = 'Debes ingresar un numero entero'
        viajes = Viaje.objects.filter(numero=numero)
    
    viajes = Viaje.objects.all()
    return render(request, 'AppCoder/lista_viajes.html', {'viajes': viajes, 'error': error})
