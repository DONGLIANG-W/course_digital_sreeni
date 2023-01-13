import cv2
import numpy as np
from matplotlib import pyplot as plt

def denoise_img():
    # read the image
    img_path = "./images/BSE_Google_noisy.jpg"
    img = cv2.imread(img_path,1)
    # define a kernel
    # here we have a 5X5 kernel, and average the brightness in the kernel window
    kernel=np.ones((3,3), np.float32)/9
    # convolve the kernel with the image
    filt_2D = cv2.filter2D(img, -1, kernel)
    # blur the image with cv2.blur func
    blur = cv2.blur(img,(3,3))
    # Gaussian blur
    gaussian_blur = cv2.GaussianBlur(img, (5,5), 0)
    # median filter
    median_blur = cv2.medianBlur(img, 3)
    # bilateral blur
    bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)
    # show the image
    cv2.imshow("original", img)
    cv2.imshow("customize filtered", filt_2D)
    cv2.imshow("blur", blur)
    cv2.imshow("Gaussian blur", gaussian_blur)
    cv2.imshow("median blur", median_blur)
    cv2.imshow("bilateral blur", bilateral_blur)
    # close the figure window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def edge_detect():
    # read the image
    img_path = "./images/Neuron.jpg"
    img = cv2.imread(img_path, 0)
    # canny edge detection
    # canny edge func second and third input are the min, max limit
    # the limit is about the hypothesis of the two level thresholding
    edges = cv2.Canny(img, 100, 200)

    # show image
    cv2.imshow("original", img)
    cv2.imshow("Canny edge", edges)
    # close the figure window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
#     denoise_img()
    edge_detect()