import sqlite3
import datetime

print('***** Insertar registros *****')

cadena_texto = input('Introduzca texto')
entero = input('Introduzca un numero entero')
decimal = input('Introduzca un decimal')

try:
    entero = int(entero)
except ValueError:
    print('No es un numero entero')
    exit()
try:
    decimal = float(decimal) or int(decimal)
except ValueError:
    print('No es un numero, ni entero, ni decimal')
    exit()

# Conexión
conexion = sqlite3.connect('sqlite3/test.sqlite3')

# Cursor
consulta = conexion.cursor()

# Argumentos
argumentos = (cadena_texto, entero, decimal, datetime.date.today())

# String con la consulta y argumentos
sql = """
INSERT INTO test(cadena_texto,entero,decimal,fecha)
VALUES(?,?,?,?)
"""

# Consulta
if consulta.execute(sql, argumentos):
    print('Registro correcto')
else:
    print('Ha habido un error')

# Guardamos los cambios
conexion.commit()

consulta.close()
