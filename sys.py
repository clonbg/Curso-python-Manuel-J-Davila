import sys
print(sys.argv)
print(sys.argv[1])

print('Programa multiplique dos números')

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print('El resultado es', (num1*num2))
except ValueError:
    print('Error')
