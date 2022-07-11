from django.urls import path
from .views import index, destino, disponibilidad, mostrar_cliente

urlpatterns =[
    path('', index,name="index"),
    path('destino/', destino,name="destino"),
    path('disponibilidad/', disponibilidad,name="disponibilidad"),
    path('clientes/', mostrar_cliente,name="clientes")
]