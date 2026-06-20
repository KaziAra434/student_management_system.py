# Student Management System

students = []
recent_stack = []

def add_student():

    while True:
        try:
            count = int(input("\nHow many students do you want to add? "))

            if count > 0:
                break
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    for i in range(count):

        print(f"\n========== Student {i + 1} ==========")

        # Student ID Validation
        while True:
            student_id = input("Enter Student ID (4 digits, e.g. 1234): ").strip()

            if student_id.isdigit() and len(student_id) == 4:

                duplicate = False

                for student in students:
                    if student["id"] == student_id:
                        duplicate = True
                        break

                if duplicate:
                    print("Student ID already exists!")
                else:
                    break

            else:
                print("Invalid ID! Enter exactly 4 digits.")

        # Name Validation
        while True:
            name = input("Enter Name: ").title().strip()

            if name.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Name! Use letters and spaces only.")

        # Department Validation
        while True:
            department = input("Enter Department: ").upper().strip()

            if department.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Department! Use letters only.")
                print("Example: CSE, EEE, ZOOLOGY, SOIL")

        # CGPA Validation
        while True:
            try:
                cgpa = float(input("Enter CGPA (0.00 - 4.00): "))

                if 0 <= cgpa <= 4:
                    break
                else:
                    print("CGPA must be between 0.00 and 4.00.")

            except ValueError:
                print("Invalid CGPA! Enter a numeric value.")

        student = {
            "id": student_id,
            "name": name,
            "department": department,
            "cgpa": cgpa
        }

        students.append(student)
        recent_stack.append(student)

    print(f"\n{count} student(s) added successfully!")


def view_students():

    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No students found.")
        return

    print(f"\n{len(students)} student(s) result have been added.\n")

    print(f"{'ID':<10}{'NAME':<25}{'DEPARTMENT':<15}{'CGPA'}")
    print("-" * 60)

    for student in students:
        print(
            f"{student['id']:<10}"
            f"{student['name']:<25}"
            f"{student['department']:<15}"
            f"{student['cgpa']:.2f}"
        )


def search_student():

    if len(students) == 0:
        print("\nNo students available to search.")
        return

    while True:
        print("\nSearch Student By")
        print("1. ID")
        print("2. Name")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice in ["0", "1", "2"]:
            break

        print("Invalid choice!")

    if choice == "0":
        return

    found = False

    if choice == "1":

        student_id = input(
            "Enter Student ID (4 digits, e.g. 1234): "
        ).strip()

        for student in students:

            if student["id"] == student_id:

                print("\nStudent Found:")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Department:", student["department"])
                print("CGPA:", f"{student['cgpa']:.2f}")

                found = True
                break

    elif choice == "2":

        name = input("Enter Name: ").title().strip()

        for student in students:

            if student["name"] == name:

                print("\nStudent Found:")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Department:", student["department"])
                print("CGPA:", f"{student['cgpa']:.2f}")

                found = True
                break

    if not found:
        print("Student not found!")


def stack_operations():

    while True:

        print("\n========== STACK OPERATIONS ==========")
        print("1. View Stack")
        print("2. Pop Student")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            if len(recent_stack) == 0:
                print("Stack is empty!")

            else:

                print("\n------ STACK (Recent Students) ------")

                for student in reversed(recent_stack):
                    print(f"{student['id']} | {student['name']}")

        elif choice == "2":

            if len(recent_stack) == 0:
                print("Stack is empty!")

            else:

                removed = recent_stack.pop()

                print(
                    f"Removed Student: "
                    f"{removed['id']} | {removed['name']}"
                )

        elif choice == "0":
            break

        else:
            print("Invalid choice! Please enter 0, 1 or 2.")


# Main Program
while True:

    print("\n================ STUDENT MANAGEMENT SYSTEM ================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Stack Operations (Recently Added Students)")
    print("0. Exit")
    print("=" * 50)

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        stack_operations()

    elif choice == "0":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please enter 0, 1, 2, 3 or 4.")
