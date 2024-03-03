from controladores_docker.controlador_cargar_datos import cargar_datatos_bd


if __name__ == "__main__":
    cargar_datatos_bd("reto.db","ultimas_posiciones","../archivos/reto_salida.txt")
    print("Base de datos inicializada y datos cargados.")