# four modules mainly used for image analysis
# matplotlib, cv2, pillow, scikit-image
import numpy as np
## pillow
from PIL import Image
img = Image.open("images/test_image.jpg")
print(type(img))
# img.show()
print(img.format)
# convert it into numpy matrix
img1 = np.asarray(img)
print(type(img1))

## Matplotlib
#Pyplot
import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
img = mpimg.imread("images/test_image.jpg")
print(type(img))
print(img.shape)
plt.imshow(img)
plt.colorbar()
# plt.show()

## scikit-image
from skimage import io
image = io.imread("images/test_image.jpg")
print(type(image))

## open-cv
import cv2
img = cv2.imread("images/test_image.jpg", 1)
# note the second argument 1 indicates that the image is read into a color image
print(type(img))
cv2.imshow("test image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_gray = cv2.imread("images/test_image.jpg",0)
# note the second argument 0 indicates that the image is read into a gray image
print(img_gray.shape)
cv2.imshow("gray image",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

## to read a bundle of image
# glob
import cv2
import glob
path = "images/test_image/aeroplane/*"
for file in glob.glob(path):
    print(file)
    img = cv2.imread(file)
    print(img)
    color_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()