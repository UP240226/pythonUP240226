#Exercises: Level 1
#Ejercicio 1
print('Ejercicio 1')
tpl = ()
print(tpl)
print("")
#Ejercicio 2
print('Ejercicio 2')
tuplesister = 'Naomi', 'Alexa', 'Sofia'
tuplebrother = 'Satoshi', 'Marco', 'Jorge'
print("")
#Ejercicio 3
print('Ejercicio 3')
siblings = (tuplesister) + (tuplebrother)
print('Siblings:', siblings)
print("")
#Ejercicio 4
print('Ejercicio 4')
lensib = len(siblings)
print('How many siblings do you have:', lensib)
print("")
#Ejercicio 5
print('Ejercicio 5')
parents = 'Victor', 'Elizabeth'
family_members = siblings + parents
print('Family members:', family_members)
print("")
#Exercises: Level 2
print('Exercises: Level 2')
print("")
#Ejercicio 1
print('Ejercicio 1')
tuplesister = list(tuplesister)
tuplebrother = list(tuplebrother)
parents = list(parents)
family_members = list(family_members)
parents = family_members[-2:]
print('Parents:', parents)
print('Siblings:', family_members[:-2])
print("")
#Ejercicio 2
print('Ejercicio 2')
tplfruts = ('apple', 'banana', 'cherry')
tplvegtables = ('tomato', 'potato', 'onion')
tplanimal_prod = ('meat', 'milk', 'eggs')
food_stuff_tp = tplfruts + tplvegtables + tplanimal_prod
tuple(food_stuff_tp)
print('Food stuff tuple:', food_stuff_tp)
print(type(food_stuff_tp))
print("")
#Ejercicio 3
print('Ejercicio 3')
food_stuff_lt = list(food_stuff_tp)
print('Food stuff list:', food_stuff_lt)
print(type(food_stuff_lt))
print("")
#Ejercicio 4
print('Ejercicio 4')
centro = len(food_stuff_lt)//2
middle = food_stuff_lt[centro]
print('Center of the list:', middle)
print("")
#Ejercicio 5
print('Ejercicio 5')
food_stuff_lt = ['apple', 'banana', 'cherry', 'tomato', 'potato', 'onion', 'meat', 'milk', 'eggs']
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print('The First three items are:', first_three)
print('The Last three items are:', last_three)
print("")
#Ejercicio 6
print('Ejercicio 6')
del food_stuff_lt[0:len(food_stuff_lt)]
print('The tuple list of food is:', food_stuff_lt)
print("")
#Ejercicio 7
print('Ejercicio 7')
paisesnordicos = ('Norway', 'Sweden', 'Denmark', 'Finland', 'Iceland', 'Estonia', 'Latvia', 'Lithuania')
print('Paises Nordicos', paisesnordicos)
print('Estonia esta en la lista?:', 'Estonia' in paisesnordicos)
print('Iceland esta en la lista?:', 'Iceland' in paisesnordicos)
print("")