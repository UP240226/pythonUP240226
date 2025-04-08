#Exercises: Level 1
print('Exercises: Level 1')
print("")
#Ejercicio 1
print('Ejercicio 1')
def add_two_numbers ():
    c = 3
    b = 4
    a = b + c
    print(a)
add_two_numbers()
print("")
#Ejercicio 2
print('Ejercicio 2')
def areaCirculo ():
    radio = 25
    pi = 3.1415
    area = pi * radio * radio
    print(area)
areaCirculo ()
print("")
#Ejercicio 3
print('Ejercicio 3')
def addAllNums (*args):
    if all ( isinstance(arg,(int, float )) for arg in args ):
        return sum(args)
    else:
        return print('Todos los resultados deben de ser numeros')
    
conjunto = [1,2,3]
res = addAllNums(*conjunto)
print(res)
print("")
#Ejercicio 4 
print('Ejercicio 4')
def convertCel_Fah():
    celcius = float(input('Enter the temperature in Celsious: '))
    farenheit = celcius * 1.8 + 32
    print('The temperature is:', farenheit, 'in Fahrenheit')
convertCel_Fah()
print("")
#Ejercicio 5
print('Ejercicio 5')
def checkSeason ():
    mes = input('Inserte el mes: ')
    if mes in ['Septiembre','Octubre','Noviembre']:
        print('Es otoño')
    elif mes in ['Diciembre','Enero','Febrero']:
        print('Es invierno')
    elif mes in ['Marzo','Abril','Mayo']:
        print('Es primavera')
    else:
        print('Es verano')
checkSeason ()
print("")
#Ejercicio 6
print('Ejercicio 6')
def calculateSlope (x1,y1,x2,y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
pendiente = calculateSlope (1,2,3,6)
print ('La pendiente es:', pendiente)
print("")
#Ejercicio 7
print('Ejercicio 7')
def quadEq (a,b,c):
    if a == 0 :
        return
    dis = b**2 - 4*a*c
    if dis > 0 :
        x1=(-b+dis**0.5)/(2*a)
        x2=(-b-dis**0.5)/(2*a)
        return x1,x2
    elif dis == 0:
        x = -b/(2*a)
        return x
    else :
        return 'No tiene solucion'
Education = quadEq (a = 2, b = 3, c = 7)
print ('La solucion es :', Education)
print("")
#Ejercicio 8
print('Ejercicio 8')
def printList (list):
    for i in list:
        print(i)
list = [1,2,4,3,5,6,7,8,9]
steList = set(list)
print(steList)
print("")
#Ejercicio 9
print('Ejercicio 9')
def reverseList (lista):
    listaIn=[]
    for i in range(len(lista)-1,-1,-1):
        listaIn.append(lista[i])
    return listaIn
lst = reverseList(lista=[4,7,3,9,5])
print(lst)
print("")
#Ejercicio 10
print('Ejercicio 10')
def capitalizeListItems (items):
    return [item.upper() for item in items]
List = ['q','d','d']
listM =capitalizeListItems(List)
print(List)
print(listM)
print("")
#Ejercicio 11
print('Ejercicio 11')
def addItem (lista,elemento):
    lista.append(elemento)
    return lista
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(addItem(food_staff,'Meat'))
print("")
#Ejercicio 12
print('Ejercicio 12')
def removeItem (lista,elemento):
    lista.remove(elemento)
    return lista 
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(removeItem(food_staff, 'Mango'))
print("")
#Ejercicio 13
print('Ejercicio 13')
def sumaNumeros(num):
    suma=0
    for i in range(1,num+1):
        suma=suma+i
    return suma
print(sumaNumeros(num=5))
print("")
#Ejercicio 14
print('Ejercicio 14')
def sumaImpares(num):
    suma=0
    for i in range(1,num+1,2):
        suma=suma+i
    return suma
print(sumaImpares(num=7))
print("")
#Ejercicio 15
print('Ejercicio 15')
def sumaPares(num):
    suma=0
    for i in range(0,num+1,2):
        suma=suma+i
    return suma
print(sumaPares(num=5))
print("")

#Exercises: Level 2
print('Exercises: Level 2')
print("")
#Ejercicio 1
print('Ejercicio 1')
def evensAndOdds (num) :
    impar = 0
    par = 0
    for i in range (1,num +1):
        if i % 2 == 0:
            par = par +1
        else :
            impar = impar + 1
    return par, impar 
print(evensAndOdds(num = 100))
print("")
#Ejercicio 2
print('Ejercicio 2')
def factorial (num) :
    fac = 1
    for i in range (1,num + 1):
        fac = fac*i
        return fac
print(factorial(num = 7))
print("")
#Ejercicio 3
print('Ejercicio 3')
def isEmpty (cosa):
    if len(cosa) == 0:
        return True
    else :
        return False
    
print (isEmpty(cosa = []))
print("")
#Ejercicio 4
print('Ejercicio 4')
def media(lista):
    return sum(lista)/len(lista)
print(media(lista=[1,2,3,4,5]))
print("")

#Exercises: Level 3
print('Exercises: Level 3')
print("")
#Ejercicio 1
print('Ejercicio 1')
def isPrime (n):
    if n <=1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
print(isPrime(n = 13))
print("")
#Ejercicio 2
print('Ejercicio 2')
def allUnique (list):
    return len(list) == len(set(list))
print(allUnique([1,3,4,6,6]))
print("")
#Ejercicio 3
print('Ejercicio 3')
def sameType (list):
    return all(isinstance(list[0],type(elemento)) for elemento in list)
print(sameType([1,2,3,4]))
print("")
#Ejercicio 4
print('Ejercicio 4')
def isPythonVariable(variable):
    if variable.isidentifier():
        return True
    else:
        return False
print(isPythonVariable(variable='variable1'))
print("")
#Ejercicio 5
print('Ejercicio 5')
from listas import listaPaises as crty

countryLen = []
def masHablados ():
    for pais in crty:
        for lenguaje in pais ['languages']:
            countryLen.append(lenguaje)

    setLen = set(countryLen)
    dicLen = {}

    for lenguaje in setLen :
        dicLen[lenguaje] = 0
    for idioma in dicLen:
        for pais in crty:
            if idioma in pais ['languages']:
                dicLen [idioma] = pais ['population'] + dicLen[idioma]
    sortValLenPopu = sorted(dicLen.values(),reverse= True)
    sortKeyLenPopu = sorted(dicLen,key=dicLen.get,reverse= True)
    return sortKeyLenPopu [:10],sortValLenPopu [:10]
print(masHablados())

def paisesMasP():
    dicPobla = {}
    for pais in crty:
        dicPobla[pais['name']] = pais['population']
    sortValPopu = sorted(dicPobla.values(),reverse=True)
    sortKeyPopu = sorted(dicPobla,key=dicPobla.get,reverse=True)
    return sortKeyPopu[:10], sortValPopu[:10]
print(paisesMasP)
print("Revisado")