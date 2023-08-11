import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import metrics


ref_img = cv2.imread('images/BSE_Google.jpg', 1)
img = cv2.imread('images/BSE_Google_noisy.jpg', 1)

mse_skimg = metrics.mean_squared_error(ref_img, img)
psnr_skimg = metrics.peak_signal_noise_ratio(ref_img, img)
rmse_skimg = metrics.normalized_root_mse(ref_img, img)

print("mean square error: {:.2f},"
      "peak signal noise ratio: {:.2f},"
      "root mean square error: {:.2f}".format(mse_skimg, psnr_skimg, rmse_skimg))





