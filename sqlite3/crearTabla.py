import sqlite3
# Conectar
conexion = sqlite3.connect('sqlite3/test.sqlite3')

# Cursor para la consulta
consulta = conexion.cursor()

sql = """CREATE TABLE IF NOT EXISTS test(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    cadena_texto VARCHAR(50) NOT NULL,
    entero  INTEGER NOT NULL,
    decimal FLOAT NOT NULL,
    fecha DATE NOT NULL)"""

# Ejecutar
if (consulta.execute(sql)):
    print('Tabla creada con éxito')
else:
    print('Ha ocurrido un error')

consulta.close()
# Guardamos los cambios
conexion.commit()

conexion.close()
