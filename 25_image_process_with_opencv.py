"""
image read, split channel, resize image,
"""
import cv2

img_path = "./images/RGBY.jpg"
img = cv2.imread(img_path, 1)
# note the opencv arrange the color layer as BGR
# check the top left pixel, which is known is blue color
print(img[0,0])
# slice of the blue channel
blue = img[:,:,0]
# show the image
cv2.imshow("blue pixel",blue)
cv2.waitKey(0)
cv2.destroyAllWindows()
# short-cut of split color channels
blue,green,red = cv2.split(img)
# combine the color channel with cv2.merge
img_merged = cv2.merge((blue,green,red))
cv2.imshow("merged",img_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
# resize the image, fx and fy is scaling factor, greater
# than 1 indicates scale it larger, interpolation is algorithm to calculate
# the brightness in the scaled image
resized = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Original",img)
cv2.imshow("Resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

