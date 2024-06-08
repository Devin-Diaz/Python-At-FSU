'''
Use the turtle graphics library to write a program that produces the following design:
2 diamonds touching side by side 
'''

import turtle

turtle.pensize(10)
turtle.pencolor('red')
turtle.hideturtle()
turtle.speed(0)

turtle.teleport(-325)
turtle.left(45)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

turtle.teleport(-42.16,0.00)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)


turtle.done()
