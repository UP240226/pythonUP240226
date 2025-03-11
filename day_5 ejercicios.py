#Ejercicio 1
empty_list = list()
print('Empty list', empty_list)
#Ejercicio 2
list_1 = [1, 2, 3, 4, 5]
print('5 item list', list_1)
#Ejercicio 3
len_list_1 = len(list_1)
print('The lenght of the list is', len_list_1, 'items.')
#Ejercicio 4
list = list_1 [0:5:2]
print('First, middle and last item:', list)
#Ejercicio 5
mixed_data_types = ('Akinori', '18 years old', '1.59 m tall', 'single', 'Los Vergeles, AGS.')
print('Personal info list:', mixed_data_types)
#Ejercicio 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#Ejercicio 7
print('The list of companys is:', it_companies)
#Ejercicio 8
num_companies = len(it_companies)
print('Number of companies:', num_companies)
#Ejercicio 9
comp = it_companies [0:7:3]
print('First, middle and last item:', comp)
#Ejercicio 10
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[3] = 'Samsung'
print('Modify list:', it_companies)
#Ejercico 11
it_companies_add = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_add.append('Meta')
print('Extra item:',it_companies_add)
#Ejercicio 12
it_companies_add.pop()
middle = 'Meta'
centro = int(len(it_companies_add)/2)
it_companies_add.insert(centro,middle)
print(it_companies_add)
#Ejercicio 13
upper = it_companies.upper()
print(upper)