#Ejercicio 1
print('Ejercicio 1')
dog = {}
print(dog)
print("")
#Ejercicio 2
print('Ejercicio 2')
dog = {
    'name': 'Chispa',
    'color': 'black',
    'breed': 'street',
    'legs': 4,
    'age': 12
}
print('Dog dictionary:', dog)
print("")
#Ejercicio 3
print('Ejercicio 3')
student = {
    'first_name': 'Akinori',
    'last_name': 'Ono',
    'gender': 'man',
    'age': 18,
    'marital_status': 'single',
    'skills': ['python', 'java', 'c++'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address': 'Hernan Cortez 105'
}
print('Student dictionary:', student)
print("")
#Ejercicio 4
print('Ejercicio 4')
len_of_student = len(student)    
print('Lenght of dictionary:', len_of_student)
print("")
#Ejercicio 5
print('Ejercicio 5')
skills = student['skills']
print('Values of dictionary:', skills)
print('Type of value:', type(skills))
print("")
#Ejercicio 6
print('Ejercicio 6')
student['skills'].append('html')
print('Updated skills:', student)
print("")
#Ejercicio 7
print('Ejercicio 7')
student.keys()
list = list(student.keys())
print('Keys of dictionary:', list)
print(type(list))
print("")
#Ejercicio 8
print('Ejercicio 8')
student.values()
val_list = list
print('Values of dictionary:', val_list)
print(type(val_list))
print("")
#Ejercicio 9
print('Ejercicio 9')
student.items()
print(student.items())
print(type(student.items()))
print("")
#Ejercicio 10
print('Ejercicio 10')
del student['address']
print('Delete "address" from dictionary student')
print(student)
print("")
#Ejercicio 11
print('Ejercicio 11')
del student
print('Dictionary "Student" deleted')