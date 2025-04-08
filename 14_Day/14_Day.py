#Exercises: Level 1
print('Exercises: Level 1')
print("")
#Ejercicio 1
print('Ejercicio 1')
print('La funcion map toma una funcion y un iterable como parametros, la funcion filter filtra los elementos que cumplen con el criterio de filtrado establecido y reduccion funciona igual que map y filter pero no devuelve un iterabele  si no un unico valor.')
print("")
#Ejercicio 2
print('Ejercicio 2')
print('Las funciones de orden superior permiten tomar funciones como parametros y sel resultado que devuelva puede ser otra funcion un cierre es una funcion anidada dentro de una funcion que es encapsulada y luego devolviendo la funcion anidada y un decorador permite al usuario añadir nuevas funciones a un objeto existente sin modificar su estructura')
print("")
#Ejercicio 3
print('Ejercicio 3') 
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']
def suma (x,y):
    return int(x) + int(y)
total = reduce(suma,numbers_str)
print(total)
print("")
#Ejercicio 4
print('Ejercicio 4')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for countrie in countries:
    print(countrie)
print("")
#Ejercicio 5
print('Ejercicio 5')
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)
print("")
#Ejericio 6
print('Ejercicio 6')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)
print("")

#Exercises: Level 2
print('Exercises: Level 2')
print("")
#Ejercicio 1
print('Ejercicio 1')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def ChangeUpper (countrie):
    return countrie.upper ()
rest = map(ChangeUpper,countries)
print(list(rest))
print("")
#Ejercicio 2
print('Ejercicio 2')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def cuadrado (n):
    return n ** 2
rest = map(cuadrado,numbers)
print(list(rest))
print("")
#Ejercicio 3
print('Ejercicio 3')
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def changeUpperNames (name):
    return name.upper()
rest =map(changeUpperNames,names)
print(list(rest))
print("")
#Ejercicio 4
print('Ejercicio 4')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def onlyLand (countrie):
    if 'land' in countrie:
        return True
    return False
rest = filter(onlyLand,countries)
print(list(rest))
print("")
#Ejercicio 5
print('Ejercicio 5')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def sixChart(countrie):
    if len(countrie) == 6:
        return True
    return False
rest = filter(sixChart,countries)
print(list(rest))
print("")
#Ejercicio 6
print('Ejercicio 6')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def sixOrMoreCharst (countrie):
    if len(countrie) >=6:
        return True
    return False
rest = filter(sixOrMoreCharst,countries)
print(list(rest))
print("")
#Ejercicio 7
print('Ejercicio 7')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def starWhitE (countrie):
    return countrie.startswith("E")
rest = filter(starWhitE,countries)
print(list(rest))
print("")
#Ejercicio 8
print('Ejercicio 8')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = reduce(
    lambda x, y: x + y,map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(resultado)
print("")
#Ejercicio 9
print('Ejercicio 9')
lista = [1,2,3,'hola','mundo','phyton',4,5,6,7,8,9,10]
def getSrtingsList(list):
    return [item for item in list if isinstance(item, str)]
rest = getSrtingsList(lista)
print(rest)
print("")
#Ejercicio 10
print('Ejercicio 10')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def addNumbers (x,y):
    return int(x) + int (y)
total = reduce(addNumbers,numbers)
print(total)
print("")
#Ejercicio 11
print('Ejercicio 11')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def paisOracion (x,y):
    return x + ', ' + y
oracion = reduce(paisOracion,countries)
oracion1 = oracion + 'son paises de europa'
print(oracion1)
print("")

print("Revisado")