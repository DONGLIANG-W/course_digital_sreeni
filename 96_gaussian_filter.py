from skimage import io, img_as_float
from skimage.filters import gaussian
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_gaussian = img_as_float(io.imread('./images/BSE_Google_noisy.jpg'))
img_salt = img_as_float(io.imread('./images/BSE_salt_pepper.jpg'))

img = img_gaussian
gaussian_kernel = np.array([[1/16, 1/8, 1/16],
                            [1/8, 1/4, 1/8],
                            [1/16, 1/8, 1/16]])
con_cv2 = cv2.filter2D(img, -1, gaussian_kernel, borderType=cv2.BORDER_CONSTANT)
# gaussian using cv2
gaussian_use_cv2 = cv2.GaussianBlur(img, (3,3), 0, borderType=cv2.BORDER_CONSTANT)
# using skimage gaussian
gaussian_use_skimage = gaussian(img, sigma=1, mode='constant', cval=0.0)

fig, axis = plt.subplots(1,3)
axis[0].imshow(con_cv2)
axis[1].imshow(gaussian_use_cv2)
axis[2].imshow(gaussian_use_skimage)
plt.show()






