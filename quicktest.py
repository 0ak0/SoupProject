from PIL import Image

img = Image.open("ref/Body.png")
cid = img.getdata()

new_image = []
for item in cid:

    if item[0] in list(range(200, 256)):
        new_image.append((255, 224, 100))
    else:
        new_image.append(item)

# update image data
img.putdata(new_image)


# save new image
img.show()