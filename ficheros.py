# w escribe y reemplaza si existe
# a escribe si no existe y añade al final
# r leer

fichero=open('fichero.txt', 'a')
texto='Vamos a escribir una línea\n'
fichero.write(texto)
fichero.close()