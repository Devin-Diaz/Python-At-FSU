'''
Use the turtle graphics library to write a program that produces the following design:
Audi symbol
'''

import turtle 

turtle.showturtle()

turtle.pensize(10)
turtle.pencolor('blue')
turtle.hideturtle()
turtle.speed(0)

turtle.teleport(-125)
turtle.circle(60)
turtle.right(45)
turtle.penup()

turtle.forward(40)
turtle.pendown()

turtle.circle(60)
turtle.left(60)
turtle.penup()

turtle.forward(120)
turtle.pendown()
turtle.circle(60)

turtle.right(90)
turtle.penup()

turtle.forward(5)
turtle.pendown()
turtle.circle(60)

turtle.left(75)
turtle.penup()
turtle.forward(120)
turtle.pendown()
turtle.circle(60)

turtle.done()