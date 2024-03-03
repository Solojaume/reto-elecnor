from flask import Flask, jsonify
from casos_de_uso.caso_uso_leer_archivo_ultimas_posiciones import cargar_ultimas_posiciones_desde_archivo
from controladores.controlador_api_rest import *

def arrancar_api_rest_desde_archivo(ruta_archivo_ultimas_posiciones,debug_option):
    cargar_ultima_posicion(cargar_ultimas_posiciones_desde_archivo(ruta_archivo_ultimas_posiciones))
    app.run(debug = debug_option)
