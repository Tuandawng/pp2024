def input_something(number): 
    return int(input(f"Please enter the number of students: {number}"))

def input_info():
    id = input("Enter student's id: ")
    name = input("Enter student's name: ")
    dob = input("Enter date of birth: ")
    return id, name, dob  

def input_number_of_course():
    return int(input("Enter number of courses: "))

def input_course_info():
    id = input("Enter course's id: ")
    name = input("Enter course's name: ")
    return id, name  

def main():
    students = []
    courses = []

    while True:
        print("""
        0. Exit.
        1. Get number of students.
        2. Get student's information.
        3. Get number of courses.
        4. Get course's information.
        """)

        option = int(input("Your choice: "))

        if option == 0:
            break

        elif option == 1:
            num_students = input_something(len(students))
            print(f"Number of students: {num_students}")

        elif option == 2:
            student_info = input_info()
            students.append(student_info)
            print("Student information added.")

        elif option == 3:
            num_courses = input_number_of_course()
            print(f"Number of courses: {num_courses}")

        elif option == 4:
            course_info = input_course_info()
            courses.append(course_info)
            print("Course information added.")

        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()
