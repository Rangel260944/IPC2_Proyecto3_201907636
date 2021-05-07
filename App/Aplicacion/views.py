from django.shortcuts import render, redirect
import requests

endpoint = 'http://127.0.0.1:8000/' 

def inicio(x):
    return render(x, 'Inicio.html')
# Create your views here.




def enviararchivo(request):
    contexto={'content':'', 'response':''}
    if request.method == 'POST':
        archvivo  = request.FILES['file'].read()
        requests.post(endpoint + 'cargarArchivo', archvivo)
    return render(request, 'Inicio.html', contexto)