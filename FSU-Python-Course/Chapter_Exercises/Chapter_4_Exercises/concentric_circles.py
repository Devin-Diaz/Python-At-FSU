import turtle

TOTAL_CIRCLES = 70
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

radius = STARTING_RADIUS

for x in range(TOTAL_CIRCLES):
    turtle.circle(radius)
    x = turtle.xcor() 
    y = turtle.ycor() - OFFSET
    radius += OFFSET

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.mainloop()