# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 

x[1] = [15, 8, 9]

# print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]["last_name"]= 'Bryant'

# print(students[0])


# In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0]= 'Andres'

# print(sports_directory['soccer'])


# Change the value 20 in z to 30


z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30

# print(z)

#PART 2

def iterateDictionary(some_list):
    for key in students:
        print(key)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 


#PART 3
#Get Values From a List of Dictionaries, , given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:



def iterateDictionary2(key_name, students):
    for student in students:
        print(student[key_name])
        
# iterateDictionary2('last_name', students)

#PART4
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:


def printInfo(some_dict):
    print(len(some_dict['locations']), "LOCATIONS:")
    for location in some_dict['locations']:
        print(location)
    print()
    print(len(some_dict['instructors']), "INSTRUCTORS:")
    for location in some_dict['instructors']:
        print(location)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)