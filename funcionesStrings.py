texto = 'manuel riQUelme'
print(texto.capitalize())
print(texto.lower())
print(texto.upper())
print(len(texto))
lista = texto.split(' ')
print(lista)
apellido = texto.replace("riQUelme", "Riquelme")
print(apellido)
string = 'loco loco loco'
print(string.replace('loco', 'caca', 1))
string = 'Hola nuevo mundo hola'
print(string.count('ola', 0, len(string)))
string = '********Olé***********'
print(string.lstrip('*'))
print(string.rstrip('*'))
string = 'sssjh kjhh jk lkñjahjh h jh  liulijjh'
print(string.find('jh'))
print(string.rfind('jh'))
string = '352345784398576297365978654273846'
print(string.isdigit())
lista = ['uno', 'dos', 'tres']
print('-'.join(lista))
