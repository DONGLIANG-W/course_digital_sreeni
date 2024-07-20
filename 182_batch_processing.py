import cv2
import glob
from skimage.filters import gaussian
from skimage.util import img_as_ubyte
import os

path = 'images\grains\*'

# loop through the images in the directory, process and save each image
for file in glob.glob(path):
    print(file)
    img_name = os.path.basename(file)
    img = cv2.imread(file,0)
    # smooth the image
    smoothed_img = img_as_ubyte(gaussian(img,sigma=5,mode='constant', cval=0.0))
    cv2.imwrite('images/smoothed/'+'smoothed_'+img_name, smoothed_img)

# os.walk() walk though the files in the directory, which works the same as glob.glob()
for root, dirs, files in os.walk('images/grains/'):
    print(files)

# store the image into a array and process later
# read and save each image into a layer in the array matrix, then process
# each layer of the matrix. Note the dimension of each layer must identical, else
# need to resize the image, which is not favorable.
