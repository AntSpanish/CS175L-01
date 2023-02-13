import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 360/NUM_SIDES
t=turtle.Turtle()

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Turtle commands
t.ht()
t.penup()
t.goto(-50,120)
t.pendown()

#First octagon
for z in range(NUM_SIDES):
    t.fd(LENGTH)
    t.rt(ANGLE)

t.penup()
t.goto(-48,114)
t.pendown()

#Re-adjust length
LENGTH=95

#Color for octagon 2
t.begin_fill()
t.fillcolor('red')
t.pencolor('red')

#Second octagon within octagon 1
for z in range(NUM_SIDES):
    t.fd(LENGTH)
    t.rt(ANGLE)
t.end_fill()

#Text
t.penup()
t.goto(0,-50)
t.pendown()
t.color('white')
style=('Highway Gothic', 60, 'bold')
t.write('STOP',font=style,align='center')
t.done()
