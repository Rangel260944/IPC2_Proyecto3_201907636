from django.shortcuts import render, redirect
import requests
from .forms import EntradaForm



endpoint = 'http://127.0.0.1:5000/'


def inicio(x):
    return render(x, 'Inicio.html')


def enviararchivo(request):
    contexto={}
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            archivivo  = request.FILES['file'].read()
            archivivo = archivivo.decode("utf-8")
            file = open('C:/Users/Carlos Rangel/Documents/GitHub/IPC2_Proyecto3_201907636/Backend/entrada.xml', 'w')
            file.write(archivivo)
            file.close()
            response = requests.post(endpoint + 'enviado', data= archivivo)
            contexto = {
                'organizado': archivivo
            }
    return render(request, 'Inicio.html', contexto)

def salida(request):
    contxt = {}
    if request.method == 'GET':
        estadistica = ""
        entrada = ""
        file = open('C:/Users/Carlos Rangel/Documents/GitHub/IPC2_Proyecto3_201907636/Backend/estadisticas.xml', 'r')
        cuchao_we = file.read()
        file.close()
        file = open('C:/Users/Carlos Rangel/Documents/GitHub/IPC2_Proyecto3_201907636/Backend/entrada.xml', 'r')
        con_entrada = file.read()
        file.close()
        contxt = {
            'entradatos': cuchao_we,
            'organizado': con_entrada
        }
    return render(request, 'Inicio.html', contxt)
def salida_entrada(request):
    if request.method == 'GET':
        new = requests.get('http://127.0.0.1:8000/')
        info = {
            'salida_entrada': new.text,
        }
        return render(request, 'Inicio.html',info)


