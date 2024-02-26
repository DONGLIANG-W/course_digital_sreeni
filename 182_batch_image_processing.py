import cv2
import glob
from skimage.filters import gaussian
from skimage import img_as_ubyte
import os
import numpy as np
import shutil


# practice 1
path = '/home/orangepi/PycharmProjects/course_digital_sreeni/images/scratch_assay/*.*'
for file in glob.glob(path):
    # print(file)
    # print(os.path.basename(file))
    file_name = os.path.basename(file)
    img = cv2.imread(file, 0)

    img_smooth = img_as_ubyte(gaussian(img, sigma=5, mode='constant', cval=0))
    cv2.imwrite('/home/orangepi/PycharmProjects/course_digital_sreeni/images/scratch_assay_smooth/'+file_name,
                img_smooth)

# practice 2
path = '/home/orangepi/PycharmProjects/course_digital_sreeni/images/scratch_assay_smooth/*.*'
img_list = []
for file in glob.glob(path):
    img = cv2.imread(file, 0)
    img_list.append(img)
img_array = np.array(img_list)
for ind in range(img_array.shape[0]):
    img_input = img_array[ind, :, :]
    img_smooth = img_as_ubyte(gaussian(img_input, sigma=2, mode='constant', cval=0))
    cv2.imwrite('/home/orangepi/PycharmProjects/course_digital_sreeni/images/scratch_assay_smooth/'+str(ind)+'.jpg',
                img_smooth)

# remove the testing image folder
path = '/home/orangepi/PycharmProjects/course_digital_sreeni/images/scratch_assay_smooth'
shutil.rmtree(path)
