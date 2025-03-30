#Exercises: Level 1
print('Exercises: Level 1')
print("")
#Ejercicio 1
print('Ejercicio 1')
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)
print('Companies:', it_companies)
print('Number of companies:', len(it_companies))
print("")
#Ejercicio 2
print('Ejercicio 2')
it_companies.add('Twitter')
print('Add Twitter', it_companies)
print("")
#Ejercicio 3
print('Ejercicio 3')
it_companies.update(['Tesla', 'SpaceX', 'IBM'])
print('More Compaies', it_companies)
print("")
#Ejercicio 4
print('Ejercicio 4')
it_companies.remove('IBM')
print('Remove IBM', it_companies)
print("")
#Ejercicio 5
print('Ejercicio 5')
it_companies.discard('SpaceX')
print('Discard SpaceX', it_companies)
print('The diference between remove and discard is that remove will raise an error if the item does not exist in the set, while discard will not raise an error')
print("")

#Exercises: Level 2
print('Exercises: Level 2')
print("")
#Ejercicio 1
print('Ejercicio 1')
A = {19, 22, 24, 20, 25, 26}
B = {18, 17, 24, 22, 23, 27}
print('A:', A)
print('B:', B)
A.union(B)
print('Union:', A.union(B))
print("")
#Ejercicio 2
print('Ejercicio 2')
find = A.intersection(B)
print('Intersection:', find)
print("")
#Ejercicio 3
print('Ejercicio 3')
subset = A.issubset(B)
print('Is A subset of B?:', subset)
print("")
#Ejercicio 4
print('Ejercicio 4')
disjoint = A.isdisjoint(B)
print('Are A and B disjoint?:', disjoint)
print("")
#Ejercicio 5
print('Ejercicio 5')
join = A.union(B)
inv = B.union(A)
print('Join:', join)
print('Inverse:', inv)
print("")
#Ejercicio 6
print('Ejercicio 6')
A.symmetric_difference(B)
print('Symmetric Difference:', A.symmetric_difference(B))
print("")
#Ejercicio 7
print('Ejercicio 7')
del A
del B
print('Del A:')
print('Del B:')
print("")

#Exercises: Level 3
print('Exercises: Level 3')
print("")
#Ejercicio 1
print('Ejercicio 1')
ages = [18, 45, 15, 23, 44, 32, 22, 19, 24, 25, 26, 24, 25, 24]
set_ages = set(ages)
print(set_ages)
list = len(ages)
st = len(set_ages)
print('Lenght list', list)
print('Lenght set', st)
print("")
#Ejercicio 2
print('Ejercicio 2')
print('An string is')
print('A list is')
print('A tuple is')
print('A set is')
print("")
#Ejercicio 3
print('Ejercicio 3')
sentence = 'I am a teacher and I love to inspire and teach people'
palabras = sentence.split()
print(palabras)
uniqueValues = set(palabras)
print(uniqueValues)
print("")