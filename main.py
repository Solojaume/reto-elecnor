from controladores.controlador_imprimir_lineas import imprimir_lineas
from controladores.controlador_imprimir_json import imprimir_json
from controladores.controlador_sumar_distancias import sumar_distancias_e_imprimir
from controladores.controlador_sumar_distancias_por_matricula import sumar_distancias_por_matricula_e_imprimir,comparar_resultados_e_imprimir

if __name__ == "__main__":
    ruta_archivo = "archivos/reto.csv"

    print("Ingrese el número del caso a ejecutar (1 a 8): ")
    
    # Pedir al usuario que elija un caso
    try:
        caso_elegido = int(input())

        if caso_elegido == 1:
            imprimir_lineas(ruta_archivo)

        elif caso_elegido == 2:
            imprimir_json(ruta_archivo)
        
        elif caso_elegido == 3:
            sumar_distancias_e_imprimir(ruta_archivo)
            
        elif caso_elegido == 4:
            sumar_distancias_por_matricula_e_imprimir(ruta_archivo)
            comparar_resultados_e_imprimir(ruta_archivo)

        else:
            print("Caso no válido.")

    except ValueError as e:
        print("Por favor, ingrese un número válido. El error es: " + e )
