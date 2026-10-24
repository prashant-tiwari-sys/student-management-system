
import json
import os
from datetime import datetime

from student import Student, ScholarshipStudent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "students.json")


def load_students():
    """Read student records from a JSON file."""
    os.makedirs(DATA_DIR, exist_ok=True)

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: Student data must be a list.")
            return []

        return data

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: The data file is damaged or invalid.")
        return []
    except OSError as error:
        print("File error:", error)
        return []


def save_students(students):
    """Save student records to a JSON file."""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        return True

    except OSError as error:
        print("Unable to save data:", error)
        return False


def read_marks():
    """Read marks for three subjects."""
    marks = []

    for subject_number in range(1, 4):
        while True:
            try:
                mark = float(
                    input(f"Enter marks for subject {subject_number} (0-100): ")
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return marks


def add_student(students):
    print("\n--- Add Student ---")

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    # Check for duplicate IDs
    for record in students:
        if record["student_id"] == student_id:
            print("This student ID already exists.")
            return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    while True:
        try:
            age = int(input("Enter age: "))

            if 1 <= age <= 120:
                break

            print("Enter an age between 1 and 120.")

        except ValueError:
            print("Age must be a whole number.")

    course = input("Enter course name: ").strip()

    if not course:
        print("Course name cannot be empty.")
        return

    marks = read_marks()

    scholarship = input(
        "Is the student scholarship eligible? (yes/no): "
    ).strip().lower()

    record = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "scholarship": scholarship == "yes",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    students.append(record)

    if save_students(students):
        print("Student added successfully.")


def create_student(record):
    """Create the appropriate object from a saved record."""
    student_class = (
        ScholarshipStudent
        if record.get("scholarship", False)
        else Student
    )

    return student_class(
        record["student_id"],
        record["name"],
        record["age"],
        record["course"],
        record["marks"]
    )


def view_students(students):
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for record in students:
        student = create_student(record)
        # Polymorphism: the method depends on the object's class
        print(student.get_details())
        print("Added:", record.get("created_at", "Unknown"))
        print("-" * 60)


def search_student(students):
    print("\n--- Search Student ---")
    student_id = input("Enter student ID: ").strip()

    for record in students:
        if record["student_id"] == student_id:
            student = create_student(record)
            print(student.get_details())
            return

    print("Student not found.")


def update_student(students):
    print("\n--- Update Student Marks ---")
    student_id = input("Enter student ID: ").strip()

    for record in students:
        if record["student_id"] == student_id:
            print("Enter the new marks.")

            record["marks"] = read_marks()

            if save_students(students):
                print("Marks updated successfully.")
            return

    print("Student not found.")


def delete_student(students):
    print("\n--- Delete Student ---")
    student_id = input("Enter student ID: ").strip()

    for record in students:
        if record["student_id"] == student_id:
            confirmation = input(
                f"Delete {record['name']}? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                students.remove(record)

                if save_students(students):
                    print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")


def show_performance_summary(students):
    print("\n--- Performance Summary ---")

    if not students:
        print("No student records available.")
        return

    averages = []

    for record in students:
        student = create_student(record)
        average = student.calculate_average()
        averages.append(average)

        print(
            f"{student.name}: Average = {average:.2f}, "
            f"Grade = {student.calculate_grade()}"
        )

    overall_average = sum(averages) / len(averages)

    print(f"\nTotal students: {len(students)}")
    print(f"Overall average: {overall_average:.2f}")


def display_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Performance Summary")
    print("7. Exit")


def main():
    students = load_students()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_performance_summary(students)
        elif choice == "7":
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed safely.")
