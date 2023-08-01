"""shading correction, non-uniform illumination correction"""
import cv2
import numpy as np
from cv2_rolling_ball import subtract_background_rolling_ball
from matplotlib import pyplot as plt

# CLAHE method
img = cv2.imread('images/Alloy_gradient.jpg', 1)
lab_img = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)
l, a, b = cv2.split(lab_img)

clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
clahe_img = clahe.apply(l)
CLAHE_img = cv2.merge((clahe_img, a, b))

corrected_img = cv2.cvtColor(CLAHE_img, cv2.COLOR_Lab2RGB)

cv2.imshow('original image', img)
cv2.imshow('Corrected image', corrected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == "__main__":
    # using rolling ball method
    img = cv2.imread('images/Alloy_gradient.jpg', 0)
    radius = 30
    final_img, background = subtract_background_rolling_ball(img, radius, light_background=True, use_paraboloid=False,
                                                             do_presmooth=True)
    cv2.imshow('Background', background)
    cv2.imshow('After background subtraction', final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # the final image does not seems very good looking although the background is now uniform, using CLAHE
    clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8, 8))
    clahe_img = clahe.apply(final_img)
    cv2.imshow('After background subtraction', final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

