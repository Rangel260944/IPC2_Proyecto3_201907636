from flask import Flask, request, jsonify
from flask_cors import CORS
from Prueba import pru
from Separador import analizar
app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)
prueba = pru()
separa = analizar()

@app.route('/cargarArchivo')
def cargar():
    global separa
    return "Cargando archivo"


@app.route('/enviado',methods=['POST'])
def getfile():
    global separa
    separa.expresiones()
    return "Funciona"

@app.route('/reseteado', methods=['POST'])
def resetear():
    global separa
    separa = analizar()

@app.route('/fechas/<fecha>', methods=['GET'])
def consulta(fecha):
    global separa
    fecha = fecha.replace("-", "/")                              #Antes de la funcion peticion borrar el archivo
    print(fecha)
    separa.peticion_fechas(fecha)
    return "Funciono"

@app.route('/codigos/<codigo>', methods=['GET'])
def consulta_cod(codigo):
    global separa  #Antes de la funcion peticion borrar el archivo
    print(codigo)
    separa.peticion_error(codigo)
    return "Funciono"


if __name__ == "__main__":
    app.run(debug=True)
