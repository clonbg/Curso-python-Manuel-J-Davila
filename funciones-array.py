diccionario={'uno':1,'dos':2,'tres':3}
print(len(diccionario))
lista=['uno','dos']
lista.append('tres')
print(lista)
lista.insert(0,'cero')
print(lista)
lista.pop(2)
print(lista)
print(lista.index('uno'))

tuples=('Hola','mundo','python')
print(tuples.index('mundo'))

lista.remove('tres')
print(lista)

tuples=('uno','uno','dos')
print(tuples.count('uno'))