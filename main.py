print("Welcome to Student Management System")
print("------------------------------------")
print("BCA IBM College Project")
print("Developed by Sanya")
students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")
    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("Roll Number:", student["roll"])
                print("Marks:", student["marks"])
    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print("Student found!")
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                found = True

        if not found:
            print("Student not found.")
    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Try again.")