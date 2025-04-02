#Exercises: Level 1
print('Exercises: Level 1')
print("")
#Ejercico 1
print('Ejercicio 1')
print('For')
for number in range(0,11):
    print(number)
print("")
print('While')
count = 0
while count < 11:
    print(count)
    count = count + 1 
print("")
#Ejercicio 2
print('Ejercicio 2')
print('For')
for number in range(10,0,-1):
    print(number)
print("")
print('While')
count = 10
while count > 0:
    print(count)
    count = count - 1 
print("")
#Ejercicio 3
print('Ejercico 3')
count = '#'
while count < '########':
    print(count)
    count = count + '#'
print("")
#Ejercicio 4
print('Ejercicio 4, ERROR')
rows = ('# # # # # # # #')
for i in range(8):
    print(rows)
print("------------------")


#Ejercicio 5
print('Ejercicio 5')
for pattern in range(0,11):
    print(pattern, 'x', pattern, '=', pattern * pattern)
    pattern = (pattern + 1) * (pattern + 1)
    print("")
#Ejercicio 6
print('Ejercicio 6')
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for items in list:
    print(items)
print("")
#Ejercicio 7
print('Ejercico 7')
for even in range(0,101,2):
    print(even)
print("")
#Ejercicio 8
print('Ejercicio 8')
for odd in range(2,101,2):
    print(odd - 1)
print("")

#Exercises: Level 2
print('Exercises: Level 2')
print("")
#Ejercicio 1
print('Ejercicio 1')
for number in range(0,101):
    print((number * (number + 1))//2)
print("")
#Ejercicio 2
print('Ejercicio 2, MEJORA')
print('Evens')
sumaImpar = 0
for i in range(101):
    if i %2 == 1:
        sumaImpar = sumaImpar + i
print("el resultado de la suma de impares es: ", sumaImpar)
print("")
print('Odds')
for odd in range(2,101,2):
    print(((number * (odd - 1))//4) + 25)
print("")

#Exercises: Level 3
print('Exercises: Level 3')
print("")
#Ejercico 1
print('Ejercicio 1, MORI')
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
for countrie in countries:
    if 'land' in countrie:
        print(countrie)
    
print("")
#Ejercicio 2
print('Ejercicio 2, NO SE')
list = ['banana', 'orange', 'mango', 'lemon']
print(list)
list.reverse()
print(list)
