import cv2
from matplotlib import pyplot as plt
import numpy as np
class Masking:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
      image = cv2.imread(self.image)
      mask = np.zeros(image.shape[:2], dtype="uint8")
      cv2.circle(mask, (145, 200), 100, 255, -1)
      masked = cv2.bitwise_and(image, image, mask=mask)
      # show the output images
      plt.subplot(1, 3, 1)
      plt.title("Original")
      plt.imshow(image)
      plt.subplot(1,3,2)
      plt.title("Mask")
      plt.imshow( mask)
      plt.subplot(1,3,3)
      plt.title("Masked")
      plt.imshow( masked)
      plt.show()

