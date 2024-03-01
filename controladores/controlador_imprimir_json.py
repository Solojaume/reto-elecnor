from casos_de_uso.caso_uso_convertir_a_json import convertir_a_json

def imprimir_json(ruta_archivo):
    datos_json = convertir_a_json(ruta_archivo)
    for json_data in datos_json:
        print(json_data)