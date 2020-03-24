def sumar(*arg):
    sumar = 0
    for item in arg:
        suma += item
    return sumar


def restar(*arg):
    restar = arg[0]
    for item in arg[1:]:
        restar -= item
    return restar


def multiplicar(*arg):
    multiplicar = arg[0]
    for item in arg[1:]:
        multiplicar *= item
    return multiplicar


def dividir(num1, num2):
    return num1/num2
