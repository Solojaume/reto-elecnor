def cargar_ultimas_posiciones_desde_archivo(ruta_archivo):
    posiciones = {}
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            matricula, fecha = linea.strip().split(': ')
            posiciones[matricula] = fecha
    return posiciones
