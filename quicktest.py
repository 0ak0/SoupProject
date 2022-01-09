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
