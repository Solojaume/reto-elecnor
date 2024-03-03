from controladores.controlador_imprimir_lineas import imprimir_lineas
from controladores.controlador_imprimir_json import imprimir_json
from controladores.controlador_sumar_distancias import sumar_distancias_e_imprimir
from controladores.controlador_sumar_distancias_por_matricula import sumar_distancias_por_matricula_e_imprimir
from controladores.controlador_ultimas_posiciones import generar_y_escribir_ultimas_posiciones
from controladores.controlador_arancar_api_rest_archivo import *

if __name__ == "__main__":
    ruta_archivo_entrada = "archivos/reto.csv"
    ruta_archivo_salida_ultimas_posiciones = "archivos/reto_salida.txt"

    print("Ingrese el número del caso a ejecutar (1 a 8): ")
    
    # Pedir al usuario que elija un caso
    try:
        caso_elegido = int(input())

        if caso_elegido == 1:
            imprimir_lineas(ruta_archivo_entrada)

        elif caso_elegido == 2:
            imprimir_json(ruta_archivo_entrada)
        
        elif caso_elegido == 3:
            sumar_distancias_e_imprimir(ruta_archivo_entrada)
            
        elif caso_elegido == 4:
            sumar_distancias_por_matricula_e_imprimir(ruta_archivo_entrada)

        elif caso_elegido == 5:
            generar_y_escribir_ultimas_posiciones(ruta_archivo_entrada, ruta_archivo_salida_ultimas_posiciones)

        elif caso_elegido == 6:
            arrancar_api_rest_desde_archivo(ruta_archivo_salida_ultimas_posiciones,False)
            
        else:
            print("Caso no válido.")

    except ValueError as e:
        print("Por favor, ingrese un número válido. El error es: " + e )