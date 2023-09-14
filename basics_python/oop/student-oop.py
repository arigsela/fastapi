"""
Object Oriented PRogramming
"""


class Student:

    # Class variables
    school = "School"
    number_of_students = 0

    def __init__(self, first_name, last_name, major):
        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        # Keeping track of student count
        Student.number_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a {self.major}!'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a {self.major} in {self.school}'

    # when this method is called, it will change the class variable for all objects
    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    # Method to split a string into class fields
    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)


print(f'Number of students = {Student.number_of_students}')

student_1 = Student('Eric','Roby', 'Computer Science')
student_2 = Student('Ari', 'Sela', 'Medicine')

print(student_1.fullname_major_school())
print(student_2.fullname_major_school())
print(f'Number of students = {Student.number_of_students}')

print(student_1.school)
print(student_2.school)
Student.set_online_school('I use Google Hangouts for class')
print(student_1.school)
print(student_2.school)

new_student = 'Adil.Yutzy.English'
student_3 = Student.split_students(new_student)
print(student_3.fullname_major_school())
