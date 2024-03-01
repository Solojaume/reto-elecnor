
from math import radians, sin, cos, sqrt, atan2

def calcular_distancia_entre_puntos(lat1, lon1, lat2, lon2):
    # Convertir grados a radianes
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Fórmula de la distancia euclidiana en la esfera terrestre
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = 6371.0 * c  # Radio medio de la Tierra en kilómetros

    return distancia

def sumar_distancias_por_matricula(datos_json):
    resultados = {}

    for vehiculo in datos_json:
        matricula = vehiculo['Matricula']
        latitud = vehiculo['Latitud']
        longitud = vehiculo['Longitud']
        distancia = vehiculo['Distance']

        if matricula not in resultados:
            resultados[matricula] = 0.0

        # Calcular la distancia si no es la primera posición
        if distancia > 0.0:
            resultados[matricula] += distancia
        else:
            # Usar la distancia si es la primera posición
            resultados[matricula] += calcular_distancia_entre_puntos(
                latitud, longitud, latitud, longitud
            )

    return resultados

