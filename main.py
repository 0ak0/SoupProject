from PIL import Image, EpsImagePlugin
from turtle import Screen, Turtle
import random
import shutil

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

print("Color 1 is: " + str(colorchoices[0]) + ", " + str(colorchoices[1]) + ", " + str(colorchoices[2]))
print("Color 2 is: " + str(colorchoices[3]) + ", " + str(colorchoices[4]) + ", " + str(colorchoices[5]))
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
preconvertbg.save("temp/background_convert.png", format("png"))

bgresize = Image.open("temp/background_convert.png")
size = (1080, 1080)
bgresized = bgresize.resize(size)
bgresized.save("temp/background_convert.png", format("png"))

#  set the background, pick a can color, and layer all correctly
bg = Image.open("ref/1080.png").convert("RGBA")
back = Image.open("temp/background_convert.png").convert("RGBA")
top = Image.open("ref/Top.png").convert("RGBA")
can = Image.open("ref/Body.png").convert("RGBA")

shutil.copy("ref/Body.png", "temp/Body.png")
newcan = Image.open("temp/Body.png")

cid = can.getdata()

cancolorlist = []

addition = 0

for i in range(256):
    cancolorlist.append(addition)
    addition += 1

cancolor = []

for x in range(3):
    cancolor.append(random.choice(cancolorlist))

for i in range(0, 1080):  # process all pixels
    for j in range(0, 1080):
        data = newcan.getpixel((i, j))
        if data[0] >= 200 and data[1] >= 200 and data[2] >= 200: # use >= 200 just because it works better(tm)
            newcan.putpixel((i, j), (cancolor[0], cancolor[1], cancolor[2]))

print("Can Color is: " + str(cancolor[0]) + ", " + str(cancolor[1]) + ", " + str(cancolor[2]))

newcan.save("temp/newcan.png", format="png")

newcan = Image.open("temp/newcan.png").convert("RGBA")
shade = Image.open("ref/Shading.png").convert("RGBA")
bottom = Image.open("ref/Bottom.png").convert("RGBA")

bg.paste(back, (0, 0), back)
bg.paste(bottom, (0, 0), bottom)
bg.paste(newcan, (0, 0), newcan)
bg.paste(shade, (0, 0), shade)
bg.paste(top, (0, 0), top)
bg.show()

print("Finished!")
