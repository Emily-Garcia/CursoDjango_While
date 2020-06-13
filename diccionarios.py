nombre = input('Ingresa el nombre: ')
apellidos = input('Ingresa los apellidos: ')
edad = int(input('Ingresa la edad: '))
correo = input('Ingresa el correo: ')

datos = {
    'nombre' : nombre,
    'apellidos' : apellidos,
    'edad' : edad,
    'correo' : correo
}

print(f'Hola! Mi nombre es {datos["nombre"]} {datos["apellidos"]}, tengo {datos["edad"]} años y mi correo electronico es {datos["correo"]}')