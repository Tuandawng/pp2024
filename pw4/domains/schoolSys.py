from student import Student
from course import Course
import math
import numpy as np
class SchoolSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []

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

    def list_courses(self):
        print("List of Courses:")
        for course in self.__courses:
            print(f"ID: {course.get_id()}, Name: {course.get_name()}")

    def list_students(self):
        print("List of Students:")
        for student in self.__students:
            print(f"ID: {student.get_id()}, Name: {student.get_name()}")

    def show_student_marks(self):
        course_id = input("Enter course's id: ")
        for student in self.__students:
            if course_id in student.get_marks():
                print(f"Student: {student.get_name()}, Marks: {student.get_marks()[course_id]}")

    def calculate_average_gpa(self, student_id):
        for student in self.__students:
            if student.get_id() == student_id:
                return student.calculate_gpa()

    def sort_students_by_gpa_descending(self):
        gpas = np.array([student.calculate_gpa() for student in self.__students])
        sorted_indices = np.argsort(gpas)[::-1]  
        sorted_students = [self.__students[i] for i in sorted_indices]
        return sorted_students