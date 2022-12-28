from PIL import Image
import numpy as np

img = Image.open("images/test_image.jpg")
print(img.format)
print(img.size)
print(img.mode)

## resize
small_img = img.resize((200,300))
small_img.save("images/test_image_small.jpg")

## thumbnail
img.thumbnail((200,300))
img.save("images/test_image_thumbnail.jpg")
print(img.size)

## crop
img = Image.open("images/test_image.jpg")
cropped_img = img.crop((0,0,300,300))
cropped_img.save("images/cropped_img.jpg")

## copy paste
img1 = Image.open("images/test_image.jpg")
print(img1.size)
img2 = Image.open("images/cropped_img.jpg")
print(img2.size)

img1_copy = img1.copy()
img1_copy.paste(img2,(50,50))
img1_copy.save("images/pasted_image.jpg")

## rotation
img = Image.open("images/test_image.jpg")
img_90 = img.rotate(90)
img_90.show()
img_45 = img.rotate(45)
img_45.show()
img_45_expand = img.rotate(45, expand=True)
img_45_expand.show()

## transpose
img_flipLR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipLR.show()

## gray
gray_img = img.convert("L")
gray_img.show()

## glob
import glob
path = "images/aeroplane/*"
for file in glob.glob(path):
    print(file)
    a = Image.open(file)
    rotated45 = a.rotate(45,expand=True)
    rotated45.show()