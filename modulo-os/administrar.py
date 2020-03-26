import os

def init():
    print('Administrar carpetas')
    opcion=input('Eliga una opción, c(crear) y e(eliminar): ')
    if (opcion == 'c'):
        ruta= input('Indique la ruta, por defecto la actual: ')
        if ruta=='':
            ruta=os.getcwd()+'\\'
        if os.path.isdir(ruta):
            