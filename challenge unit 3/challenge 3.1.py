Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.

class Student:
 def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa 
   
def sort_students (student_list):
    sorted_students = sorted(student_list, key=lambda student: 
                              student.cgpa, reverse=True)
    return sorted_students

# Test with different input lists of students
students_list = [
    Student("John", "2021001", 3.9),
    Student("Jane", "2021002", 3.7),
    Student("Alice", "2021003", 3.8),
    Student("Bob", "2021004", 3.6)
]

sorted_students = sort_students(students_list)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
