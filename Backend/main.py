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
    return "Cargando archivo"


@app.route('/enviado',methods=['POST'])
def getfile():
    separa.expresiones()
    return "Funciona"

@app.route('/fechas', methods=['GET'])
def consulta():
    print("")
if __name__ == "__main__":
    app.run(debug=True)
