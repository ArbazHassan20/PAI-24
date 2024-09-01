# Dictionary containing students' names as keys and their grades as values
students_grades = {
    "John": ['A', 'B', 'C'],
    "Bob": ['B', 'B', 'B'],
    "Alice": ['D', 'A', 'C']
}

# Mapping of grades to their respective marks
grade_to_marks = {
    'A': 90,
    'B': 80, 
    'C': 70, 
    'D': 60
}

# Initial dictionary of students and their grades
print(students_grades)

# Adding a new grade 'A' to John's list of grades
students_grades["John"].append('A') 
print("Grade 'A' added to John's list")
print(students_grades["John"])

# Calculating John's average marks
total_marks = 0
for grade in students_grades["John"]:
    total_marks += grade_to_marks[grade]
print("John's average marks:", total_marks / len(students_grades["John"]))

# Adding a new student 'Adam' with an empty list of grades
students_grades['Adam'] = []
print("Adam added with an empty list of grades")

# Removing 'Bob' from the dictionary
students_grades.pop("Bob") 
print("Bob removed from the list")

# Final dictionary after updates
print(students_grades)
