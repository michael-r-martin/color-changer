from PIL import Image
import numpy as np
img = Image.open("base.jpg")

width = img.size[0]
height = img.size[1]

for i in range(0, width):
    for j in range(0, height):
        data = img.getpixel((i, j))
        if data[0] == 209 and data[1] == 255 and data[2] == 255:
            img.putpixel((i, j), (253, 100, 291))
        if data[0] == 100 and data[1] == 200 and data[2] == 200:
            img.putpixel((i, j), (20, 100, 255))

img.save("newOne.png")
