from modulos.deportista import Deportista

deportista = Deportista()


print('Nombre:', deportista.nombre('Lucas'))
print('Pais:', deportista.pais('España'))
print('Sexo:', deportista.sexo[0])
print('Edad:', deportista.edad(98))
print('Estatura', deportista.estatura(77))
print('Peso:', deportista.peso(3))
print('Deporte:', deportista.deporte('Atletismo'))
print(deportista.detener())
print(deportista.correr())
print(deportista.saltar())
