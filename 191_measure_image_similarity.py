from skimage.metrics import structural_similarity
import cv2


def orb_sim(img1, img2):
    orb = cv2.ORB_create()
    kp_a, desc_a = orb.detectAndCompute(img1, None)
    kp_b, desc_b = orb.detectAndCompute(img2, None)
    # detect key points and description
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # define the bruteforce matcher object
    matches = bf.match(desc_a, desc_b)
    # perform match
    similar_regions = [i for i in matches if i.distance <50]
    if len(matches) == 0:
        return 0
    return len(similar_regions)/len(matches)

def structural_sim(img1, img2):
    sim, diff =structural_similarity(img1, img2, full=True)
    return sim

img00 = cv2.imread('images/monkey.jpg',0)
img11 = cv2.imread('images/monkey_distorted.jpg',0)

orb_similarity = orb_sim(img00,img11)
structural_similarity = structural_sim(img00,img11)

print("Similarity using ORB is :{}".format(orb_similarity))
print("Similarity using structural is :{}".format(structural_similarity))
