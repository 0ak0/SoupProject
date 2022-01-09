from turtle import Screen, Turtle
import random

addition = 0
colorlist = []
for i in range(256):
    colorlist.append(addition)
    addition += 1

colorchoices = []

for x in range(6):
    colorchoices.append(random.choice(colorlist))

print("Color 1 is : " + str(colorchoices[0]) + " " + str(colorchoices[1]) + " " + str(colorchoices[2]))
print("Color 2 is : " + str(colorchoices[3]) + " " + str(colorchoices[4]) + " " + str(colorchoices[5]))

topcolor = (colorchoices[0] / 255, colorchoices[1] / 255, colorchoices[2] / 255)
bottomcolor = (colorchoices[3] / 255, colorchoices[4] / 255, colorchoices[5] / 255)
screen = Screen()
height = screen.window_height()
width = screen.window_width()


#class CreateBackground:

deltas = [(hue - topcolor[index]) / height for index, hue in enumerate(bottomcolor)]

turtle = Turtle()
turtle.color(topcolor)
turtle.speed(0)
turtle.penup()
turtle.goto(-width / 2, height / 2)
turtle.pendown()

direction = 1

"""for distance, y in enumerate(range(height // 2, -height // 2, -1)):
    turtle.forward(width * direction)
    turtle.color([topcolor[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1"""

for distance, y in enumerate(range(height // 2, -height // 2, -1)):
    turtle.forward(width * direction)
    turtle.color([topcolor[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

turtle.getscreen().getcanvas().postscript(file="temp/background.ps")
screen.exitonclick()
