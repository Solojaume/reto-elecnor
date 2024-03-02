from casos_de_uso.caso_uso_convertir_a_json import convertir_a_json
from casos_de_uso.caso_uso_sumar_distancias import sumar_distancias

def sumar_distancias_e_imprimir(ruta_archivo):
    datos_json = convertir_a_json(ruta_archivo)
    resultados = sumar_distancias(datos_json)

    for matricula, suma_distancias in resultados.items():
        print(f"Matricula: {matricula}, Suma de Distancias: {suma_distancias}")
