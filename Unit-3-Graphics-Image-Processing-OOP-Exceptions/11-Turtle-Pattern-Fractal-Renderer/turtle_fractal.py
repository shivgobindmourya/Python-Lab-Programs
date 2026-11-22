# Program: Fractal and Geometric Pattern Generator
# Library: turtle, math, colorsys

import turtle
import math
import colorsys


# Create and configure the screen
screen = turtle.Screen()
screen.title("Fractal and Geometric Pattern Generator")
screen.setup(width=1000, height=750)
screen.bgcolor("black")
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()


# Generate rainbow colors
def get_color(index, total):
    hue = (index % total) / total
    return colorsys.hsv_to_rgb(hue, 1, 1)


# Configure drawing position
def reset_pen(x=0, y=0):
    pen.clear()
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(0)
    screen.bgcolor("black")


# 1. Koch Snowflake
def koch_curve(length, depth):
    if depth == 0:
        pen.forward(length)
    else:
        length /= 3

        koch_curve(length, depth - 1)
        pen.left(60)

        koch_curve(length, depth - 1)
        pen.right(120)

        koch_curve(length, depth - 1)
        pen.left(60)

        koch_curve(length, depth - 1)


def draw_koch_snowflake():
    reset_pen(-180, 100)
    pen.pensize(2)

    for i in range(3):
        pen.color(get_color(i, 3))
        koch_curve(360, 3)
        pen.right(120)

    screen.update()


# 2. Recursive Tree
def draw_branch(length, depth):
    if depth == 0 or length < 3:
        return

    pen.pensize(max(1, depth))
    pen.color(get_color(depth, 10))
    pen.forward(length)

    pen.left(30)
    draw_branch(length * 0.7, depth - 1)

    pen.right(60)
    draw_branch(length * 0.7, depth - 1)

    pen.left(30)
    pen.backward(length)


def draw_recursive_tree():
    reset_pen(0, -280)
    pen.setheading(90)
    pen.pensize(8)

    draw_branch(140, 9)
    screen.update()


# 3. Sierpinski Triangle
def sierpinski(points, depth):
    if depth == 0:
        pen.penup()
        pen.goto(points[0])
        pen.pendown()

        pen.goto(points[1])
        pen.goto(points[2])
        pen.goto(points[0])
        return

    p1, p2, p3 = points

    mid1 = midpoint(p1, p2)
    mid2 = midpoint(p2, p3)
    mid3 = midpoint(p3, p1)

    sierpinski([p1, mid1, mid3], depth - 1)
    sierpinski([mid1, p2, mid2], depth - 1)
    sierpinski([mid3, mid2, p3], depth - 1)


def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2,
            (p1[1] + p2[1]) / 2)


def draw_sierpinski_triangle():
    reset_pen(-250, -180)
    pen.pensize(1)

    points = [(-250, -180), (250, -180), (0, 253)]

    pen.color("cyan")
    sierpinski(points, 5)
    screen.update()


# 4. Logarithmic Spiral
def draw_logarithmic_spiral():
    reset_pen(0, 0)
    pen.pensize(3)

    for angle in range(0, 1440):
        radius = 0.12 * angle
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))

        pen.color(get_color(angle, 360))
        pen.goto(x, y)

    screen.update()


# 5. Geometric Pattern
def draw_geometric_pattern():
    reset_pen(0, 0)
    pen.pensize(2)

    for i in range(36):
        pen.color(get_color(i, 36))

        for _ in range(4):
            pen.forward(150)
            pen.right(90)

        pen.right(10)

    screen.update()


# 6. Star Pattern
def draw_star_pattern():
    reset_pen(0, 0)
    pen.pensize(2)

    for i in range(36):
        pen.color(get_color(i, 36))

        for _ in range(5):
            pen.forward(200)
            pen.right(144)

        pen.right(10)

    screen.update()


# 7. Change background using RGB values
def change_rgb_background():
    try:
        red = int(input("Enter Red value (0-255): "))
        green = int(input("Enter Green value (0-255): "))
        blue = int(input("Enter Blue value (0-255): "))

        if not all(0 <= value <= 255
                   for value in (red, green, blue)):
            print("RGB values must be between 0 and 255.")
            return

        screen.bgcolor(
            red / 255,
            green / 255,
            blue / 255
        )

        screen.update()
        print("Background color changed successfully!")

    except ValueError:
        print("Please enter valid integer RGB values.")


# Main menu
def main():
    while True:
        print("\n====== FRACTAL AND PATTERN GENERATOR ======")
        print("1. Koch Snowflake")
        print("2. Recursive Tree")
        print("3. Sierpinski Triangle")
        print("4. Logarithmic Spiral")
        print("5. Geometric Pattern")
        print("6. Star Pattern")
        print("7. Custom RGB Background")
        print("8. Clear Screen")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            draw_koch_snowflake()

        elif choice == "2":
            draw_recursive_tree()

        elif choice == "3":
            draw_sierpinski_triangle()

        elif choice == "4":
            draw_logarithmic_spiral()

        elif choice == "5":
            draw_geometric_pattern()

        elif choice == "6":
            draw_star_pattern()

        elif choice == "7":
            change_rgb_background()

        elif choice == "8":
            pen.clear()
            screen.bgcolor("black")
            screen.update()
            print("Screen cleared successfully!")

        elif choice == "9":
            print("Exiting Pattern Generator. Goodbye!")
            screen.bye()
            break

        else:
            print("Invalid choice! Select a number from 1 to 9.")


if __name__ == "__main__":
    main()
