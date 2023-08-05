"""
object detection by template matching
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img_rgb = cv2.imread('images/f16.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGRA2GRAY)
template = cv2.imread('images/f16_template.jpg', 0)

h, w = template.shape

# use the cv2 module to match between the image and templet. The third input
# is the algorithm that used to do the math
# SQDIFF is square of the difference
# other algorithm available cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED
res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF)
# plot the result, which shows the best matching as low value
plt.imshow(res, cmap='gray')
plt.show()
# get the min max location and value
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# plot a rectangle the best matching on the figure
top_left = min_loc
bottom_right = (top_left[0]+w, top_left[1]+h)
cv2.rectangle(img_gray, top_left, bottom_right, 255, 2)
cv2.imshow('Matched image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# above show draw only the best matching case, user can draw the objects with matching confidence more than 0.8
# or other which make sense
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
plt.imshow(res, cmap='gray')
plt.show()
threshold = 0.4
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)
cv2.imshow('Matched image', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()