# Filename: student_profile_system_duaeman.py

students = []


def add_std():
    print("\n*** Add New Student ***")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    roll_no = input("Enter your roll number: ")
    email = input("Enter your email: ")
    course = input("Enter your course name: ")
    skills = input("Enter your skills (comma-separated): ").split(',')

    student = {
        "name": name,
        "age": age,
        "roll_no": roll_no,
        "email": email,
        "course": course,
        "skills": [skill.strip() for skill in skills]
    }

    students.append(student)
    print("The student is added successfully\n")


def view_std():
    if not students:
        print("there are no student available.\n")
    else:
        for student in students:
            print(f"Roll No: {student['roll_no']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Email: {student['email']}")
            print(f"Course: {student['course']}")
            print(f"Skills: {', '.join(student['skills'])}")
            print("-" * 30)


def search_std():
    print("\n*** Search Student by Roll Number ***")
    roll_no = input("Enter roll number: ")
    for student in students:
        if student["roll_no"] == roll_no:
            print(f"\nName: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Email: {student['email']}")
            print(f"Course: {student['course']}")
            print(f"Skills: {', '.join(student['skills'])}")
            return
    print("Student not found.\n")


def update_std():
    print("\n=== Update Student Profile ===")
    roll_no = input("Enter roll number to update: ")
    for student in students:
        if student["roll_no"] == roll_no:
            print("1. Update Email")
            print("2. Update Course")
            choice = input("Choose field to update (1 or 2): ")
            if choice == "1":
                new_email = input("Enter new email: ")
                student["email"] = new_email
                print("Email updated successfully!\n")
            elif choice == "2":
                new_course = input("Enter new course name: ")
                student["course"] = new_course
                print("Course updated successfully!\n")
            else:
                print("Invalid option.\n")
            return
    print("Student not found.\n")


def delete_std():
    print("\n=== Delete Student Profile ===")
    roll_no = input("Enter roll number to delete: ")
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student profile deleted successfully!\n")
            return
    print("Student not found.\n")


def main():
    while True:
        print("*** Student Profile Management System ***")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search by Roll Number")
        print("4. Update Student Profile")
        print("5. Delete Profile")
        print("6. Exit")
        print("*****************************************")
        choice = input("Choose an option: ")

        if choice == "1":
            add_std()
        elif choice == "2":
            view_std()
        elif choice == "3":
            search_std()
        elif choice == "4":
            update_std()
        elif choice == "5":
            delete_std()
        elif choice == "6":
            print("thank u for your time. Goodbye!")
            break
        else:
            print("No option available. Please try again.\n")


# Run the main program
main()
