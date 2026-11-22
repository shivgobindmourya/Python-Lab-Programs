import pickle
import shelve
import os


# 1. Class representing a Python object
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print("\n----- STUDENT DETAILS -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.marks)

    def __repr__(self):
        return (
            f"Student(id={self.student_id}, "
            f"name={self.name!r}, marks={self.marks})"
        )


# File used by pickle
PICKLE_FILE = "student_data.pkl"

# Database file used by shelve
SHELVE_FILE = "student_database"


# 2. Save objects using pickle
def save_with_pickle():
    try:
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        marks = float(input("Enter student marks: "))

        if not student_id or not name:
            print("Student ID and name cannot be empty!")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100!")
            return

        student = Student(student_id, name, marks)

        # Save object in binary format
        with open(PICKLE_FILE, "wb") as file:
            pickle.dump(student, file)

        print("Object serialized successfully using pickle!")
        print("Saved file:", os.path.abspath(PICKLE_FILE))

    except ValueError:
        print("Invalid marks! Please enter a numeric value.")

    except OSError as error:
        print("File error:", error)


# 3. Restore objects using pickle
def load_with_pickle():
    if not os.path.exists(PICKLE_FILE):
        print("No saved pickle object found!")
        return

    try:
        with open(PICKLE_FILE, "rb") as file:
            student = pickle.load(file)

        if not isinstance(student, Student):
            print("The saved file does not contain a Student object.")
            return

        print("Object restored successfully using pickle!")
        student.display()

    except (OSError, pickle.UnpicklingError, EOFError) as error:
        print("Unable to restore object:", error)


# 4. Save objects using shelve
def save_with_shelve():
    try:
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        marks = float(input("Enter student marks: "))

        if not student_id or not name:
            print("Student ID and name cannot be empty!")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100!")
            return

        student = Student(student_id, name, marks)

        # Store object using a persistent dictionary
        with shelve.open(SHELVE_FILE) as database:
            database[student_id] = student

        print("Object saved successfully using shelve!")
        print("Storage key:", student_id)

    except ValueError:
        print("Invalid marks! Please enter a numeric value.")

    except OSError as error:
        print("Storage error:", error)


# 5. Restore an object using shelve
def load_with_shelve():
    student_id = input("Enter student ID to restore: ").strip()

    if not student_id:
        print("Student ID cannot be empty!")
        return

    try:
        with shelve.open(SHELVE_FILE) as database:
            if student_id not in database:
                print("No student found with that ID!")
                return

            student = database[student_id]

        if not isinstance(student, Student):
            print("Stored data is not a Student object.")
            return

        print("Object restored successfully using shelve!")
        student.display()

    except (OSError, EOFError, pickle.UnpicklingError) as error:
        print("Unable to restore object:", error)


# 6. Display all saved objects
def display_all_students():
    try:
        with shelve.open(SHELVE_FILE) as database:
            if not database:
                print("No student records available!")
                return

            print("\n----- ALL SAVED STUDENTS -----")

            for key in database:
                student = database[key]

                if isinstance(student, Student):
                    student.display()

    except (OSError, EOFError, pickle.UnpicklingError) as error:
        print("Unable to read database:", error)


# 7. Main menu
def main():
    while True:
        print("\n====== OBJECT PERSISTENCE TOOL ======")
        print("1. Save Object Using Pickle")
        print("2. Restore Object Using Pickle")
        print("3. Save Object Using Shelve")
        print("4. Restore Object Using Shelve")
        print("5. Display All Shelve Records")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            save_with_pickle()

        elif choice == "2":
            load_with_pickle()

        elif choice == "3":
            save_with_shelve()

        elif choice == "4":
            load_with_shelve()

        elif choice == "5":
            display_all_students()

        elif choice == "6":
            print("Exiting Object Persistence Tool. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()