# Removing key-value pairs from a dictionary

student_grades = {"Bob" : 92,"Alice" : 85, "Charlie" : 78}

# using .pop()
# Removes the specified key and returns its value. If the key doesn't exist it returns the default value
# bob_grade = student_grades.pop("Bob", "Not found")
# print(bob_grade)
# print(student_grades)

# Using the .popitem() removes and returns the last key-value pair as a tuple
# last_item = student_grades.popitem()
# print(last_item)
print(student_grades)

# using del
#delete the key-value pair from the dictionary
del student_grades['Charlie']
print(student_grades)

# Using .clear() : Removes all key-value pairs from the dictionary, leaving it empty
student_grades.clear()
print(student_grades)