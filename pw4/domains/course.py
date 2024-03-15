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