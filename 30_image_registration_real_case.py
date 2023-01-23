"""
1. import 2 images
2. convert to gray images
3. initialize ORB
4. find the keypoints and describe them
5. match keypoints - Brute force matcher
6. RANSAC - reject the bad keypoints
7. Register the 2 images - using homology
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

def img_registration():
    img_path_2 = './images/monkey.jpg'
    img_path_1 = './images/monkey_distorted.jpg'
    # read image
    img1 = cv2.imread(img_path_1, -1)
    img2 = cv2.imread(img_path_2, -1)
    # convert color image to gray
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # initialize ORB
    orb = cv2.ORB_create(50)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    # match the keypoints
    matcher = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_BRUTEFORCE_HAMMING)
    # match the discriptor
    matches = matcher.match(des1, des2, None)
    # sort the matches
    matches = sorted(matches, key=lambda x:x.distance)
    # initilized the empty array of points
    points1 = np.zeros((len(matches),2), dtype=np.float32)
    points2 = np.zeros((len(matches),2), dtype=np.float32)
    for i, match in enumerate(matches):
        points1[i,:] = kp1[match.queryIdx].pt
        points2[i,:] = kp2[match.trainIdx].pt
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
    # use the homograpy
    height, width = img2.shape
    # project the un-distorted image
    img_1_Reg = cv2.warpPerspective(img1, h, (width, height))
    
    # draw the key point on the image
    img3 = cv2.drawKeypoints(img1, kp1, None, flags=None)
    img4 = cv2.drawKeypoints(img2, kp2, None, flags=None)
    img5 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None)
    
    cv2.imshow("Keypoint 1", img3)
    cv2.imshow("Keypoint 2", img4)
    cv2.imshow("Matches", img5)
    cv2.imshow("Registered/un-distorted image", img_1_Reg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    img_registration()

