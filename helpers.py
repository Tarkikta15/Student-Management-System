from data import students

def find_students(roll):
    for s in students:
        if s["roll"] == roll:
            return s
        return None

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

def press_enter_to_continue():
    input("\nPress Enter to return to the menu...")