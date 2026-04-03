students = [
    {"name": "Anil Malappa Dodamani", "roll": "2LB22EC400", "marks": "93"},
    {"name": "Akshata Anil Dodamani", "roll": "2LB22EC401", "marks": "94"},
    {"name": "Ankita Biradar", "roll": "2LB22EC402", "marks": "90"},
    {"name": "Adarsh Biradar", "roll": "2LB22EC403", "marks": "91"},
    {"name": "Aishwarya Biradar", "roll": "2LB22EC404", "marks": "80"}
]

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return

    for student in students:
        print(student)
    print()

def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found:", student, "\n")
            return

    print("Student not found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")