#Exercise Level 1
#'Day 2:30 Days of python programming'

first_name = 'Akinori'
last_name = 'Ono'
full_name = first_name + ' ' + last_name
country = 'Mexico'
city = 'Aguascalientes'
age = 18
year = 2025
is_married = False
is_true = True
is_light_on = False
print(first_name, last_name, country, city, age, year, ',', 'Is married?', is_married, ',', 'Is light on?', is_light_on)

#Exercise Level 2

type(first_name)
len(first_name) / len(last_name)

num_one = float(input('Enter the first number: '))
num_two = float(input('Enter the second number: '))
varable_total = num_one + num_two
variable_diff = num_one - num_two
variable_product = num_one * num_two
variable_division = num_one / num_two
variable_remainder = num_one % num_two
variable_exp = num_one ** num_two
variable_floor_division = num_one // num_two
print('Suma',varable_total,',','Resta',variable_diff,',', 'Multiplicación',variable_product,',', 'División',variable_division,',', 'Porcentaje',variable_remainder,',', 'Exponencial',variable_exp,',', 'Cociente',variable_floor_division)

#circulo
radius = float(input("Enter the radius of the circle: ")) 
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print("Area of the Circle", area_of_circle)