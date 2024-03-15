from domains.student import Student
from domains.course import Course
from domains.schoolSys import SchoolSystem
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