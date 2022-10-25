people = [
    {
        'id': 1,
        'name': "Bob",
        'height': 5.8,
        'gender': "male",
        'money': 100,
        'age': 24,
        'email': 'bob@aol.com',
    },
    {
        'id': 2,
        'name': "Stacy",
        'height': 5,
        'gender': "female",
        'money': 10,
        'age': 30,
        'email': 'stacy16@aol.com',
    },
    {
        'id': 3,
        'name': "Jessica",
        'height': 4.6,
        'gender': "female",
        'money': 90,
        'age': 52,
        'email': 'jessbess@aol.com',
    },
    {
        'id': 4,
        'name': "Billy",
        'height': 6.1,
        'gender': "male",
        'money': 120,
        'age': 43,
        'email': 'billyTheKid@aol.com',
    },
    {
        'id': 5,
        'name': "Davey",
        'height': 5.9,
        'gender': "male",
        'money': 50,
        'age': 19,
        'email': 'crocket@aol.com',
    },
    {
        'id': 6,
        'name': "Heather",
        'height': 5,
        'gender': "female",
        'money': 10,
        'age': 46,
        'email': 'Heathers@aol.com',
    },
    {
        'id': 7,
        'name': "Jennie",
        'height': 5.1,
        'gender': "female",
        'money': 40,
        'age': 18,
        'email': 'jenjen@aol.com',
    },
    {
        'id': 8,
        'name': "Sara",
        'height': 5.2,
        'gender': "female",
        'money': 80,
        'age': 35,
        'email': 'rocknroll@aol.com',
    },
    {
        'id': 9,
        'name': "David",
        'height': 5.6,
        'gender': "male",
        'money': 35,
        'age': 28,
        'email': 'TheMuppetsMadeMeDoIt@aol.com',
    },
]

# Get user by id


def get_user_by_id(id):  # should tell us what the function is or does
    for person in people:
        if person['id'] == id:
            return person

# print(get_user_by_id(2))


# Get user by email
def get_user_by_email(email):
    for person in people:
        if person['email'] == email:
            return (person)


# print(get_user_by_email('TheMuppetsMadeMeDoIt@aol.com'))
logged_in_user = get_user_by_email('TheMuppetsMadeMeDoIt@aol.com')
print(logged_in_user['name'])
# ... (70 lines left)


def get_male_users():
    male_users = []
    for person in people:
        if person['gender'] == 'male':
            male_users.append(person)
    return male_users


print(get_male_users())


def get_female_users():
    female_users = []
    for person in people:
        if person['gender'] == 'female':
            female_users.append(person)
    return female_users


print(get_female_users())


def get_users_by_gender(gender):
    users = []
    for person in people:
        if person['gender'] == gender:
            users.append(person)
    return users


def create_new_user(name, age, gender, email, height, money):
    if get_user_by_email(email):
        return False
    id = len(people) + 1
    people.append(
        {
            'id': id,
            'name': name,
            'age': age,
            'gender': gender,
            'email': email,
            'height': height,
            'money': money,
        }
    )
    return True


create_new_user(name="Johnny", height=6, gender="male",
                money='2', email='jbg@music.toons', age=30)
print(people)

# clean version


def create_new_user_2(data):
    if get_user_by_email(data['email']): return False
    data['id'] = len(people) + 1
    people.append(data)
    return True
    
user_submitted_form_data = {
    'name' : 'John B',
    'height' : 6,
    'gender' : 'male',
    'money' : 5,
    'email' : 'aol@aol.cm',
    'age' : 6,
}

create_new_user_2(user_submitted_form_data)

print(people)