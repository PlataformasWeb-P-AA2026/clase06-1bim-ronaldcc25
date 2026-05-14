import csv
import sqlite3

# Configuración
ARCHIVO_CSV = 'data/info.csv'
BASE_DATOS = 'base_ejemplo.db'
NOMBRE_TABLA = 'Autor'

# 1. Conectar a la base de datos
conexion = sqlite3.connect(BASE_DATOS)
cursor = conexion.cursor()

# 2. Leer el CSV e insertar los datos
with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)  # Nos saltamos los encabezados

    for fila in lector:
        # CORRECCIÓN: Le decimos a SQLite en qué columnas van los 4 datos del CSV
        query = f'''
            INSERT INTO {NOMBRE_TABLA} (nombre, apellido, cedula, edad)
            VALUES (?, ?, ?, ?)
        '''
        cursor.execute(query, fila)

# 3. Guardar cambios y cerrar
conexion.commit()
conexion.close()

print('Datos subidos con éxito con IDs auto-incrementales')
