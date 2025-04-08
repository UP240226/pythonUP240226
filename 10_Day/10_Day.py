#Exercises: Level 1
print('Exercises: Level 1')
print("")
#Ejercico 1
print('Ejercicio 1')
print('For')
for number in range(0,11):
    print(number)
print("")
print('While')
count = 0
while count < 11:
    print(count)
    count = count + 1 
print("")
#Ejercicio 2
print('Ejercicio 2')
print('For')
for number in range(10,0,-1):
    print(number)
print("")
print('While')
count = 10
while count > 0:
    print(count)
    count = count - 1 
print("")
#Ejercicio 3
print('Ejercico 3')
count = '#'
while count < '########':
    print(count)
    count = count + '#'
print("")
#Ejercicio 4
print('Ejercicio 4')
rows = ('# # # # # # # #')
for i in range(8):
    print(rows)
print("")
#Ejercicio 5
print('Ejercicio 5')
for pattern in range(0,11):
    print(pattern, 'x', pattern, '=', pattern * pattern)
    pattern = (pattern + 1) * (pattern + 1)
    print("")
#Ejercicio 6
print('Ejercicio 6')
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for items in list:
    print(items)
print("")
#Ejercicio 7
print('Ejercico 7')
for even in range(0,101,2):
    print(even)
print("")
#Ejercicio 8
print('Ejercicio 8')
for odd in range(2,101,2):
    print(odd - 1)
print("")

#Exercises: Level 2
print('Exercises: Level 2')
print("")
#Ejercicio 1
print('Ejercicio 1')
sum = 0
for i in range(101):
    sum = sum + i
print("El resultado de la suma de TODOS los numeros del 0 al 100 es: ", sum)
print("")
#Ejercicio 2
print('Ejercicio 2')
print('Evens')
sumapar = 0
for i in range(101):
    if i % 2 == 0:
        sumapar = sumapar + i
print("El resultado de la suma de los pares es:", sumapar)
print("")
print('Odds')
sumaImpar = 0
for i in range(101):
    if i % 2 == 1:
        sumaImpar = sumaImpar + i
print("El resultado de la suma de impares es:", sumaImpar)
print("")


#Exercises: Level 3
print('Exercises: Level 3')
print("")
#Ejercico 1
print('Ejercicio 1')
import paises as p
countries = p.countriesList

for pais in countries:
    if 'land' in pais:
        print(pais)
    
print("")
#Ejercicio 2
print('Ejercicio 2')
list = ['banana', 'orange', 'mango', 'lemon']
print(list)
list.reverse()
print(list)
print("")
#Ejercicio 3
print('Ejercicio 3')
print("")
#Ejercicio i
print('i.')

from listas import listaPaises as paises
listaIdiomas = []
for pais in paises:
    for language in pais['languages']:
        listaIdiomas.append(language)

idiomasUnicos = set(listaIdiomas)
sortedIdiomas = sorted(idiomasUnicos)
print('Total numbers of languages:', len(idiomasUnicos))
print("")
#Ejercicio ii
print('ii')

dicHablantes = {}
for language in idiomasUnicos:
    dicHablantes[language] = 0

print(dicHablantes)

for idioma in dicHablantes:
        for pais in paises:
            if idioma is pais['languages']:
                dicHablantes[idioma] = pais['population'] + dicHablantes[language]

ordenados = sorted(dicHablantes.values(), reverse=True)
ordenadosKeys = sorted(dicHablantes, key=dicHablantes.get, reverse=True)

print(ordenadosKeys[1], ordenados[1])
print("")
#Ejercicio iii
print('Ejercicio iii')

for i in range(10):
    print(ordenadosKeys[i], ordenados[i])
print("")
print("Revisado")