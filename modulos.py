
import modulos.matematicas as mates  # Acceder a los modulos a través de un alias
from modulos.matematicas import *  # Acceder directamente a los modulos
# Acceder directamente a un modulo y ponerle alias
from modulos.matematicas import dividir as div

print(mates.sumar(5, 8, 7, 8, 9, 95))


print(sumar(56, 587, 154, 256, 999, 124*8))


print(div(87, 54))
