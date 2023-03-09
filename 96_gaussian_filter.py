from skimage import io, img_as_float
from skimage.filters import gaussian
import cv2
import numpy as np


img_gaussian = img_as_float(io.imread('./images/BSE_Google_noisy.jpg'))
img_salt = img_as_float(io.imread('./images/BSE_salt_pepper.jpg'))

img = img_gaussian
gaussian_kernel = np.array([[1/16, 1/8, 1/16],
                            [1/8, 1/4, 1/8],
                            [1/16, 1/8, 1/16]])
con_cv2 = cv2.filter2D(img, -1, gaussian_kernel, borderType=cv2.BORDER_CONSTANT)





