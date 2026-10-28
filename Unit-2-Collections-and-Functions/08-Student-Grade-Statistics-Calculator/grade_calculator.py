# Program: Class Performance Analyzer Using *args and **kwargs


# Function to calculate the letter grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


# Function to calculate performance metrics using *args and **kwargs
def analyze_performance(*args, **kwargs):
    if not args:
        return None, None, None, {}

    # Convert marks to float for calculations
    marks = list(args)

    # Calculate minimum, maximum, and average marks
    minimum = min(marks)
    maximum = max(marks)
    average = sum(marks) / len(marks)

    # Calculate letter grade distribution
    grade_distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for score in marks:
        grade = calculate_grade(score)
        grade_distribution[grade] += 1

    # Display additional keyword arguments
    print("\n========== ASSESSMENT DETAILS ==========")

    if kwargs:
        for key, value in kwargs.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("No additional assessment details provided.")

    # Return multiple values as a tuple
    return minimum, maximum, average, grade_distribution


# Main program
print("========== CLASS PERFORMANCE ANALYZER ==========")

while True:
    try:
        count = int(input("\nEnter the number of assessment grades: "))

        if count <= 0:
            print("Please enter a positive number.")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter an integer.")


# Accept assessment grades
grades = []

for i in range(count):
    while True:
        try:
            score = float(input(f"Enter marks for assessment {i + 1} (0-100): "))

            if 0 <= score <= 100:
                grades.append(score)
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a numeric mark.")


# Accept additional information
student_name = input("\nEnter student or class name: ").strip()
subject = input("Enter subject name: ").strip()
semester = input("Enter semester: ").strip()

# Call the function using *args and **kwargs
minimum, maximum, average, distribution = analyze_performance(
    *grades,
    student_name=student_name or "Not specified",
    subject=subject or "Not specified",
    semester=semester or "Not specified"
)


# Display the results
print("\n========== PERFORMANCE REPORT ==========")
print(f"Assessment Grades: {grades}")
print(f"Minimum Marks: {minimum}")
print(f"Maximum Marks: {maximum}")
print(f"Average Marks: {average:.2f}")

print("\n========== LETTER GRADE DISTRIBUTION ==========")

for grade, frequency in distribution.items():
    print(f"Grade {grade}: {frequency} assessment(s)")

print("\nAnalysis completed successfully!")

