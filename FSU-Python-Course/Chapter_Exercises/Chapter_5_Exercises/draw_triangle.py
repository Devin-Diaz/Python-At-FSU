import turtle

def triangle(x1, y1, x2, y2, x3, y3, color):
    """
    Draws a triangle with the given vertices and fill color.

    Parameters:
    x1, y1: Coordinates of the first vertex.
    x2, y2: Coordinates of the second vertex.
    x3, y3: Coordinates of the third vertex.
    color: The fill color of the triangle.
    """
    pen = turtle.Turtle()
    pen.speed(1)  # You can adjust the speed (0 is the fastest, 1 is slow)

    # Move to the first vertex
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()

    # Set the fill color
    pen.fillcolor(color)

    # Start filling
    pen.begin_fill()

    # Draw the triangle
    pen.goto(x2, y2)
    pen.goto(x3, y3)
    pen.goto(x1, y1)

    # End filling
    pen.end_fill()

    # Hide the turtle after drawing
    pen.hideturtle()

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Draw a Triangle with Turtle")

# Demonstrate the triangle function
triangle(-100, 0, 0, 100, 100, 0, "blue")

# Keep the window open until the user closes it
turtle.done()
