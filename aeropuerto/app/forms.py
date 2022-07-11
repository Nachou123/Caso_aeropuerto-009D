from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente 


class ClienteForm(forms.ModelForm):

    class Meta:
        model= Cliente 
        fields = ['rut', 'nombrecliente', 'destino', 'correo', 'fono']
        labels ={
            'rut' : 'rut',
            'nombrecliente' : 'Nombrecliente',
            'destino' : 'Destino',
            'correo' : 'Correo',
            'fono' : 'Fono',
        }

        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id del cliente', 
                    'id': 'rut'
                }
            ), 
            'nombrecliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del cliente', 
                    'id': 'nombreCliente'
                }
            ),
            'destino': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese destino del cliente', 
                    'id': 'destino'
                }
            ), 
            'Correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el correo del cliente', 
                    'id': 'correo'
                }
            ),
            'fono': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese fono del cliente', 
                    'id': 'fono'
                }
            ),
    
        





        }
