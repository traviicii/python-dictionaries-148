def d():
    print('='*75)
# Nesting Dictionaries and Lists

# Lists inside of dictionaries

pet_names = {
    'Dog': ['Oreo', 'Max', 'Punkin', 'Pinky', 'Rover', 'Fido', 'Rex', 'Pluto', 'Trouble'],
    'Cat': ['Mittens', "Ziggy", "Hot Pocket", 'Miso', 'CatKeisha', 'Randolf', 'Snowball', 'Smokey', 'Cookie'],
    'Hamster': ['Hamtarro', 'Lightening', 'Nugget', 'Cheddars', 'Hammie', 'Turbo'],
    'Lizard': 'Lizzy'
}

pet_names['Lizard'] = ['Lizzy', 'Izzy']
# we can chain keys and indecies one after another
print(pet_names['Cat'][3])

#   key  value
for pet, names in pet_names.items():
    print(f"\nCommon {pet} names: ")
    if isinstance(names, list):
        for name in names:
            print(name)
    else:
        print(names)

d()

# Dictionaries inside of Lists

books = [
    {'Title': 'Diary of a Wimpy Kid', 'Author': 'Jeff Kiney', 'Genre': 'YAF'},
    {'Title': 'Rich Dad Poor Dad', 'Author': 'Robert Kiwaske', 'Genre': 'Self Help'},
    {'Title': 'Dune', 'Author': 'Frank Herbert', 'Genre': 'Science Fiction'}
]

# We can chain indecies and keys one after another
print(books[0]['Author'])

for book in books:
    print(f"{book['Title']} is written by {book['Author']}")


user = {
    'dk@email.com': {'username': 'dylank', 'password': '12345', 'likes': ['tacos', 'dogs']},
    'tp@email.com': {'username': 'travisp', 'password': '67890', 'likes': ['key lime pie', 'walks on the beach']},
    'rk@dogmail.com': {'username': 'Rhiannon-Bananan', 'password': '91827465', 'likes': ['treats', 'walks to the park']}
}

print(user['tp@email.com']['likes'][0])

def login(user_dict):
    while True:
        try:
            email = input("enter your email: ")
            password = input("Enter your password: ")
            user = user_dict[email]
            if password != user['password']:
                raise ValueError
        except Exception as e:
            print(e)
            print("Invalid email or password")
        else:
            print(f"Welcome back {user['username']}")
            break

login(user)