from skimage.transform import hough_line, hough_line_peaks
import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('images/lines1.png', 0)
img = ~img
plt.imshow(img, cmap='gray')
# plt.show()

tested_angle = np.linspace(-np.pi/2, np.pi/2, 180)
hspace, theta, dist = hough_line(img, tested_angle)

plt.figure(figsize=(10,10))
plt.imshow(hspace)
# plt.show()

h, q, d = hough_line_peaks(hspace, theta, dist)
angle_list = []

fig, axes = plt.subplots(1,3,figsize=(15,6))
ax = axes.ravel()

ax[0].imshow(img, cmap='gray')
ax[0].set_title('input image')
ax[0].set_axis_off()

ax[1].imshow(np.log(1+hspace),
             extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), dist[-1], dist[0]],
             cmap='gray', aspect=1/1.5)
ax[1].set_title('Hough transform')
ax[1].set_xlabel('Angles (degree)')
ax[1].set_ylabel('Distance (pixel)')
ax[1].axis('image')
ax[2].imshow(img, cmap='gray')
origin = np.array((0, img.shape[1]))
for _, angle, dist in zip(*hough_line_peaks(hspace, theta, dist)):
    angle_list.append(angle)
    y0, y1 =(dist - origin*np.cos(angle)) / np.sin(angle)
    ax[2].plot(origin, (y0, y1), '-r')
ax[2].set_xlim(origin)
ax[2].set_ylim((img.shape[0], 0))
ax[2].set_axis_off()
ax[2].set_title('Detected lines')
# plt.show()
angles = [a*180/np.pi for a in angle_list]
print(angles)
angle_difference = np.max(angles) - np.min(angles)
print('angles found are: {}'.format(180-angle_difference))