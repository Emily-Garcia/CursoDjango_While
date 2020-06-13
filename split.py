text = "Martin_8/9$Juan_5/4/9/8$Francisco_10/10/10/9"

students = text.split('$')
#print(students)

for student in students:
    #print(student)
    info = student.split('_')
    #print(info)
    name = info[0]
    num = info[1]
    numbers = num.split('/')
    sum = 0
    for number in numbers:
        sum = sum + int(number)
    prom = sum / len(numbers)
    print(f'La calificacion final de {name} es {prom}')