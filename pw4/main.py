from domains.student import Student
from domains.course import Course
from domains.schoolSys import SchoolSystem
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
            7. Calculate average GPA for a student.
            8. Sort students by GPA descending.
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

            elif option == 7:
                student_id = input("Enter student's ID: ")
                avg_gpa = self.calculate_average_gpa(student_id)
                print(f"Average GPA for student {student_id}: {avg_gpa:.2f}")

            elif option == 8:
                sorted_students = self.sort_students_by_gpa_descending()
                print("Students sorted by GPA descending:")
                for student in sorted_students:
                    print(f"ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.calculate_gpa()}")

            else:
                print("Invalid input. Please try again!")


if __name__ == "__main__":
    school_system = SchoolSystem()
    school_system.main()
