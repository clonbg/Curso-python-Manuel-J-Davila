import glob
import os.path

todos = glob.glob("directorio/*")
print(todos)

archivos = []
directorios = []
for item in todos:
    if (os.path.isfile(item)):
        archivos.append(item)
    else:
        directorios.append(item)


print(archivos)
print(directorios)

txt = glob.glob('directorio/*.txt')
print(txt)

ext3char = glob.glob('directorio/*.???')
print(ext3char)
