
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

   
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")


class Marks(Student):
    def __init__(self, student_id, student_name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, student_name) 
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

   
    def display_marks(self):
        print(f"Marks in Algorithms: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_dataScience}")
        print(f"Marks in Calculus: {self.marks_calculus}")


class Result(Marks):
   
    def display_result(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")


student = Result(4031, "Arbaz Hassan", 75, 82, 83)
student.display_info() 
student.display_marks()
student.display_result() 
