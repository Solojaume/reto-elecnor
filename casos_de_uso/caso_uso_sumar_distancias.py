def sumar_distancias(datos_json):
    resultados = {}

    for vehiculo in datos_json:
        matricula = vehiculo['Matricula']
        distancia = vehiculo['Distance']

        if matricula in resultados:
            resultados[matricula] += distancia
        else:
            resultados[matricula] = distancia

    return resultados
