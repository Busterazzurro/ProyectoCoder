from django.urls.conf import path
from .views import inicio, lista_clientes, lista_autos, lista_viajes


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('clientes/', lista_clientes, name='Clientes'),
    path('autos/', lista_autos, name='Autos'),
    path('viajes/', lista_viajes, name='Viajes')
]
