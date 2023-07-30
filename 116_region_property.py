import matplotlib.pyplot as plt
from skimage import io, img_as_ubyte, measure
from skimage.color import label2rgb, rgb2gray
import numpy as np
from skimage.filters import threshold_otsu
import pandas as pd


if __name__ == "__main__":
    img = img_as_ubyte(rgb2gray(io.imread('images/cast_iron.jpg')))
    threshold = threshold_otsu(img)
    label_img = measure.label(img<threshold, connectivity=img.ndim)
    plt.imshow(label_img)
    # plt.show()
    img_label_overlay = label2rgb(label_img, image=img)
    plt.imshow(img_label_overlay)
    # plt.show()
    props = measure.regionprops_table(label_img, img, properties=['label', 'area', 'equivalent_diameter',
                                                                  'mean_intensity', 'solidity'])
    df = pd.DataFrame(props)
    print(df.head())





