"""
the image feature, key point, detector and descriptor
https://docs.opencv.org/3.4/df/d54/tutorial_py_features_meaning.html
https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html

simplified:
corners are good features 
Harris Corner Detector is good for detecting corners in the image

SIFT - scale invariant feature transform
SIFT is both detector and descriptor

FAST - features from accelerated 
FAST is a detector

BRIEF - Binary robust independent elementary features
BRIEF is a descriptor

ORB - oriented FAST and rotated BRIEF
combined the FAST detector and BRIEF descriptor

"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


def harris_corner():
    img_path = "./images/grains.jpg"
    # note if no second input given in the imread function argument, the numpy
    # array assigned to the img has 3 channels - default color
    # if second arg is set as -1, which means unchanged.
    # the mean from the 2D and 3D matrix are exactly same, which indicates one is
    # derived from the other, possible from 2D to 3D in this case.
    img = cv2.imread(img_path, -1)
    # print(img.shape)
    # print(np.mean(np.mean(img)))
    # read image into 3 channels color image
    img = cv2.imread(img_path)
    # print(img.shape)
    # print(np.mean(np.mean(np.mean(img))))
    # convert the image to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    # print(np.mean(np.mean(gray)))
    # use harris method find corners
    harris = cv2.cornerHarris(gray, 2,3,0.04)
    # highlight the corner is the original image with blue color
    img[harris>0.01*harris.max()] = [255,0,0]
    # show highlighted image
    cv2.imshow("highlight corners",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def tomasi_corner():
    img_path = "./images/grains.jpg"
    img = cv2.imread(img_path, -1)
    # find the corners with tomasi method in opencv
    corners = cv2.goodFeaturesToTrack(img,25,0.01,10)
    corners = np.int0(corners)
    # plot a circle at the coordinate of the corners found
    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)
    cv2.imshow("tomasi corners",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def fast_corner():
    img_path = "./images/grains.jpg"
    img = cv2.imread(img_path, -1)
    # find the corners with FAST method in opencv
    fast = cv2.FastFeatureDetector_create()
    # find and draw the keypoints
    kp = fast.detect(img,None)
    img_corners = cv2.drawKeypoints(img,kp,None,color=(255,0,0))
    # plot corners found
    cv2.imshow("fast corners",img_corners)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def orb_corner():
    img_path = "./images/grains.jpg"
    img = cv2.imread(img_path, -1)
    orb = cv2.ORB_create(50)
    kp, des = orb.detectAndCompute(img,None)
    img_corners = cv2.drawKeypoints(img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # plot corners found
    cv2.imshow("fast corners",img_corners)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
    
if __name__ == "__main__":
    # harris_corner()
    # tomasi_corner()
    # fast_corner()
    orb_corner()


