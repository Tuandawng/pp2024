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

    def calculate_gpa(self):
        total_marks = sum(self.__marks.values())
        return total_marks / len(self.__marks)
