from dom import DOM
import cv2


img_1 = cv2.imread('images/BSE_Google.jpg', 1)
img_2 = cv2.imread('images/BSE_1sigma_blur.jpg', 1)
img_3 = cv2.imread('images/BSE_2sigma_blur.jpg', 1)
img_4 = cv2.imread('images/BSE_3sigma_blur.jpg', 1)
img_5 = cv2.imread('images/BSE_10sigma_blur.jpg', 1)

iqa = DOM()

score1 = iqa.get_sharpness(img_1)
score2 = iqa.get_sharpness(img_2)
score3 = iqa.get_sharpness(img_3)
score4 = iqa.get_sharpness(img_4)
score5 = iqa.get_sharpness(img_5)

print("sharpness for reference image 1: {:.2f},"
      "sharpness for reference image 2: {:.2f},"
      "sharpness for reference image 3: {:.2f},"
      "sharpness for reference image 4: {:.2f},"
      "sharpness for reference image 5: {:.2f},".format(score1, score2, score3, score4, score5))