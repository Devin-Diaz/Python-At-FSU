'''
Write a turtle graphics program that uses the square function presented in Chapter 5 - Slide 66,
along with a loop (or loops) to draw the checkerboard pattern shown below.
'''

import turtle

# window size of 600x600
screen = turtle.Screen()
screen.setup(width=600, height=600)

# creates turtle instance, hides, and speed runs program 
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# board dimensions details 
BOARD_SIZE = 5
SQUARE_SIZE = 100

# draws a square with filled color, provided by Prof Satish 
def square(width: int, color: str) -> None:
    t.fillcolor(color) # Set the fill color
    t.pendown() # Lower the pen
    t.begin_fill() # Start filling
    for _ in range(4): # Draw a square
        t.forward(width)
        t.right(90)
    t.end_fill()

# determines what color to fill the square in based off the indices of the row and column during iterations
def square_color(row: int, col: int) -> str:
    if row % 2 == 0:
        if col % 2 == 0: return 'black'
        else: return 'white'
    else:
        if col % 2 == 0: return 'white'
        else: return 'black'        

# draws a 5x5 chess board 
def draw_board() -> None:

    # Moves our turtle to the top left of the board and preps it to begin drawing the board
    top_left_x = screen.window_width() / 2 
    top_left_y = screen.window_height() / 2  
    t.penup()
    t.goto(top_left_x - 550, top_left_y - 30)

    # tracks initial cordinates where board begins
    x_cordinate = t.xcor()
    y_cordinate = t.ycor()

    # iterates through the dimensions of the board, drawing a square with color and adjusting position
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            square(SQUARE_SIZE, square_color(row, col))
            t.forward(SQUARE_SIZE)
        t.penup()
        y_cordinate -= SQUARE_SIZE
        t.goto(x_cordinate, y_cordinate)

    # finishes program
    turtle.done()

draw_board()