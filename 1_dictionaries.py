# Python Dictionaries

# What are dictionaries?

# Mutables data type : We can add, mutate, and remove data fro them
# collection of key-value pairs: like labeled jars, each key has a corresponding value

# keys:
#-- must be unique
#-- Typically keys are strings, but they can be any IMMUTABLE data type (strings, numbers, tuples)

# values : can be any data type

# big benefit is that they are flexible and can change over time

# We use a key to acces the data contained in its value

# Emtpy dictionary
#empty_list = [] 
empty_dictionary = {}

# Populated dictionary

student_grades = {
    "Alice" : 85, 
    "Bob" : 92,
    "Charlie" : 78
    }

# Accessing elements within dictionaries

# accessing values by specifying its key in square brackets
alice_grade = student_grades["Alice"]
print(alice_grade)

# KeyErrors can occur when trying to access data at a key that doesn't exist
# david_grade = student_grades["David"]

# Can access dictionaries using the .get()

#syntax for .get(<key>, <a default value to return if the key we're looking for isn't found>)

david_grade = student_grades.get("David", "Not found")
print(david_grade)
# using .get() method prevents us from encountering KeyError

