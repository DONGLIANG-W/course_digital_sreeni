from skimage import io, img_as_float
from skimage.filters import gaussian, median
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_gaussian = img_as_float(io.imread('./images/BSE_Google_noisy.jpg'))
img_salt = io.imread('./images/BSE_salt_pepper.jpg', 0)

img = img_salt
# apply median filter with cv2
median_cv2 = cv2.medianBlur(img, 3)
# apply median with skimage
median_skimage = median(img, mode='constant', cval=0.0)
cv2.imshow('salt and pepper', img)
cv2.imshow('skimage median',median_skimage)
cv2.waitKey()
cv2.destroyAllWindows()


