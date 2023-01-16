import cv2
import numpy as np
import matplotlib.pyplot as plt


def threshold_with_opencv():
    # read the image
    img_path = "./images/BSE_Google_noisy.jpg"
    img = cv2.imread(img_path, -1)
    # plot the histogram
    # plt.hist(img, bins=100, range=(0,255))
    # plt.show()
    # get the threshold and binary image threshold with the ostu method
    ret, img_threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # remove the salt and pepper noise
    img_thresh_median = cv2.medianBlur(img_threshold,3)
    # show the image
    cv2.imshow("original",img)
    cv2.imshow("OTSU thresholding image",img_threshold)
    cv2.imshow("median filtered binary", img_thresh_median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return [img_threshold, img_thresh_median]


def morphological_process(img_threshold):
    # dilation - adding
    # erosion - reducing
    kernel = np.ones((3,3), np.uint8)
    iternation_cycle = 1
    erosion = cv2.erode(img_threshold,kernel,iterations=iternation_cycle)
    dilation = cv2.dilate(erosion,kernel,iterations=iternation_cycle)
    # opening and closing
    opening = cv2.morphologyEx(img_threshold, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img_threshold, cv2.MORPH_CLOSE, kernel)
    # show image
    cv2.imshow("binary",img_threshold)
    cv2.imshow("erosion",erosion)
    cv2.imshow("dilation",dilation)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 


if __name__ == "__main__":
    img_binary, denoised_binary = threshold_with_opencv()
    morphological_process(denoised_binary)