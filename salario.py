selection = 'S'
while selection == 'S':
    nombre = input('Ingresa el nombre del trabajador: ')
    salario = float(input('Ingresa el salario del trabajador: '))
    
    sal_bruto = salario - (salario * 0.16)

    print('El salario bruto de', nombre ,' es:', sal_bruto)

    selection = input('¿Desea colcer a calcular el salario de otra persona? S/N: ')

print('Hasta la proximaaaaa xd')
