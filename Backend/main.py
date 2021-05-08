from flask import Flask, request, jsonify
from flask_cors import CORS
from Prueba import pru

app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)
prueba = pru()


@app.route('/cargarArchivo')
def cargar():
    return "Cargando archivo"


@app.route('/enviado',methods=['POST'])
def getfile():
    datos = request.data
    json = prueba.devuelto(datos)
    return json



if __name__ == "__main__":
    app.run(debug=True)