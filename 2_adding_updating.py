# Adding and Updating elements in a dictionary

student_grades = {
    "Bob" : 92,
    "Alice" : 85, 
    "Charlie" : 78
    }

# add a new key-value pair
student_grades["David"] = 88
student_grades["Josh"] = 98

print(student_grades)

# updating existing data within a dictionary
student_grades["Alice"] = 90 # altering the data at the key "Alice" to now = 90
student_grades["Alice"] += 5 # we're just adding 5 to the number already stored in the value at the key "Alice"
print(student_grades)

# using the update method
# Merges another dictionary into the existing dictionary, updates the keys as necesary
student_grades.update({"Eve": 95, "Walter": 78, "Charlie": 85})
print(student_grades)

