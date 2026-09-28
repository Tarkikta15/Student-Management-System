from helpers import find_students, get_valid_int


def calculate_grade(marks):
    """Convert a numeric mark (out of 100) into a letter grade."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def enter_marks():
    print("\n--- Enter Marks ---")
    roll = get_valid_int("Enter roll number: ")
    s = find_students(roll)

    if not s:
        print("No student found with that roll number.")
        return

    subject = input("Enter subject name: ").strip().title()
    marks = get_valid_int("Enter marks for {} (out of 100): ".format(subject))

    while marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        marks = get_valid_int("Enter marks for {} (out of 100): ".format(subject))

    s["marks"][subject] = marks
    print("Marks recorded for {} in {}.".format(s["name"], subject))

def view_report_card():
    print("\n--- Report Card ---")
    roll = get_valid_int("Enter roll number: ")
    s = find_students(roll)

    if not s:
        print("No student found with that roll number.")
        return

    if not s["marks"]:
        print("No marks recorded yet for {}.".format(s["name"]))
        return

    print("\nReport Card for {} ({})".format(s["name"], s["class"]))
    print("{:<15}{:<10}{:<10}".format("Subject", "Marks", "Grade"))
    print("-" * 35)

    total = 0
    for subject, marks in s["marks"].items():
        grade = calculate_grade(marks)
        total += marks
        print("{:<15}{:<10}{:<10}".format(subject, marks, grade))

    average = total / len(s["marks"])
    print("-" * 35)
    print("Average: {:.2f}   Overall Grade: {}".format(average, calculate_grade(average)))