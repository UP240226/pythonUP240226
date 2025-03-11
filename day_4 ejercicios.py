#Ejercicio 1
'Thirty', 'Days', 'Of', 'Python'
full_text = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(full_text)
#Ejercicio 2
'Coding', 'For', 'All'
full_text = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(full_text)
#Ejercicio 3
company = 'Coding For All'
str(company)
#Ejercicio 4
print(company)
#Ejercicio 5
print(len(company))
#Ejercicio 6
print(company.upper())
#Ejercicio 7
print(company.lower())
#Ejercicio 8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#Ejercicio 9
cut = company[0:6]
print(cut)
#Ejercicio 10
print(company.find('Coding'))
#Ejercicio 11
python = (company.replace('Coding', 'Python'))
print(python)
#Ejercicio 12
print(python.replace('All', 'Everyone'))
#Ejercicio 13
print(company.split('.'))
#Ejercicio 14
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))
#Ejercicio 15
print('"Coding For All" index for "Coding" is...', company.index('Coding'))
#Ejercicio 16
sub_string = 'l'
print('"Coding For All" index for "l" is...', company.index(sub_string))
#Ejercicio 17
print('"Coding For All" index for "All" is...', company.index(' All'))
#Ejercicio 18
complete = 'Python For Everyone'
acrn = complete[0] + complete[1] + complete[2] + complete[7] + complete[9] + complete[11] + complete[12] + complete[14]
print('The acronym of Python For Everyone is...', acrn)
#Ejercicio 19
complete = 'Coding For All'
acrn = complete[0] + complete[1] + complete[2] + complete[7] + complete[9] + complete[11] 
print('The acronym of Coding For All is...', acrn)
#Ejercicio 20
print('The index of C is...', company.index('C'))
#Ejercicio 21
print('The index of F is...', company.index('F'))
#Ejercicio 22
company = 'Coding For All People'
print('The index of the last l is...', company.rfind('ll'))
#Ejercicio 23
sent = 'You cannot end a sentence with because because because is a conjunction'
print('The index of the first because is...', sent.find('because'))
#Ejercicio 24
print('The index of the last because is...', sent.rfind('because'))
#Ejercicio 25
sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent[31:54])
#Ejercicio 26
print('The fisrt occurrence if the word "because" is...', sent.find('because'))
#Ejercicio 27
sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent[31:54])
#Ejercicio 28
company = 'Coding For All'
print('Does "Coding For All" start with a substring Coding?', company.startswith('Coding'))
#Ejercicio 29
print('Does "Coding For All" end with a substring coding?', company.endswith('coding'))
#Ejercicio 30
company = '   Coding For All      ' 
print(company.strip())
#Ejercicio 31
print('''Which one of the following variables return True when we use the method isidentifier():
1.- 30DaysOfPython?''')
challenge = '30DaysOfPython'
print(challenge.isidentifier())
print('2.- thirty_days_of_python?')
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())
#Ejercicio 32
librarys = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(librarys))
#Ejercicio 33
print('I am enjoying this challenge. I just wonder what is next.'.split('.'))
#Ejercicio 34
Name = 'Asabeneh'
Age = 250
Country = 'Finland'
City = 'Helsinki'
sentence = 'I am {}. I am {} years old. I live in {} {}.'.format(Name, Age, Country, City)
print(sentence) 
#Ejercicio 35
radius = 10
area = 3.14 * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)
#Ejercicio 36
sum = 8 + 6
res = 8 - 6
mult = 8 * 6
div = 8 / 6
red = 8 % 6
fdiv = 8 // 6
exp = 8 ** 6
result = '8 + 6 = {}\n8 - 6 = {}\n8 * 6 = {}\n8 / 6 = {}\n8 % 6 = {}\n8 // 6 = {}\n8 ** 6 = {}'.format(8 + 6, 8 - 6, 8 * 6, 8 / 6, 8 % 6, 8 // 6, 8 ** 6)
print(result)
#Ejercicio Personal
high = 'bullish'
low = 'bearish'
middle = 'sideways'
stmk = 'stock market'
trade = 'The {} today is expected to be {}. The price of the stock market at the end of the month is expected to be more {} than {}.'.format(stmk, middle, high, low)
print(trade)