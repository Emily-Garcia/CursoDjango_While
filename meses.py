meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

usuario = 'S'

while usuario == 'S':
    num = int(input('Ingrese el numero del mes que desea visualizar: '))
    if num > 0 and num <= 12:
        print(meses[num-1])
    else:
        print('NUMERO INVALIDO')
    usuario = input('¿Desea visualizar otro mes? S/N: ')
