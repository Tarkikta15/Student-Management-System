from helpers import press_enter_to_continue
from records import add_student , view_students , search_student , update_student , delete_student
from attendance import mark_attendance, view_attendance
from marks import enter_marks, view_report_card

def main_menu():
    while True:
        print("\n" + "=" * 40)
        print("     STUDENT MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Mark Attendance (Subject-wise)")
        print("7. View Attendance")
        print("8. Enter Marks")
        print("9. View Report Card")
        print("0. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            mark_attendance()
        elif choice == "7":
            view_attendance()
        elif choice == "8":
            enter_marks()
        elif choice == "9":
            view_report_card()
        elif choice == "0":
            print("\nExiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        press_enter_to_continue()


if __name__ == "__main__":
    main_menu()