import csv

class AdaptadorCSV:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer_datos(self):
        with open(self.ruta_archivo, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            datos = [linea for linea in lector_csv]
        return datos