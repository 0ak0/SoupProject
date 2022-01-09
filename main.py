from PIL import Image, EpsImagePlugin
from turtle import Screen, Turtle
import random

# import background
# from background import topcolor, bottomcolor, screen, height, width

#  use my jank-ass method of creating a gradient background

#  create a gradient image using turtle
#  find 6 (3 + 3) random values for the rgb of 2 colors
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
print("Turtle has Started!")

topcolor = (colorchoices[0] / 255, colorchoices[1] / 255, colorchoices[2] / 255)
bottomcolor = (colorchoices[3] / 255, colorchoices[4] / 255, colorchoices[5] / 255)
screen = Screen()
#  set up turtle and run it
turt = Turtle()
Screen().setup(1080, 1080)
height = screen.window_height()
width = screen.window_width()
deltas = [(hue - topcolor[index]) / height for index, hue in enumerate(bottomcolor)]

turt.color(topcolor)
turt.speed(0)  # this is as fast as it will go ;-;
turt.penup()
turt.goto(-width / 2, height / 2)
turt.pendown()

direction = 1

for distance, y in enumerate(range(height // 2, -height // 2, -1)):
    turt.forward(width * direction)
    turt.color([topcolor[i] + delta * distance for i, delta in enumerate(deltas)])  # this gives me a warning but works
    turt.sety(y)

    direction *= -1

turt.getscreen().getcanvas().postscript(file="temp/background.ps")
screen.bye()
print("Turtle Finished!")

#  make the gradient image usable
EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs9.55.0\bin\gswin64c'  # Ghostscript path goes here
preconvertbg = Image.open("temp/background.ps")
preconvertbg.save("temp/background_convert.png")

#  create a list of all can colors
cans = ["ref/can/black.png", "ref/can/blue.png", "ref/can/green.png", "ref/can/orange.png", "ref/can/pink.png",
        "ref/can/purple.png", "ref/can/red.png", "ref/can/teal.png", "ref/can/white.png", "ref/can/yellow.png"]
canchoice = random.choice(cans)

#  set the background, pick a can color, and layer all correctly
bg = Image.open("temp/background_convert.png")
top = Image.open("ref/top.png")
can = Image.open(canchoice)
bottom = Image.open("ref/bottom.png")

bg.paste(bottom, (0, 0), bottom)
bg.paste(can, (0, 0), can)
bg.paste(top, (0, 0), top)
bg.show()

print("Finished!")
print("Can Color: " + str(canchoice))
