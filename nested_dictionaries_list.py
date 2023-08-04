# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0] ['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)

# 2 iterate thhrough a list of dictionaries

students1 = [ 
        {'first_name': 'michael', 'last_name': 'jordan'},
        {'first_name': 'john', 'last_name': 'rosales'},
        {'first_name': 'mark', 'last_name': 'guillen'},
        {'first_name': 'kb', 'last_name': 'tonel'}
    ]

for name in students1:
    for key, val in name.items():
        print(f'{key} - {val}')


# 3 get values from a list of dictionaries
students2 = [ 
        {'first_name': 'michael', 'last_name': 'jordan'},
        {'first_name': 'john', 'last_name': 'rosales'},
        {'first_name': 'mark', 'last_name': 'guillen'},
        {'first_name': 'kb', 'last_name': 'tonel'}
    ]
for i, first_name in enumerate(key['first_name'] for key in students2):
    print(i,first_name)
for i, last_name in enumerate(key['last_name'] for key in students2):
    print(i,last_name)

# 4 iterate through a dictionary with list values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
for key, value in dojo.items():
    print(len(value),key)
    if(isinstance(value, list)):
        for value in value:
            print(value)