from casos_de_uso.caso_uso_convertir_a_json import convertir_a_json
from casos_de_uso.caso_uso_sumar_distancias_por_matricula import sumar_distancias_por_matricula

def sumar_distancias_por_matricula_e_imprimir(ruta_archivo):
    datos_json = convertir_a_json(ruta_archivo)
    resultados = sumar_distancias_por_matricula(datos_json)

    for matricula, suma_distancias in resultados.items():
        print(f"Matricula: {matricula}, Suma de Distancias: {suma_distancias} km")

