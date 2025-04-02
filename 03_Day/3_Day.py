#Ejercicio 1
print('Ejercicio 1')
age = int(18)
print(type(age))
#Ejercicio 2
height = float(1.59)
print(type(height))
#Ejercicio 3
complex_number = 3 + 5j
print(type(complex_number))
print("")
#Ejercicio 4
print('Ejercicio 4')
Base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))
areaT = 0.5 * Base * height
print('The area of the triangle is: ', areaT)
print("")
#Ejercicio 5
print('Ejercicio 5')
sidea = float(input('Enter side a of the triangle: '))
sideb = float(input('Enter side b of the triangle: '))
sidec = float(input('Enter the side c ot the triangle: '))
perimeterT = sidea + sideb + sidec 
print('The perimeter is: ', perimeterT)
print("")
#Ejercicio 6 
print('Ejercicio 6')
lenght = float(input('Enter the lenght of a rectangle: '))
width = float(input('Enter the width of a rectangle: '))
areaR = lenght * width
perimeterR = 2*(lenght + width)
print('The area of the rectangle is: ', areaR)
print('The perimeter of the rectangle is: ', perimeterR)
print("")
#Ejercicio 7
print('Ejercicio 7')
radius = float(input('Enter the radius of a circle: '))
areaC = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print('The area of the circle is: ', areaC)
print('The circumference of the circle is: ', circumference)
print("")
#Ejercicio 8
print('Ejercicio 8')
#slopeEj8
x = float(input('Enter the x: '))
y = float(input('Enter the y: '))
yT = 2 * x - 2
xT = (y - 2) / 2
m1 = (yT / (-xT))
print('The slope is: ', m1)
print("")
#Ejercicio 9
print('Ejercicio 9')
#slopeEj9
#x1 = float(input('Enter the x1: '))
#x2 = float(input('Enter the x2: '))
#y1 = float(input('Enter the y1: '))
#y2 = float(input('Enter the y2: ')) 
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m2 = y2 - y1 / x2 - x1
print('The slope is: ', m2)
print("")
#Ejercicio 10
print('Ejercicio 10')
mT = m1 == m2
print('The slope in Ejercicio 8 is equal to the slope in Ejercicio 9 ?: ', mT)
mT = m1 != m2
print('The slope in Ejercicio 8 is different than the slope in Ejercicio 9 ?: ', mT)
mT = m1 > m2
print('The slope in Ejercicio 8 is greater than the slope in Ejercicio 9 ?: ', mT)
print("")
#Ejercicio 11
print('Ejercicio 11')
x = float(input('Enter the x: '))
y = x ** 2 + 6 * x + 9
# x = -3
# y = 0
print('The value of y is: ', y)
print("")
#Ejercicio 12
print('Ejercicio 12')
print('Python lenght is equal to Dragon lenght ?: ', len('python') == len('dragon'))
print('Python lenght is different to Dragon lenght ?: ', len('python') != len('dragon'))
print("")
#Ejercicio 13 
print('Ejercicio 13')
print('The letters "on" are in python ?: ', 'on' in 'python')
print('The leters "on" are in dragon ?: ', 'on' in 'dragon')
print("")
#Ejercicio 14
print('Ejercicio 14')
print('In the frase "I hope this course is not full of jargon" there is jargon in it ?: ', 'jargon' in 'I hope this course is not full of jargon')
print("")
#Ejercicio 15
print('Ejercicio 15')
print('The letters "on" are not in python ?: ', 'on' not in 'python')
print('The leters "on" are not in dragon ?: ', 'on' not in 'dragon')
print("")
#Ejercicio 16
print('Ejercicio 16')
len1 = str(len('python'))
print('The lenght of the word python is: ', len1)
print(type(len1))
print("")
#Ejercicio 17
print('Ejercicio 17')
num = float(input('Give me a number and I will tell you if it is even or odd: '))
if num % 2 == 0:
    print('The number is even ', num)
else:
    print('The number is odd ', num)
print('Two is an even number ?: ', 2 % 2 == 0)
print('Three is an even number ?: ', 3 % 2 == 0)
print("")
#Ejercicio 18
print('Ejercicio 18')
fd = int(7 // 3)
r = (fd == int(2.7))
print('The floor division of 7 and 3 is: ', fd)
print('The floor division of 7 and 3 is equal to 2.7 ?: ', r)
print("")
#Ejercicio 19
print('Ejercicio 19')
print("type '10' is equal to type 10 ?: ", type('10') == type(10))
print("")
#Ejercicio 20
print('Ejercicio 20')
print("type int('9.8') is equal to 10 ?: ", int(9.8) == 10)
print("")
#Ejercicio 21
print('Ejercicio 21')
h = float(input('Enter the hours you work per week: '))
rph = float(input('Enter the rate per hour per week: '))
pay = h * rph
print('Your weekly earning is: ', pay)
print("")
#Ejercicio 22
print('Ejercicio 22')
age = int(input('Enter the numbers of years you have lived: '))
years = 100 - age
sec = years * 365 * 24 * 60 * 60
print('You have ', sec, ' seconds left to have 100 years')
print("")
#Ejercicio 23
print('Ejercicio 23')
one = 1
two = 2
three = 3
four = 4
five = 5
res1 = one * 1
res11 = one * res1
res111 = res1 * res11
res2 = two * 1
res22 = two * res2
res222 = res2 * res22
res3 = three * 1
res33 = three * res3
res333 = res3 * res33
res4 = four * 1
res44 = four * res4
res444 = res4 * res44
res5 = five * 1
res55 = five * res5
res555 = res5 * res55
print(one, ' ', 1, ' ', res1, ' ', res11, ' ', res111)
print(two, ' ', 1, ' ', res2, ' ', res22, ' ', res222) 
print(three, ' ', 1, ' ', res3, ' ', res33, ' ', res333)
print(four, ' ', 1, ' ', res4, ' ', res44, ' ', res444)
print(five, ' ', 1, ' ', res5, ' ', res55, ' ', res555)
print("")

print("revisado")