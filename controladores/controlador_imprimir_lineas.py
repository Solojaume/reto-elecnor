from casos_de_uso.caso_uso_leer_csv import leer_csv

def imprimir_lineas(ruta_archivo):
    datos = leer_csv(ruta_archivo)
    for linea in datos:
        print(linea)
