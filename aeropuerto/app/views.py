from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def destino(request):
    return render(request, 'destino.html')

def disponibilidad(request):
    return render(request, 'disponibilidad.html')



def mostrar_cliente(request):
    clientes = Cliente.objects.all()

    datos= {
        'clientes' : clientes
    }
    return render(request, 'clientes.html', datos)
