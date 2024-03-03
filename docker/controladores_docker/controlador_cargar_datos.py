from adaptadores_docker.adaptador_sqlite import AdaptadorSQLite

from casos_uso_docker.caso_uso_cargar_datos import *

def cargar_datatos_bd(archivo_db ,nombre_tabla, ruta_archivo_ultimas_posiciones):
    adaptador_sqlite = AdaptadorSQLite(archivo)


    adaptador_sqlite.create_table(
        nombre_tabla,
        [
            { nombre: "matricula", config:{type:"Text", primary:True}},
            { nombre: "fecha_ultima_posicion",config:{type:"Text"}}    
        ]
    )
    
    cargar_datos_desde_archivo(nombre_tabla, ruta_archivo_ultimas_posiciones, adaptador_sqlite)
