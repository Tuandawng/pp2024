students = []
courses = []

def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_info():
    for i in range(input_number_of_students()):
        id = input("Enter student's id: ")
        name = input("Enter student's name: ")
        dob = input("Enter date of birth: ")
        students.append({'id': id, 'name': name, 'dob': dob, 'marks': {}})
        print("\n")

def input_number_of_course():
    return int(input("Enter number of courses: "))

def input_course_info():
    for i in range(input_number_of_course()):
        id = input("Enter course's id: ")
        name = input("Enter course's name: ")
        courses.append({'id': id, 'name': name, 'marks': {}})
        print("\n")

def input_marks():
    course_id = input("Enter course's id: ")
    for course in courses:
        if course['id'] == course_id:
            for student in students:
                mark = float(input(f"Input mark for {student['name']}: "))
                student['marks'][course_id] = mark
                course['marks'][student['id']] = mark

def list_courses():
    print("List of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    print("List of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}")

def show_student_marks():
    course_id = input("Enter course's id: ")
    for student in students:
        if course_id in student['marks']:
            print(f"Student: {student['name']}, Marks: {student['marks'][course_id]}")

def main():
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
            input_student_info()
            print("Student information added.")

        elif option == 2:
            input_course_info()
            print("Course information added.")

        elif option == 3:
            input_marks()
            print("Marks added.")

        elif option == 4:
            list_courses()

        elif option == 5:
            list_students()

        elif option == 6:
            show_student_marks()

        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()
