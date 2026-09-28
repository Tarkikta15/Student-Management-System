from helpers import find_students, get_valid_int


def mark_attendance():
    print("\n--- Mark Attendance ---")
    roll = get_valid_int("Enter roll number: ")
    s = find_students(roll)

    if not s:
        print("No student found with that roll number.")
        return

    subject = input("Enter subject name: ").strip().title()
    status = input("Present today? (y/n): ").strip().lower()

    # If this subject hasn't been tracked before, initialise it
    if subject not in s["attendance"]:
        s["attendance"][subject] = {"present": 0, "total": 0}

    s["attendance"][subject]["total"] += 1
    if status == "y":
        s["attendance"][subject]["present"] += 1

    print("Attendance marked for {} in {}.".format(s["name"], subject))

def view_attendance():
    print("\n--- View Attendance ---")
    roll = get_valid_int("Enter roll number: ")
    s = find_students(roll)

    if not s:
        print("No student found with that roll number.")
        return

    if not s["attendance"]:
        print("No attendance records yet for {}.".format(s["name"]))
        return

    print("\nAttendance record for {} ({}):".format(s["name"], s["class"]))
    print("{:<15}{:<10}{:<10}{:<10}".format("Subject", "Present", "Total", "Percentage"))
    print("-" * 45)

    for subject, record in s["attendance"].items():
        present = record["present"]
        total = record["total"]
        percentage = (present / total * 100) if total > 0 else 0
        print("{:<15}{:<10}{:<10}{:.1f}%".format(subject, present, total, percentage))

        if percentage < 75:
            print("   -> Warning: attendance below 75% in {}".format(subject))