"""
显微镜下拍照，抹片上是细胞，用手指将抹片中间部分细胞抹去，一段时间后观察，发现抹平部分逐渐缩小。为计算缩小的速率，需要计算每一张照片中抹平部分的面
积。
因为照片中抹平的部分和有细胞覆盖的部分颜色基本一直，所以不能从histogr中查找，只能用两者在纹理上的差别进行区分。
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import try_all_threshold
from skimage.filters import threshold_otsu

img = io.imread("images/scratch.jpg")
entr_img = entropy(img, disk(3))
# plt.imshow(entr_img, cmap='gray')

# check which threshold filter/method gives the best result
fig, ax = try_all_threshold(entr_img, figsize=(10,8), verbose=False)
plt.show()

# from the figure plotted, it is found that Otsu gives reasonable result
thresh = threshold_otsu(entr_img)
print(thresh)
binary = entr_img<=thresh
plt.imshow(binary,cmap='gray')
plt.show()
print("The percentage of white pixel is: {}%".format(100*np.sum(binary==1)/(np.sum(binary==1)+np.sum(binary==0))))
