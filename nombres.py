nombres = input('Ingrese los nombres: ')

list_nombres = nombres.split(',')

tuple_nombres = tuple(list_nombres)
print(tuple_nombres)

print('La cantidad de nombres introducidos:', len(tuple_nombres))
print('El valor maximo de la tupla:', max(tuple_nombres))
print('El valor minimo de la tupla:', min(tuple_nombres))