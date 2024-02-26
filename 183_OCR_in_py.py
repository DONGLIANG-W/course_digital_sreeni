"""
OCR stands for optical character recognition
Here we are not start from the scratch, instead running with keras-ocr, a module
provided by kera
"""

import keras_ocr
import matplotlib.pyplot as plt
import glob

pipeline = keras_ocr.pipeline.Pipeline()
# List of images
images = [keras_ocr.tools.read(img) for img in glob.glob('images/signage/*')]

# each list of predictions in prediction_groups is a list of tuples
predictions_groups = pipeline.recognize(images)

# plot the predictions
fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
for ax, image, predictions in zip(axs, images, predictions_groups):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)

plt.savefig('images/signage/ocr_prediction.png')
plt.show()
