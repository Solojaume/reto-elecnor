from adaptadores.adaptador_csv import AdaptadorCSV

def leer_csv(ruta_archivo):
    adaptador_csv = AdaptadorCSV(ruta_archivo)
    return adaptador_csv.leer_datos()