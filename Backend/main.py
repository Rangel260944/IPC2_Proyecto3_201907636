from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

@app.route('/cargarArchivo')
def cargar():
    return "Cargando archivo"


