#Exercises: Level 1
print('Exercises: Level 1')
print("")
#Ejercicio 1
print('Ejercicio 1')
import random
import string
def randomUserId ():
    return ''.join(random.choices(string.ascii_letters + string.digits, k= 6))
print('Este es su usuario ', randomUserId())
print("")
#Ejercico 2
print('Ejercicio 2')
def userIdGenByUser ():
    numCar = int(input('Enter the caracters number: '))
    numIds = int(input('Enter the ids number: '))
    Ids = [
        ''.join(random.choices(string.ascii_letters + string.digits, k= numCar))
        for _ in range(numIds)
    ]
    return Ids
print(userIdGenByUser())
print("")
#Ejercicio 3
print('Ejercicio 3')
def genRgbColor ():
    rojo = random.randint(0,255)
    azul = random.randint(0,255)
    verde = random.randint(0,255)
    return(rojo,azul,verde)
print(genRgbColor)
print("")

#Exercises: Level 2
print('Exercises: Level 2')
print("")
#Ejercicio 1
print('Ejercicio 1')
def listOfHexaColors (n):
    hexaColor = []
    for j in range(5):
     for _ in range (n):
        color = '#'+ ''.join(random.choices('0123456789ABCDEF',k=6))
        hexaColor.append(color)
     return hexaColor
print(listOfHexaColors(5))
print("")
#Ejercicio 2
print('Ejercicio 2')
def listOfRgbColors (n):
   return[(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(n)]

print(listOfRgbColors(5))
print("")
#Ejercicio 3
print('Ejercico 3')
def generateColors(n, format='hex'):
    
    colors = []
    for _ in range(n):
        if format == 'hex':
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        else: 
            format == 'rgb'
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colors.append(color)
    
    return colors
print(generateColors(3,'hex'))
print("")

#Exercises: Level 3
print('Exercises: Level 3')
print("")
#Ejercicio 1
print('Ejercicio 1')
def shuffleList(list):
    shuffle = list[:]
    random.shuffle(shuffle)
    return shuffle
print(shuffleList([1,2,3,4,5]))
print("")
#Ejercicio 2
print('Ejercicio 2')
def uniqueNumbers ():
    return random.sample(range(10),7)
print(uniqueNumbers())
print("")

print("Revisado")