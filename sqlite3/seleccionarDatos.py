import sqlite3

conexion = sqlite3.connect('sqlite3/test.sqlite3')

consulta = conexion.cursor()
sql = 'SELECT * FROM test'

# todos los campos
if (consulta.execute(sql)):
    filas = consulta.fetchall()
    for fila in filas:
        print(fila[0], fila[1], fila[2], fila[3], fila[4])


# Uno solo
sql = 'SELECT * FROM test WHERE id=%s' % 2

if (consulta.execute(sql)):
    fila = consulta.fetchone()
    print(fila)
    print(fila[0], fila[1], fila[2], fila[3], fila[4])

# Entre...
argumentos = (2, 3)
sql = 'SELECT * FROM test WHERE id BETWEEN ? AND ?'

if (consulta.execute(sql, argumentos)):
    filas = consulta.fetchall()
    for fila in filas:
        print(fila[0], fila[1], fila[2], fila[3], fila[4])

# Nombre del campo


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conexion.row_factory = dict_factory
consulta = conexion.cursor()
sql = 'SELECT * FROM test'

if (consulta.execute(sql)):
    filas = consulta.fetchall()
    for fila in filas:
        print(fila)
        print(fila['cadena_texto'])


consulta.close()
conexion.commit()
conexion.close()
