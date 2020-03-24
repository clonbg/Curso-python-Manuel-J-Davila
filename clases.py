from modulos.persona import Persona

persona1 = Persona()

print('Nombre:', persona1.nombre('Lucas'))
print('Pais:', persona1.pais('España'))
print('Sexo:', persona1.sexo[0])
print('Edad:', persona1.edad(98))
print('Estatura', persona1.estatura(77))
print('Peso:', persona1.peso(3))
