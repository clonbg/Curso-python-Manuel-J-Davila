def nombreFuncion():
    print('Hola mundo')


nombreFuncion()


def otraFuncion(String):
    print(String)


otraFuncion('Mis narices')


def sumar(num1, num2=0):
    print((num1+num2))


sumar(3)
sumar(4, 8)


def multiplesArgumentos(*arg):
    for var in arg:
        print(var, end=" ")


multiplesArgumentos(87, 'ksjhdk', 'khgkgh', 'MANUE', 'GHJHG', 9)


def restar(num1, num2, num3): return num1 - num2 - num3


print(restar(7, 5, 1))
print(restar(98, 54, 12), sep='\n')
