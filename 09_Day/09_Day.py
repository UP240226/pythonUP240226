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
grade = float(input('Enter students score from 0-100: '))
if grade >= 90:
    print('The student have an "A"')
elif grade <= 89 and grade >= 70:
    print('The student have a "B"')
elif grade <= 69 and grade >= 60:
    print('The student have a "C"')
elif grade <= 59 and grade >= 50:
    print('The student have a "D"')
else: 
    print('The student have an "F"')
print("")
#Ejercicio 2
print('Ejercicio 2')
month = input('Enter the month we are in (write it in low case): ')
winter = ['january', 'february', 'dicember']
spring = ['march', 'april', 'may']
summer = ['march', 'april', 'may', 'june', 'july', 'august']
autumn = ['september', 'october', 'november']
if month in winter:
    print('Now is winter')
elif month in spring:
    print('Now is spring')
elif month in summer:
    print('Now is summer')
else:
    print('Now is autumn')
#Ejercicio 3
print('Ejercicio 3')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit in fruits: 
    print('That fruit already exist in the list')
    print(fruits)
if fruit not in fruits:
    fruits.append(fruit)
    print('We add', fruit, 'to the list')
    print(fruits)
print("")

#Exercises: Level 3
print('Exercises: Level 3')
print("")
#Ejercicio 1
print('Ejercico 1')
person={
    'first_name': 'Akinori',
    'last_name': 'Ono',
    'age': 18,
    'married': False,
    'country': 'Mexico',
    'skills': ['Basquet', 'Mathematics', 'Python', 'Minecraft'],
    'address': {'street': 'Hernan Cortes', 'postal code': '20100', 'house color': 'white'}
    }

if 'skills' in person:
   centro = (len(person['skills']))//2
   middle = (person['skills'])[centro]
   print('The skill in the middle of the lis is:', middle)
   print("")
if 'Python' in person['skills']:
    print('Person has Python skills')
    print("")
if person['skills'] is 'JavaScript' and 'React':
    print('He is a fron end developer')
elif person['skills'] is 'Node' and 'Python' and 'MongoDB':
    print('He is a backend developer')
elif person['skills'] is 'React' and 'Node' and 'MongoDB':
    print('He is a fullstack developer')
else:
    print('unknown title')
    print("")
if person['married'] is False and person['country'] is 'Mexico':
    print(person['first_name'], person['last_name'], "isn't married yet.", 'He lives in', person['country'])
    print("")

print("revisado")