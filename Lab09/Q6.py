import matplotlib.pyplot as plt

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5",
            "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"]
math_marks = [85, 78, 92, 88, 76, 95, 89, 67, 91, 82]
science_marks = [80, 82, 88, 85, 75, 90, 85, 70, 95, 78]

plt.figure(figsize=(10, 6))
plt.scatter(math_marks, science_marks, color='blue', label='Student Marks')

plt.title('Comparison of Mathematics and Science Marks')
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')

plt.legend(loc='upper left')

plt.grid(True)

plt.show()
