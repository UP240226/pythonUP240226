#Ejercicio 1
print('Ejercicio 1')
empty_list = list()
print('Empty list', empty_list)
print("")
#Ejercicio 2
print('Ejercicio 2')
list_1 = [1, 2, 3, 4, 5]
print('5 item list', list_1)
print("")
#Ejercicio 3
print('Ejercicio 3')
len_list_1 = len(list_1)
print('The lenght of the list is', len_list_1, 'items.')
print("")
#Ejercicio 4
print('Ejercicio 4')
list = list_1 [0:5:2]
print('First, middle and last item:', list)
print("")
#Ejercicio 5
print('Ejercicio 5')
mixed_data_types = ('Akinori', '18 years old', '1.59 m tall', 'single', 'Los Vergeles, AGS.')
print('Personal info list:', mixed_data_types)
print("")
#Ejercicio 6
print('Ejercicio 6')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("")
#Ejercicio 7
print('Ejercicio 7')
print('The list of companys is:', it_companies)
print("")
#Ejercicio 8
print('Ejercicio 8')
num_companies = len(it_companies)
print('Number of companies:', num_companies)
print("")
#Ejercicio 9
print('Ejercicio 9')   
comp = it_companies [0:7:3]
print('First, middle and last item:', comp)
print("")
#Ejercicio 10
print('Ejercicio 10')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[3] = 'Samsung'
print('Modify list:', it_companies)
print("")
#Ejercico 11
print('Ejercicio 11')
it_companies_add = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_add.append('Meta')
print('Extra item:',it_companies_add)
print("")
#Ejercicio 12
print('Ejercicio 12')
it_companies_add.pop()
middle = 'Meta'
centro = int(len(it_companies_add)/2)
it_companies_add.insert(centro,middle)
print('Meta in the middle:', it_companies_add)
print("")
#Ejercicio 13
print('Ejercicio 13')
it_companies =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Upper case:', it_companies[1].upper())
print("")
#Ejercicio 14
print('Ejercicio 14')
print('Join companies with #; :', '#;'.join(it_companies))
print("")
#Ejercicio 15
print('Ejercicio 15')  
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Facebook and Apple are in the list of Companies?:', 'Facebook' and 'Apple' in it_companies)
print("")
#Ejercicio 16
print('Ejercicio 16')
list_2 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
list_2.sort()
print('Alphabetic order of the list:', list_2)
print("")
#Ejercicio 17
print('Ejercicio 17')
list_2.reverse()
print('List in reverse alphabetic order:', list_2)
print("")
#Ejercicio 18
print('Ejercicio 18')
print('First 3 companies:', it_companies[0:3])
print("")
#Ejercicio19
print('Ejercicio 19')
print('Last 3 companies:', it_companies[4:7])
print("")
#Ejercicio 20
print('Ejercicio 20')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle = len(it_companies)//2
it_companies.pop(middle)
print('Remove the middle company: (Apple)', it_companies)
print("")
#Ejercicio 21
print('Ejercicio 21')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
print('Remove the first company: (Facebook)', it_companies)
print("")
#Ejercicio 22
print('Ejercicio 22')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle = len(it_companies)//2
it_companies.pop(middle)
print('Remove the middle company: (Apple)', it_companies)
print("")
#Ejercicio 23
print('Ejercicio 23')
it_companies.pop()
print('Remove the last company: (Amazon)', it_companies)
print("")
#Ejercicio 24
print('Ejercicio 24')
it_companies.clear()
print('Remove all the companies:', it_companies)
print("")
#Ejercicio 25
print('Ejercicio 25')
del it_companies
print("")
#Ejercicio 26
print('Ejercicio 26')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
join = front_end + back_end
print('front_end:', front_end)
print('back_end:', back_end)
print('Join front_end and back_end:', join)
print("")
#Ejercicio 27
print('Ejercicio 27')
full_stack = join
full_stack.append('Python')
full_stack.append('SQL')
print('Full stack:', full_stack)
print("")
#Exercises: Level 2
print('Exercises: Level 2')
print("")
#Ejercicio 1
print('Ejercicio 1')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print('Ages list:', ages)
ages.sort() 
print('Sorted Ages list:', ages)
print('min:', ages[0])
print('max:', ages[len(ages)-1])
centro = len(ages)//2
print('Middle age:', ages[centro])
average = sum(ages)/len(ages)
print('Average:', average)
range = ages[len(ages)-1] - ages[0]
print('Range of the list is:', range)
comparemin = abs(ages[0] - average)
comparemax = abs(ages[len(ages)-1] - average)
compare = comparemax - comparemin
print('Min value minus average:', comparemin)
print('Max value minus average:', comparemax)
print('Range minus average:', compare)
print("")
#Ejercicio 2
print('Ejercicio 2')
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
centro = len(countries)//2
print('The middle country is:', countries[centro])
print("")
#Ejercicio 3
print('Ejercicio 3')
centro = len(countries)//2
left = countries[0:centro]
right = countries[centro:len(countries)]
print('Half left list of countries:', left)
print('Half right list of countries:', right)
print("")
#Ejercicio 4
print('Ejercicio 4')
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print('Countries:', countries)
centro = len(countries)//2
others = countries[0:centro]
scandic = countries[centro:len(countries)]
print('Not scandic Countries:', others)
print('Scandic Countries:', scandic)
print("")
print("revisado")