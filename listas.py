lista = ['MX', 'US', 'UK', 'MX', 'MX', 'US', 'UK', 'FR', 'CH', 'CH']

lista.append('JP')
print(lista)
print('-------------------')

print(lista.count('MX'))
print('-------------------')

print(lista.index('UK'))
print('-------------------')

copia = lista.copy()
print(copia)
print('-------------------')

copia.extend(['COL', 'ARG', 'BR'])
print(copia)
print('-------------------')

copia.remove('CH')
print(copia)
print('-------------------')