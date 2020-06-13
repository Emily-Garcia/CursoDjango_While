usuario = 'S'
nombres = []

while usuario == 'S':
    nombre = input('Ingresa un nombre: ')
    nombres.append(nombre)
    usuario = input('¿Desea seguir agregando nombres? S/N: ')

list_nom = ', '.join(nombres)
print(list_nom)