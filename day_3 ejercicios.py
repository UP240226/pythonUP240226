edad = 18
estatura = 1.59
numero_complejo = 3 + 5j
print(type(edad))
print(type(estatura))
print(type(numero_complejo))

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle:"))
area = .5 * base * height
print("The area of the riangle is:")
print(area)

a = float(input("Enter the side a of the triangle: "))
b = float(input("Enter the side b of the triangle: "))     
c = float(input("Enter the side c of the triangle: "))
perimeter = a + b + c
print("The perimeter of the triangle is: ")
print(perimeter)

lenght = float(input("Dame el largo del rectángulo: "))
width = float(input("Dame el ancho del rectángulo: "))
area = lenght * width
perimeter = 2 * (lenght + width)
print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimeter)

radius = float(input("Dame el radio del circulo: "))
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius   
print("El área del circulo es: ", area)
print("La circunferencia del circulo es: ", circumference)

