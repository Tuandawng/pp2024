from domains.student import Student
from domains.course import Course
from domains.schoolSys import SchoolSystem
import math

def input_number_of_students(self):
    return int(input("Enter number of students: "))

def input_student_info(self):
    for _ in range(self.input_number_of_students()):
        id = input("Enter student's id: ")
        name = input("Enter student's name: ")
        dob = input("Enter date of birth: ")
        self.__students.append(Student(id, name, dob))
        print("\n")

def input_number_of_courses(self):
    return int(input("Enter number of courses: "))

def input_course_info(self):
    for _ in range(self.input_number_of_courses()):
        id = input("Enter course's id: ")
        name = input("Enter course's name: ")
        self.__courses.append(Course(id, name))
        print("\n")

def input_marks(self):
    course_id = input("Enter course's id: ")
    for course in self.__courses:
        if course.get_id() == course_id:
            for student in self.__students:
                mark = float(input(f"Input mark for {student.get_name()}: "))
                mark = math.floor(mark * 10) / 10  
                student.add_mark(course_id, mark)
                course.get_marks()[student.get_id()] = mark
