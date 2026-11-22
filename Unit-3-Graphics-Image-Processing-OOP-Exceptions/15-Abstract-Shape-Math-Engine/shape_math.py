from abc import ABC, abstractmethod
import math


# 1. Abstract Base Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# 2. Vector Class
class Vector(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Vector addition using operator overloading
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    # Compare two vectors
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    # Compare vector magnitudes
    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return self.magnitude() < other.magnitude()

    # Calculate vector magnitude
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Dot product
    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Dot product requires another Vector.")

        return self.x * other.x + self.y * other.y

    # Implement abstract methods
    def area(self):
        return 0

    def perimeter(self):
        return 0

    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# 3. Circle Class
class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")

        self.radius = radius

    # Add circle areas
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        # Return a circle with the combined area
        combined_area = self.area() + other.area()
        new_radius = math.sqrt(combined_area / math.pi)

        return Circle(new_radius)

    # Compare circles by area
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return self.area() < other.area()

    # Calculate area
    def area(self):
        return math.pi * self.radius ** 2

    # Calculate circumference
    def perimeter(self):
        return 2 * math.pi * self.radius

    # String representation
    def __str__(self):
        return f"Circle(radius={self.radius:.2f})"


# 4. Demonstrate Polymorphism
def display_shape(shape):
    print("\nShape:", shape)
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")


# 5. Main Program
def main():

    while True:
        print("\n====== ABSTRACT GEOMETRIC FRAMEWORK ======")
        print("1. Create and Display a Vector")
        print("2. Add Two Vectors")
        print("3. Compare Two Vectors")
        print("4. Calculate Vector Dot Product")
        print("5. Create and Display a Circle")
        print("6. Add Two Circles")
        print("7. Compare Two Circles")
        print("8. Demonstrate Polymorphism")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":
                x = float(input("Enter x component: "))
                y = float(input("Enter y component: "))

                vector = Vector(x, y)

                print("Vector:", vector)
                print(f"Magnitude: {vector.magnitude():.2f}")

            elif choice == "2":
                x1 = float(input("Enter first vector x: "))
                y1 = float(input("Enter first vector y: "))
                x2 = float(input("Enter second vector x: "))
                y2 = float(input("Enter second vector y: "))

                v1 = Vector(x1, y1)
                v2 = Vector(x2, y2)

                print("First Vector:", v1)
                print("Second Vector:", v2)
                print("Vector Sum:", v1 + v2)

            elif choice == "3":
                x1 = float(input("Enter first vector x: "))
                y1 = float(input("Enter first vector y: "))
                x2 = float(input("Enter second vector x: "))
                y2 = float(input("Enter second vector y: "))

                v1 = Vector(x1, y1)
                v2 = Vector(x2, y2)

                print("First Vector:", v1)
                print("Second Vector:", v2)
                print("Vectors Equal:", v1 == v2)
                print("First Vector Smaller:", v1 < v2)

            elif choice == "4":
                x1 = float(input("Enter first vector x: "))
                y1 = float(input("Enter first vector y: "))
                x2 = float(input("Enter second vector x: "))
                y2 = float(input("Enter second vector y: "))

                v1 = Vector(x1, y1)
                v2 = Vector(x2, y2)

                print("Dot Product:", v1.dot(v2))

            elif choice == "5":
                radius = float(input("Enter circle radius: "))

                circle = Circle(radius)
                display_shape(circle)

            elif choice == "6":
                r1 = float(input("Enter first circle radius: "))
                r2 = float(input("Enter second circle radius: "))

                c1 = Circle(r1)
                c2 = Circle(r2)

                print("First Circle:", c1)
                print("Second Circle:", c2)
                print("Combined Area Circle:", c1 + c2)

            elif choice == "7":
                r1 = float(input("Enter first circle radius: "))
                r2 = float(input("Enter second circle radius: "))

                c1 = Circle(r1)
                c2 = Circle(r2)

                print("Circles Equal:", c1 == c2)
                print("First Circle Smaller:", c1 < c2)

            elif choice == "8":
                shapes = [
                    Circle(5),
                    Circle(3),
                    Vector(3, 4),
                    Vector(6, 8)
                ]

                print("\n----- POLYMORPHISM DEMONSTRATION -----")

                for shape in shapes:
                    display_shape(shape)

            elif choice == "9":
                print("Exiting Geometric Framework. Goodbye!")
                break

            else:
                print("Invalid choice! Please select 1-9.")

        except ValueError as error:
            print("Invalid input:", error)

        except TypeError as error:
            print("Operation error:", error)


if __name__ == "__main__":
    main()

