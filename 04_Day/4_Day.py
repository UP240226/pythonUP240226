#Ejercicio 1
print('Ejercicio 1')
'Thirty', 'Days', 'Of', 'Python'
full_text = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(full_text)
print("")
#Ejercicio 2
print('Ejercicio 2')
'Coding', 'For', 'All'
full_text = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(full_text)
print("")
#Ejercicio 3
print('Ejercicio 3')
company = 'Coding For All'
str(company)
print(type(company))
print("")
#Ejercicio 4
print('Ejercicio 4')
print(company)
print("")
#Ejercicio 5
print('Ejercicio 5')
print(len(company))
print("")
#Ejercicio 6
print('Ejercicio 6')
print(company.upper())
print("")
#Ejercicio 7
print('Ejercicio 7')
print(company.lower())
print("")
#Ejercicio 8
print('Ejercicio 8')
print(company.capitalize())
print(company.title())
print(company.swapcase())
print("")
#Ejercicio 9
print('Ejercicio 9')
cut = company[0:6]
print(cut)
print("")
#Ejercicio 10
print('Ejercicio 10')
print(company.find('Coding'))
print("")
#Ejercicio 11
print('Ejercicio 11')
python = (company.replace('Coding', 'Python'))
print(python)
print("")
#Ejercicio 12
print('Ejercicio 12')
print(python.replace('All', 'Everyone'))
print("")
#Ejercicio 13
print('Ejercicio 13')
print(company.split('.'))
print("")
#Ejercicio 14
print('Ejercicio 14')
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))
print("")
#Ejercicio 15
print('Ejercicio 15')
print('"Coding For All" index for "Coding" is...', company.index('Coding'))
print("")
#Ejercicio 16
print('Ejercicio 16')
sub_string = 'l'
print('"Coding For All" index for "l" is...', company.index(sub_string))
print("")
#Ejercicio 17
print('Ejercicio 17')
print('"Coding For All" index for "All" is...', company.index(' All'))
print("")
#Ejercicio 18
print('Ejercicio 18')
complete = 'Python For Everyone'
acrn = complete[0] + complete[1] + complete[2] + complete[7] + complete[9] + complete[11] + complete[12] + complete[14]
print('The acronym of Python For Everyone is...', acrn)
print("")
#Ejercicio 19
print('Ejercicio 19')
complete = 'Coding For All'
acrn = complete[0] + complete[1] + complete[2] + complete[7] + complete[9] + complete[11] 
print('The acronym of Coding For All is...', acrn)
print("")
#Ejercicio 20
print('Ejercicio 20')
print('The index of C is...', company.index('C'))
print("")
#Ejercicio 21
print('Ejercicio 21')
print('The index of F is...', company.index('F'))
print("")
#Ejercicio 22
print('Ejercicio 22')
company = 'Coding For All People'
print('The index of the last l is...', company.rfind('ll'))
print("")
#Ejercicio 23
print('Ejercicio 23')
sent = 'You cannot end a sentence with because because because is a conjunction'
print('The index of the first because is...', sent.find('because'))
print("")
#Ejercicio 24
print('Ejercicio 24')
print('The index of the last because is...', sent.rfind('because'))
print("")
#Ejercicio 25
print('Ejercicio 25')
sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent[31:54])
print("")
#Ejercicio 26
print('Ejercicio 26')
print('The fisrt occurrence if the word "because" is...', sent.find('because'))
print("")
#Ejercicio 27
print('Ejercicio 27')
sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent[31:54])
print("")
#Ejercicio 28
print('Ejercicio 28')
company = 'Coding For All'
print('Does "Coding For All" start with a substring Coding?', company.startswith('Coding'))
print("")
#Ejercicio 29
print('Ejercicio 29')
print('Does "Coding For All" end with a substring coding?', company.endswith('coding'))
print("")
#Ejercicio 30
print('Ejercicio 30')
company = '   Coding For All      ' 
print(company.strip())
print("")
#Ejercicio 31
print('Ejercicio 31')
print('''Which one of the following variables return True when we use the method isidentifier():
1.- 30DaysOfPython?''')
challenge = '30DaysOfPython'
print(challenge.isidentifier())
print('2.- thirty_days_of_python?')
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())
print("")
#Ejercicio 32
print('Ejercicio 32')
librarys = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(librarys))
print("")
#Ejercicio 33
print('Ejercicio 33')
print('I am enjoying this challenge. I just wonder what is next.'.split('.'))
print("")
#Ejercicio 34
print('Ejercicio 34')
Name = 'Asabeneh'
Age = 250
Country = 'Finland'
City = 'Helsinki'
sentence = 'I am {}. I am {} years old. I live in {} {}.'.format(Name, Age, Country, City)
print(sentence) 
print("")
#Ejercicio 35
print('Ejercicio 35')
radius = 10
area = 3.14 * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)
print("")
#Ejercicio 36
print('Ejercicio 36')
sum = 8 + 6
res = 8 - 6
mult = 8 * 6
div = 8 / 6
red = 8 % 6
fdiv = 8 // 6
exp = 8 ** 6
result = '8 + 6 = {}\n8 - 6 = {}\n8 * 6 = {}\n8 / 6 = {}\n8 % 6 = {}\n8 // 6 = {}\n8 ** 6 = {}'.format(8 + 6, 8 - 6, 8 * 6, 8 / 6, 8 % 6, 8 // 6, 8 ** 6)
print(result)
print("")
#Ejercicio Personal

high = 'bullish'
low = 'bearish'
middle = 'sideways'
stmk = 'stock market'
trade = 'The {} today is expected to be {}. The price of the stock market at the end of the month is expected to be more {} than {}.'.format(stmk, middle, high, low)
print(trade)