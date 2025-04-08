#Ejercicio 1
print('Ejercicio 1')
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numFil = [num for num in numbers if num <= 0]
print(numFil)
print("")
#Ejercicio 2
print('Ejercicio 2')
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
listaAplanada = [num for i in list_of_lists for j in i for num in j]
print(listaAplanada)
print("")
#Ejercicio 3
print('Ejercicio 3')
tupleList = [(i, 1, i, i**2, i**3, i**4, i**5)for i in range (11)] 
print(tupleList)
print("")
#Ejercicio 4
print('Ejercicio 4')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista = [i for i in countries for j in i for i in j]
lista = [[i.upper()]for i in lista]
print(lista)
print("")
#Ejercicio 5
print('Ejercicio 5')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dicCountries = [{'country':country.upper(), 'city' : city.upper() } for [(country,city )]in countries]
print(dicCountries)
print()
#Ejercicio 6
print('Ejercicio 6')
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = [''.join(i)for j in names for i in j] 
print(names)
print("")
#Ejercicio 7
print('Ejercicio 7')
slope = lambda x1, y1, x2, y2 :(y2-y1) / (x2-x1)
yIntercept = lambda x1, y1, m: y1 - (m * x1)
m = slope(2,3,5,7)
print(m)
print(yIntercept(2,3,m))
print("")
print("Revisado")