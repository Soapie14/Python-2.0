#Robert C Martin-book on clean code


dictionary = {
    'word' : 'definition of the word',
    'dog'  : 'things that bark',
    'cat'  : 'things that do not bark',
}

southerner = {
    'name' : 'Aaron',
    'age' : 37,
    'hobbies' : ['fishing', 'motorcycling', 'sailing'],
    'pets' : [
        {
            'breed' : 'dog',
            'dog_name' : 'Caly',
        },
        {
            'breed' : 'dog',
            'name' : 'sam',
        }
    ],
    'isCoder' : True
}

x='name'
#print(southerner['pets'][0]['dog_name'])

#cat= {'tiger', 'lion'} #list, can change the contents in a list

#affirmative = ('si', 'hai', 'da') #tuple, can not change the contents in the list(can make a copy and change that)

foods = ['pizza', 'tamales', 'chocolate', 'steak']

#for x in range(len(food)):
#    print(food[x])

#for food in foods:
#    print(food)

#for i in range(len(foods)):
#    print(str(i+1), foods[i].capitalize())
    
    
dictionary = {
    'word' : 'definition of the word',
    'dog'  : 'things that bark',
    'cat'  : 'things that do not bark',
}

#for i in dictionary:
#    print(i,'-', dictionary[i])

#for key in dictionary:
    #print(key, dictionary[key])
    
dictionary['ship'] = 'water vessel'

#for key in dictionary:
    #print(key, dictionary[key])
    
    
    
name = 'Sophie'
age = 28

print(f'''I'm {name}, and I'm {age} "years" old''')

myString= '''
this
really
works
'''

print(myString)

x='1'
y=2

print(x+y)