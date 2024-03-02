from datetime import datetime

def obtener_ultimas_posiciones(datos_json):
    ultimas_posiciones = {}

    for vehiculo in datos_json:
        matricula = vehiculo['Matricula']
        fecha_posicion = int(vehiculo['Pos_date']) / 1000  # Convertir de milisegundos a segundos
        fecha_posicion = datetime.utcfromtimestamp(fecha_posicion).strftime('%d/%m/%Y %H:%M:%S')

        if matricula in ultimas_posiciones:
            ultimas_posiciones[matricula] = max(ultimas_posiciones[matricula], fecha_posicion)
        else:
            ultimas_posiciones[matricula] = fecha_posicion

    return ultimas_posiciones

def escribir_ultimas_posiciones_a_archivo(ultimas_posiciones, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for matricula, fecha in sorted(ultimas_posiciones.items(), key=lambda x: datetime.strptime(x[1], '%d/%m/%Y %H:%M:%S'), reverse=True):
            archivo.write(f"{matricula}: {fecha}\n")