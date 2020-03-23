entero = input('Introduzca un número entero: ')
try:
    entero = int(entero)
    print('Enhorabuena')
except ValueError:
    print('Ohhhhh')

print(entero)
