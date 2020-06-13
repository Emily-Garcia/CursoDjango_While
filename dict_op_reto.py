usuario = 'S'

paises = {}

while usuario == 'S':
    pais = input('Ingresa el nombre del pais: ')
    personas = int(input('Ingresa el numero de personas (millones): '))

    paises[pais] = personas

    usuario = input('Desea seguir ingresando paises? S/N: ')
#print(paises)

print('--- DICCIONARIO PAISES ---')
for dict_pais, dict_pers in paises.items():
    print(f'{dict_pais} : {dict_pers} millones de personas')

nom_pais = input('Ingresa el nombre del pais que quieras saber su cantidad de personas: ')

print(f'La cantidad de personas que tiene {nom_pais} es {paises[nom_pais]} millones de personas')