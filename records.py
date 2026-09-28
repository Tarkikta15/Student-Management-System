from data import students
from helpers import find_students , get_valid_int

def add_student():
    print("\n--- Add New Student ---")
    roll = get_valid_int("Enter roll number: ")

    if find_students(roll):
        print("A student with this roll number already exists.")
        return

    name = input("Enter name: ").strip()
    student_class = input("Enter class (e.g. 10A): ").strip()

    new_student = {
        "roll": roll,
        "name": name,
        "class": student_class,
        "attendance": {},   # subject-wise attendance, filled in later
        "marks": {}          # subject-wise marks, filled in later
    }
    students.append(new_student)
    print("Student '{}' added successfully.".format(name))
    
def view_students():
    print("\n--- All Students ---")
    if not students:
        print("No student records found.")
        return

    print("{:<6}{:<15}{:<8}".format("Roll", "Name", "Class"))
    print("-" * 30)
    for s in students:
        print("{:<6}{:<15}{:<8}".format(s["roll"], s["name"], s["class"]))

def search_student():
    print("\n--- Search Student ---")
    roll = get_valid_int("Enter roll number to search: ")
    s =  find_students(roll)

    if not s:
        print("No student found with that roll number.")
        return

    print("\nRoll No : {}".format(s["roll"]))
    print("Name    : {}".format(s["name"]))
    print("Class   : {}".format(s["class"]))

def update_student():
    print("\n--- Update Student ---")
    roll = get_valid_int("Enter roll number to update: ")
    s =  find_students(roll)

    if not s:
        print("No student found with that roll number.")
        return

    print("Leave blank to keep existing value.")
    new_name = input("New name [{}]: ".format(s["name"])).strip()
    new_class = input("New class [{}]: ".format(s["class"])).strip()

    if new_name:
        s["name"] = new_name
    if new_class:
        s["class"] = new_class

    print("Student record updated successfully.")

def delete_student():
    print("\n--- Delete Student ---")
    roll = get_valid_int("Enter roll number to delete: ")
    s =  find_students(roll)

    if not s:
        print("No student found with that roll number.")
        return

    confirm = input("Are you sure you want to delete '{}'? (y/n): ".format(s["name"])).lower()
    if confirm == "y":
        students.remove(s)
        print("Student record deleted.")
    else:
        print("Deletion cancelled.")