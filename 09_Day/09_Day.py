#Ejercicio 1
print('Ejercicio 1')
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive legally')
else:
    rest = (18 - age)
    print('You need', rest, 'more years to get your driver license')
print("")
#Ejercicio 2
print('Ejercicio 2')
my_age = 18
your_age = int(input('Enter your age to compare it to mine: '))
diference = your_age - my_age
if your_age > my_age:
    if diference == 1:
        print('You are', diference, 'year older than me')
    else:
        print('You are', diference, 'years older than me')
elif your_age == my_age:
    print('We are the same age')
else: 
    if diference == -1:
        print('You are', diference * -1, 'year younger than me')
    else:
        print('You are', diference * -1, 'years younguer than me')
print("")
#Ejercicio 3
print('Ejercicio 3')
n1 = float(input('Enter number one: '))
n2 = float(input('Enter number two: '))
if n1 > n2:
    print('Number one is greater than number 2')
elif n1 < n2:
    print('Number one is smaller than number two')
else:
    print('They are equal')
print("")

#Exercises: Level 2
#Ejercicio 1
print('Ejercicio 1')
