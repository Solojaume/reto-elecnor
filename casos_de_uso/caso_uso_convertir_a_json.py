from casos_de_uso.caso_uso_leer_csv import leer_csv

def convertir_a_json(ruta_archivo):
    datos = leer_csv(ruta_archivo)
    json_data = []

    for linea in datos[1:]:
        json_linea = {
            'Matricula': linea[0],
            'Latitud': float(linea[1]),
            'Longitud': float(linea[2]),
            'Distance': float(linea[3]),
            'Pos_date': int(linea[4])
        }
        json_data.append(json_linea)

    return json_data