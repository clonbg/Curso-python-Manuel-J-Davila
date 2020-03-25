# w escribe y reemplaza si existe
# a escribe si no existe y añade al final
# r leer

fichero = open('fichero.txt', 'w')
texto = 'Vamos a escribir una línea'
fichero.write(texto)
fichero.close()

fichero = open('fichero.txt', 'a')
texto = '\nVamos a escribir otra línea'
fichero.write(texto)
fichero.close()


fichero = open('fichero.txt', 'r')
print(fichero.read())
fichero.close()

fichero = open('fichero.txt', 'r')
for item in fichero:
    print(item, end='')
fichero.close()
