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
print('Meta in the middle:', it_companies_add)
#Ejercicio 13
it_companies =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Upper case:', it_companies[1].upper())
#Ejercicio 14
print('Join companies with #; :', '#;'.join(it_companies))
#Ejercicio 15
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Facebook and Apple are in the list of Companies?:', 'Facebook' and 'Apple' in it_companies)
#Ejercicio 16
list_2 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
list_2.sort()
print('Alphabetic order of the list:', list_2)
#Ejercicio 17
list_2.reverse()
print('List in reverse alphabetic order:', list_2)
#Ejercicio 18
print('First 3 companies:', it_companies[0:3])
#Ejercicio19
print('Last 3 companies:', it_companies[4:7])
#Ejercicio 20
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle = len(it_companies)//2
it_companies.pop(middle)
print('Remove the middle company: (Apple)', it_companies)
#Ejercicio 21
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
print('Remove the first company: (Facebook)', it_companies)
#Ejercicio 22
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle = len(it_companies)//2
it_companies.pop(middle)
print('Remove the middle company: (Apple)', it_companies)
#Ejercicio 23
it_companies.pop()
print('Remove the last company: (Amazon)', it_companies)
#Ejercicio 24
it_companies.clear()
print('Remove all the companies:', it_companies)
#Ejercicio 25
del it_companies
#Ejercicio 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
join = front_end + back_end
print('front_end:', front_end)
print('back_end:', back_end)
print('Join front_end and back_end:', join)
#Ejercicio 27
full_stack = join
full_stack.append('Python')
full_stack.append('SQL')
print('Full stack:', full_stack)
#Exercises: Level 2
print('Exercises: Level 2')