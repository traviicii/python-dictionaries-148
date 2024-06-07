# Looping/Iterating over dictionaries

def d():
    print('='*75)

student_grades = {
    "Bob" : 92,
    "Alice" : 85, 
    "Charlie" : 78
    }

# Using .items() : return each key-value pair as a tuple
items = student_grades.items()
print(items)


# Iterate over key-value pairs
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

for thing in student_grades.items():
    print(f"{thing[0]}: {thing[1]}")

d()

# using .keys() : iterate over only the keys in a dictionary

for key in student_grades.keys():
    print(key)
    print(f"Key: {key}, Value: {student_grades[key]}")

d()

# using .values() : iterates over only the values stored on a dictionary
list_of_grades = []
for value in student_grades.values():
    print(value)
    list_of_grades.append(value)

print(sum(list_of_grades)/len(list_of_grades))


d()
#--------------------

chips = {
    "Cheeto" : "Flamin Hot",
    "Dorito" : "Cool Ranch",
    "Takis" : "Fuego",
    "Miss Vickies" : "Spicy Dill Pickle"
}

# looping over keys
# .keys()

print("Major Chip Brands")
print("--------------------")
for key in chips.keys():
    print(f"Key: {key}")
    print(f"Value: {chips[key]}")

d()
# looping over values
# .values()

print("\nFlavors")
print("--------------------")
for value in chips.values():
    print(f"Flavor: {value}")

d()

# looping over both keys and values at the same time

print("\nMy favorite flavor per chip")
print("--------------------")
for key, value in chips.items():
    print(f"My favorite {key} flavor is {value}!")
