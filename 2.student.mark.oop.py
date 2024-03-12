class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_marks(self):
        return self.__marks


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__marks = {}

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks


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

    def main(self):
        while True:
            print("""
            0. Exit.
            1. Get number of students and their info.
            2. Get number of courses and their info.
            3. Input marks.
            4. List courses.
            5. List students.
            6. Show student marks for a given course.
            """)

            option = int(input("Your choice: "))

            if option == 0:
                break

            elif option == 1:
                self.input_student_info()
                print("Student information added.")

            elif option == 2:
                self.input_course_info()
                print("Course information added.")

            elif option == 3:
                self.input_marks()
                print("Marks added.")

            elif option == 4:
                self.list_courses()

            elif option == 5:
                self.list_students()

            elif option == 6:
                self.show_student_marks()

            else:
                print("Invalid input. Please try again!")


if __name__ == "__main__":
    school_system = SchoolSystem()
    school_system.main()
