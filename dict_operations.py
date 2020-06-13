cellphone = {
    'marca': 'Xiomi',
    'RAM': 6,
    'almacenamiento': 64,
    'color': 'negro'
}

print('La marca es:', cellphone['marca'])

new_marca = input('Dame el nombre de la nueva marca: ')

#ACTUALIZAR VALOR EN UN DICCIONARIO
cellphone['marca'] = new_marca
print(cellphone)

#AGREGAR UN NUEVO ELEMENTO AL DICCIONARIO
so = input('Cual es el sistema operativo?: ')
cellphone['so'] = so
print(cellphone)

#ELIMINAR UN ELEMENTO DE UN DICCIONARIO
print('ELIMINAMOS COLOR')
del cellphone['color']
print(cellphone)

for clave, valor in cellphone.items():
    print(f'La clave es: {clave}, y su valor es {valor}')


for clave in cellphone.keys():
    print('La clave es: ', clave)

for value in cellphone.values():
    print('El valor es: ', value)