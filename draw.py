import turtle
import math
t = turtle.Turtle()
screen = turtle.Screen()

# initial settings
screen.bgcolor("black")
t.pensize(6)
t.pencolor('white')
t.speed(4)

# little side of black sun
side = 20

# loop for black sun
for i in range(12):
    t.left(30)
    t.forward(side * 3)
    t.right(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.penup()
    t.goto(0, 0)
    t.pendown()

# drawing circles
t.penup()
t.goto(0, (-4.12) * side)
t.pendown()
t.circle(side * 4.12)
t.penup()
t.goto(0, (-2.06) * side)
t.pendown()
t.circle(side * 2.06)

# calculate pentagram sides
pentagonHalfSide = 4 * side * math.tan((36 * math.pi) / 180) * 1.03
pentagramTriangleSmallSide = pentagonHalfSide / math.cos((72 * math.pi) / 180) * 1.03
pentagramTriangleBigSide = pentagonHalfSide / math.sin((18 * math.pi) / 180)
pentagramFullSide = 2 * pentagonHalfSide + 2 * pentagramTriangleSmallSide
pentagramStartPositionX = 0 - pentagonHalfSide - pentagramTriangleSmallSide
pentagramStartPositionY = 0 - 4 * side * 1.06
circleStartPositionX = 0
circleStartPositionY = 0 - 4 * side - pentagramTriangleBigSide
circleRadius = abs(circleStartPositionY)

# go to initial position for drawing pentagram
t.penup()
t.goto(pentagramStartPositionX, pentagramStartPositionY)
t.pendown()

# draw pentagram
for j in range(5):
    t.forward(pentagramFullSide)
    t.left(144)

# draw circle
t.penup()
t.goto(circleStartPositionX, circleStartPositionY)
t.pendown()
t.circle(circleRadius)

win = turtle.Screen()
win.exitonclick()
