"""
Gradebook App
- list creation
-  inndex
-  basic list options
-  trackes student grades
"""

student_names = []
student_grades = []


def create_course() -> str:
    """Ask user for course name and return it."""
    return input("Enter the course name: ").strip().title()


def add_student():
    """Add a single student with a grade."""
    name = input("Enter student name: ").title().strip()
    grade = int(input("Enter student percentage: ").strip())
    student_names.append(name)
    student_grades.append(grade)


def update_grade():
    """Update the grade for an existing student."""
    name = input("Enter student name to update: ").title().strip()
    if (
        name in student_names
    ):  # this is how you loop throught a list and search for an item
        index = student_names.index(name)
        new_grade = int(input(f"Enter new grade for {name}: ").strip())
        student_grades[index] = new_grade


def remove_student():
    """Remove student and their grade."""
    name = input("Enter student name to remove: ").title().strip()
    if name in student_names:  # Cheak to see if the name entered is in the list
        index = student_names.index(name)  # get the index of the name entered
        student_names.pop(index)  # pop gets rid ofthe item at the index
        student_grades.pop(index)
        print("Student removed.")
    else:
        print("There are no students by that name.")


def show_roster():
    """Display all students and their grades."""
    # Do something if there are no students in the roster
    if not student_names:
        print("No students in the course.")
        return
    # Loop through list ofstudents and show their name and grade
    print("\nCourse Roster:")
    for index in range(len(student_names)):
        print(f"Student: {student_names[index]}, Grade: {student_grades[index]}%")


def show_statistics():
    """Display class statistics."""
    # If there are no students,  tell user
    if not student_names:
        print("No students in the course to calculate statistics.")
        return

    # Calculate and show average of the class
    average = sum(student_grades) / len(student_grades)

    # Output the avrage, highest and lowest score
    print(f"\nClass Statistics:")
    print(f"Average: {round(average, 2)}%")
    print(f"Highest mark: {max(student_grades)}%")
    print(f"Lowest mark: {min(student_grades)}%")


def main():
    """
    Main program loop - runs all other functions
    """
    # Create a new course
    course = create_course()
    # welcome user to course
    print(f"\nWelcome to the {course}!")

    # show options for user to choose
    while True:
        print("\n1-Please choose an option:")
        print("2 - Update grade")
        print("3 - Remove student")
        print("4 - Show roster")
        print("5 - Show statistics")
        print("0 - Exit")

        choice = input(" Choose an option ").strip()

        # Based on chioce, run feature
        # Features:
        # Add student
        if choice == "1":
            add_student()
        # Update grade
        elif choice == "2":
            update_grade()
        # Remove student
        elif choice == "3":
            remove_student()
        # show roster
        elif choice == "4":
            show_roster()
        # show statstisics
        elif choice == "5":
            show_statistics()
        # Exit
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
