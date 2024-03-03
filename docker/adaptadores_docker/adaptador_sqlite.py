import sqlite3

class AdaptadorSQLite:
    def __init__(self, ruta_db):
        self.con = sqlite3.connect(ruta_db)
        self.cursor = self.conn.cursor()

    #Columnas :[{ nombre: string, config:{type:"EL TIPO QUE SEA", primary:boolean, unique:boolean, otros:string}}] 
   def create_table(self, table_name, columnas):
        # Crear la sentencia SQL para la creación de la tabla
        sql = f"CREATE TABLE {table_name} ("
        for columna in columnas:
            nombre = columna['nombre']
            config = columna['config']
            tipo = config['type']
            primary = 'PRIMARY KEY' if config.get('primary', False) else ''
            unique = 'UNIQUE' if config.get('unique', False) else ''
            otros = config.get('otros', '')
            sql += f"{nombre} {tipo} {primary} {unique} {otros}, "
        sql = sql.rstrip(", ") + ");"

        # Ejecutar la sentencia SQL
        self.cursor.execute(sql)
        self.conn.commit()

    def get(self, table_name, condiciones):
        # Construir la sentencia SQL para la consulta
        condiciones_sql = " AND ".join([f"{key} = '{value}'" for key, value in condiciones.items()])
        sql = f"SELECT * FROM {table_name} WHERE {condiciones_sql};"

        # Ejecutar la consulta
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()

        return resultado

    def get_all(self, table_name):
        # Construir la sentencia SQL para la consulta
        sql = f"SELECT * FROM {table_name};"

        # Ejecutar la consulta
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()

        return resultados

    def insert(self, table_name, valores):
        # Construir la sentencia SQL para la inserción
        columnas = ", ".join(valores.keys())
        valores_sql = ", ".join([f"'{value}'" for value in valores.values()])
        sql = f"INSERT INTO {table_name} ({columnas}) VALUES ({valores_sql});"

        # Ejecutar la inserción
        self.cursor.execute(sql)
        self.conn.commit()

    def cerrar_conexion(self):
        # Cerrar la conexión a la base de datos
        self.conn.close()