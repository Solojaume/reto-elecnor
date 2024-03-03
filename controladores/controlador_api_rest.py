
from flask import Flask, jsonify
from casos_de_uso.caso_uso_leer_archivo_ultimas_posiciones import cargar_ultimas_posiciones_desde_archivo


app = Flask(__name__)

ultimas_posiciones = {}

@app.route('/<matricula>', methods=['GET'])
def obtener_ultima_posicion(matricula):
    if matricula in ultimas_posiciones:
        fecha_ultima_posicion = ultimas_posiciones[matricula]
        return jsonify({"matricula": matricula, "fecha_ultima_posicion": fecha_ultima_posicion})
    else:
        return jsonify({"error": "Matrícula no encontrada"}), 404


def arrancar_api_rest(ruta_archivo_ultimas_posiciones,debug_option):
    global ultimas_posiciones
    ultimas_posiciones = cargar_ultimas_posiciones_desde_archivo(ruta_archivo_ultimas_posiciones)
    app.run(debug = debug_option)