from skimage import io
from matplotlib import pyplot as plt
from skimage.transform import resize, rescale, downscale_local_mean
from skimage.filters import roberts, sobel, scharr, prewitt
from skimage.feature import canny
from skimage import restoration
import numpy as np

img = io.imread('images/test_image.jpg', as_gray=True)
rescaled_img = rescale(img, 0.25, anti_aliasing=True)
resized_img = resize(img,(200, 200))
downscaled_img = downscale_local_mean(img, (4,3))
# plt.imshow(resized_img)
# plt.imshow(downscaled_img)
# plt.imshow(rescaled_img)
# plt.show()
# print(img.shape)

# robert edge detector
edge_roberts = roberts(img)
edge_sobel = sobel(img)
edge_scharr = scharr(img)
edge_prewitt = prewitt(img)
edge_canny = canny(img, sigma=3)

# restoration with point spread function
psf = np.ones((3,3)) / 9
deconvolved, _ = restoration.unsupervised_wiener(downscaled_img, psf)



fig, axes = plt.subplots(4,2,sharex=True, sharey=True,figsize=(8,8))

ax = axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title("original image")

# ax[1].imshow(edge_roberts)
# ax[1].set_title("Roberts edge detector")
# ax[2].imshow(edge_sobel)
# ax[2].set_title("sobel edge detector")
# ax[3].imshow(edge_scharr)
# ax[3].set_title("Scharr edge detector")
# ax[4].imshow(edge_prewitt)
# ax[4].set_title("Prewitt edge detector")
# ax[5].imshow(edge_canny)
# ax[5].set_title("Canny edge detector")
# ax[6].imshow(deconvolved)
# ax[6].set_title("deconvolved image")

ax[1+1].imshow(edge_roberts)
ax[1+1].set_title("Roberts edge detector")
ax[2+1].imshow(edge_sobel)
ax[2+1].set_title("sobel edge detector")
ax[3+1].imshow(edge_scharr)
ax[3+1].set_title("Scharr edge detector")
ax[4+1].imshow(edge_prewitt)
ax[4+1].set_title("Prewitt edge detector")
ax[5+1].imshow(edge_canny)
ax[5+1].set_title("Canny edge detector")
ax[6+1].imshow(deconvolved)
ax[6+1].set_title("deconvolved image")

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()



