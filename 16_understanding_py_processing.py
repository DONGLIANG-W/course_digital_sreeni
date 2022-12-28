from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_float

my_image = io.imread('images/test_image.jpg')
print(my_image)
print(my_image.min(), my_image.max())
plt.imshow(my_image)
plt.show()

my_image[10:200, 10:200, :] = [255, 255, 0]
plt.imshow(my_image)
plt.show()