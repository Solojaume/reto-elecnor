from casos_de_uso.caso_uso_leer_archivo_ultimas_posiciones import cargar_ultimas_posiciones_desde_archivo

def cargar_datos_desde_archivo(nombre_tabla,ruta_archivo_ultimas_posiciones, adaptador_sqlite):
    u_p = cargar_ultimas_posiciones_desde_archivo(ruta_archivo_ultimas_posiciones)
    
    for matricula in u_p:
        fecha = u_p[matricula]
        valores = {'matricula': matricula, 'fecha_ultima_posicion': fecha}
        adaptador_sqlite.insert(nombre_tabla, valores)