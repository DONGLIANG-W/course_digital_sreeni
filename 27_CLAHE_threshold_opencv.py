"""
Process the low contrast image, use CLAHE to stretch the histogram distribution
create binary image from the local adaptive histogram equalized image
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_clahe():
    img_path = "./images/Alloy.jpg"
    img = cv2.imread(img_path, -1)
    print(img.shape)
    # equalize the histogram
    eq_img = cv2.equalizeHist(img)
    # using the clahe
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_img = clahe.apply(img)
    # show image
    cv2.imshow("original",img)
    cv2.imshow("global histogram equalized",eq_img)
    cv2.imshow("localized adaptive histogram equalized",clahe_img)
    # close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    plot the histogram
    fig, axes = plt.subplots(1,3, tight_layout=True)
    ax = axes.ravel()
    ax[0].hist(img, bins=100)
    ax[1].hist(eq_img, bins=100)
    ax[2].hist(clahe_img, bins=100)
    plt.show()
    # from the histogram, define threshold = 190
    # with 190 as the threshold, plot the image with pixel brightness lower than threshold
    ret1, threshold1 = cv2.threshold(clahe_img, 190, 150, cv2.THRESH_BINARY)
    # with 190 as the threshold, plot the image with pixel brighter
    ret2, threshold2 = cv2.threshold(clahe_img, 190, 255, cv2.THRESH_BINARY_INV)
    # with Otsu threshold method, auto define threshold
    ret3, threshold3 = cv2.threshold(clahe_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # show image
    cv2.imshow("original",img)
    cv2.imshow("binary threshold 1",threshold1)
    cv2.imshow("binary threshold 2 inverted", threshold2)
    cv2.imshow("otsu threshold",threshold3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


if __name__ == "__main__":

    get_clahe()
