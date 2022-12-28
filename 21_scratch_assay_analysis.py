from skimage.filters.rank import entropy
import matplotlib.pyplot as plt
from skimage.morphology import disk
from skimage import io
import numpy as np
from skimage.filters import threshold_otsu
import glob

time = 0
time_list = []
area_list = []
path = 'images/scratch_assay/*.jpg'

for file in glob.glob(path):
    img =io.imread(file)
    entropy_img = entropy(img, disk(10))
    threshold = threshold_otsu(entropy_img)
    # print(threshold)
    binary = entropy_img <= threshold
    area = np.sum(binary==True)
    area_list.append(area)
    time_list.append(time)
    time += 1
# print(area_list)
plt.plot(time_list,area_list,'bo')


# print(area)
# fig, axes = plt.subplots(4,2,sharey=True, sharex=True, figsize=(10, 8))
# ax = axes.ravel()
# ax[0].imshow(img)
# ax[0].set_title("Original image")
# ax[1].imshow(entropy_img)
# ax[1].set_title("entropy image")
# ax[2].imshow(binary)
# ax[2].set_title("Binary image")
plt.show()
