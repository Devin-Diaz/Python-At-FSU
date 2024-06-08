import turtle

TOTAL_SQUARES = 200
SIZE_INCREMENT = 20
STARTING_SIZE = 20

turtle.speed(0)

for i in range(TOTAL_SQUARES):
    size = STARTING_SIZE + i * SIZE_INCREMENT

    turtle.penup()
    turtle.goto(-size / 2, size / 2)
    turtle.pendown()
    
    # Draw the square
    for j in range(4):
        turtle.forward(size)
        turtle.right(90)

turtle.mainloop()