import os


def init():
    print('Administrar carpetas')
    opcion = input('Eliga una opción, c(crear) y e(eliminar): ')
    if (opcion == 'c'):
        ruta = input('Indique la ruta, por defecto la actual: ')
        if ruta == '':
            ruta = os.getcwd() + '/'
        else:
            ruta += '/'
            # print(ruta)
        if os.path.isdir(ruta):
            tipo = input('Indique si es un a(archivo) o una c(carpeta): ')
            if tipo == 'a':
                nombre = input('Indique el nombre del archivo: ')
                fichero = open(ruta + nombre, 'w')
                fichero.close()
                print('Creado¡¡¡')
            elif tipo == 'c':
                nombre = input('Indique el nombre de la carpeta: ')
                os.mkdir(ruta+nombre)
                print('Creada¡¡¡')
            else:
                init()  # reinicia
    elif (opcion == 'e'):
        ruta = input('Indique la ruta, por defecto la actual: ')
        if ruta == '':
            ruta = os.getcwd() + '/'
        eliminar = input('Nombre de archivo o carpeta a eliminar: ')
        if os.path.isfile(ruta+eliminar):
            os.remove(ruta+eliminar)
            print('Eliminado¡¡¡')
        elif os.path.isdir(ruta+eliminar):
            os.rmdir(ruta + eliminar)
            print('Eliminada¡¡¡')
        else:
            init()
    else:
        init()


init()
