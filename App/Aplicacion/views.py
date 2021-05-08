from django.shortcuts import render, redirect
import requests
from .forms import EntradaForm

endpoint = 'http://127.0.0.1:8000/' 
global contexto

def inicio(x):
    return render(x, 'Inicio.html')


def enviararchivo(request):
    contexto={}
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            archivivo  = request.FILES['file'].read()
            archivivo = archivivo.decode("utf-8")
            response = requests.post(endpoint + 'enviado', data= archivivo)
            contexto = {
                'entradatos': archivivo,
                'nuevo': response
            }

            
    return render(request, 'Inicio.html', contexto)

    
def salida_entrada(request):
    if request.method == 'GET':
        new = requests.get('http://127.0.0.1:8000/')
        info = {
            'salida_entrada': new.text,
        }
        return render(request, 'Inicio.html',info)
    

