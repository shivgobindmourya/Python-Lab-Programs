# Program: Matrix Transformation Using Functional Programming

# Original matrix represented as a 2D list
matrix = [
    [12, -5, 8],
    [3, 15, -2],
    [10, 6, 20]
]

# Original data represented as tuples
data = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 95),
    ("David", 60),
    ("Eva", 88)
]


# Function 1: Display the original matrix
def display_matrix(matrix):
    for row in matrix:
        print(row)


# Function 2: Remove negative values using filter()
def remove_negative_values(matrix):
    return [
        list(filter(lambda x: x >= 0, row))
        for row in matrix
    ]


# Function 3: Transform matrix elements using map()
def transform_matrix(matrix):
    return [
        list(map(lambda x: x * 2, row))
        for row in matrix
    ]


# Function 4: Sort all matrix elements
def sort_matrix_elements(matrix):
    elements = [
        element
        for row in matrix
        for element in row
    ]

    return sorted(elements)


# Function 5: Sort matrix rows by their sum
def sort_rows_by_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))


# Function 6: Filter tuples based on marks
def filter_students(data, minimum_marks):
    return list(
        filter(lambda student: student[1] >= minimum_marks, data)
    )


# Function 7: Sort tuples by marks in descending order
def sort_students(data):
    return sorted(data, key=lambda student: student[1], reverse=True)


# Function 8: Extract student marks using map()
def extract_marks(data):
    return list(map(lambda student: student[1], data))


# Main program
print("========== ORIGINAL MATRIX ==========")
display_matrix(matrix)

print("\n========== MATRIX WITHOUT NEGATIVE VALUES ==========")
clean_matrix = remove_negative_values(matrix)
display_matrix(clean_matrix)

print("\n========== MATRIX ELEMENTS MULTIPLIED BY 2 ==========")
modified_matrix = transform_matrix(matrix)
display_matrix(modified_matrix)

print("\n========== SORTED MATRIX ELEMENTS ==========")
print(sort_matrix_elements(matrix))

print("\n========== MATRIX ROWS SORTED BY SUM ==========")
print(sort_rows_by_sum(matrix))

print("\n========== ORIGINAL STUDENT RECORDS ==========")
for student in data:
    print(student)

print("\n========== STUDENTS WITH MARKS >= 80 ==========")
print(filter_students(data, 80))

print("\n========== STUDENTS SORTED BY MARKS ==========")
for student in sort_students(data):
    print(student)

print("\n========== EXTRACTED STUDENT MARKS ==========")
print(extract_marks(data))

