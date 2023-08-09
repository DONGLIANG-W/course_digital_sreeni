import numpy as np
import matplotlib.pyplot as plt
from skimage import io, data
from skimage.registration import phase_cross_correlation
from skimage.registration._phase_cross_correlation import _upsampled_dft
from scipy.ndimage import fourier_shift, shift
import cv2

img = cv2.imread('images/BSE_Image.jpg', 0)
# create an shifted image, first fourier shift the frequency domain image, then inverse fourier transform the frequency
# image back to space domain image
shift_value = (-22.4, 13.32)
img_shift = fourier_shift(np.fft.fftn(img), shift_value)
img_shift = np.fft.ifftn(img_shift)
# leave only the real part of the inverse fourier transform of the image
img_shift_real = img_shift.real
# plot the image
# fig, ax = plt.subplots(1,2)
# ax[0].imshow(img, cmap='gray')
# ax[1].imshow(img_shift_real, cmap='gray')
# plt.show()

shifted, error, diffphase = phase_cross_correlation(img, img_shift)
print(f'Detected subpixel offset (x, y): {shifted} ')

# use the skimage.ndimage.shift module, shift the image back
img_corrected = shift(img_shift, shift=(shifted[0], shifted[1]))
# use the fourier_shift module to shift the image
img_correct_fourier = fourier_shift(np.fft.fftn(img_shift_real), (shifted[0], shifted[1]))
img_correct_fourier = np.fft.ifftn(img_correct_fourier)
fig, ax = plt.subplots(1,4)
ax[0].imshow(img)
ax[1].imshow(img_shift_real)
ax[2].imshow(img_corrected.real)
ax[3].imshow(img_correct_fourier.real)
plt.suptitle('Image shift in fft')
plt.show()
# as shown in figure, the fourier_shift module maintained the integrity of the image data, better compared to
# scipy.ndimage.shift

