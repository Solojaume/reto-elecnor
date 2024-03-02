from casos_de_uso.caso_uso_convertir_a_json import convertir_a_json
from casos_de_uso.caso_uso_ultimas_posiciones import obtener_ultimas_posiciones, escribir_ultimas_posiciones_a_archivo

def generar_y_escribir_ultimas_posiciones(ruta_archivo_entrada, ruta_archivo_salida):
    datos_json = convertir_a_json(ruta_archivo_entrada)
    ultimas_posiciones = obtener_ultimas_posiciones(datos_json)
    escribir_ultimas_posiciones_a_archivo(ultimas_posiciones, ruta_archivo_salida)
