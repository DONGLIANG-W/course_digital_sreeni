from scipy import misc
from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

## read image
img = io.imread("test_image.jpg")
print(img.dtype, img.shape)

img_gray = io.imread("test_image.jpg", as_gray=True)
print(img_gray.dtype, img_gray.shape)

## image array slicing
print(img[0,0])
print(img[10:15, 20:25])

mean_gray = img.mean()
max_value = img.max()
min_value = img.min()

print("Min, Max and Mean are: {0}, {1}, {2:5.3f}".format(min_value,max_value,mean_gray))
# note the argument in {}, the 0,1,2 referring to the sequence number of the variable
print("Min, Max and Mean are: %d, %d, %5.3f" %(min_value,max_value,mean_gray))
# note the argument is not compusory

## scipy ndimage
img = img_as_ubyte(io.imread("test_image.jpg", as_gray=False))
print(type(img), img.shape)
flippedLR = np.fliplr(img)
flippedUD = np.flipud(img)

# plot image
# plt.subplot(2,2,1)
# note above plt.subplot argument(2 rows, 2 column, the image is shown in the first position)
plt.subplot(2,1,1)
# note the second argument is 1, means 2 rows, 1 column, the image is shown in middle
plt.imshow(img)
plt.subplot(2,2,3)
# note above plt.subplot argument(2 rows, 2 column, the image is shown in the third position)
plt.imshow(flippedLR)
plt.subplot(2,2,4)
plt.imshow(flippedUD)
plt.show()

## scipy ndimage.rotate
rotated_img = ndimage.rotate(img,45)
plt.imshow(rotated_img)
plt.show()

## ndimage.uniform_filter
uniform_filtered_img = ndimage.uniform_filter(img, size=9)
plt.imshow(uniform_filtered_img)
plt.show()


## ndimage.gaussian_filter
gaussian_filtered_img = ndimage.gaussian_filter(img, sigma=3)
plt.imshow(gaussian_filtered_img)
plt.show()

# ndimage.median_filter
median_filtered_img = ndimage.median_filter(img, 3)
plt.imshow(median_filtered_img)
plt.show()

## sobel filter
sobel_img = ndimage.sobel(img, axis=0)
plt.imshow(sobel_img)
plt.show()