from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cliente, Auto, Viaje

#INICIO
def inicio(request):
    
    return render(request, 'AppCoder/Inicio.html', {})

#CLIENTES
def lista_clientes(request):
    clientes = None
    error = None
    if request.method == 'GET':
        numero = request.GET.get('numero', '')
        if numero =='':
            clientes = Cliente.objects.all()
        else:
            try:
                numero = int(numero)
                clientes = Cliente.objects.filter(numero=numero)
            except:
                error = 'Debes ingresar un numero entero'

    return render(request, 'AppCoder/lista_clientes.html', {'clientes': clientes, 'error': error})

#AUTOS
def lista_autos(request):
    autos = None
    error = None
    if request.method == 'GET':
        numero = request.GET.get('numero', '')
        if numero =='':
            autos = Auto.objects.all()
        else:
            try:
                numero = int(numero)
                autos = Auto.objects.filter(numero=numero)
            except:
                error = 'Debes ingresar un numero entero'
                
    return render(request, 'AppCoder/lista_autos.html', {'autos': autos, 'error': error})

#VIAJES
def lista_viajes(request):
    viajes = None
    error = None
    if request.method == 'GET':
        numero = request.GET.get('numero', '')
        if numero =='':
            viajes = Viaje.objects.all()
        else:
            try:
                numero = int(numero)
                viajes = Viaje.objects.filter(numero=numero)
            except:
                error = 'Debes ingresar un numero entero'

    return render(request, 'AppCoder/lista_viajes.html', {'viajes': viajes, 'error': error})
