from skimage import io, img_as_float
from skimage.filters import gaussian
import cv2
import numpy as np


img = img_as_float(io.imread('./images/BSE_Google_noisy.jpg'))
img_salt = img_as_float(io.imread('./images/BSE_salt_pepper.jpg'))

img = img


