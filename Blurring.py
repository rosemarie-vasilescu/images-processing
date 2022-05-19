import cv2
from matplotlib import pyplot as plt
import numpy as np
class Blurring:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
      image = cv2.imread(self.image)

      plt.figure(figsize=(20, 20))
      plt.subplot(1, 3, 1)
      plt.title("Original")
      plt.imshow(image)
      kernel_3x3 = np.ones((3, 3), np.float32) / 9
      blurred = cv2.filter2D(image, -1, kernel_3x3)
      plt.subplot(1, 3, 2)
      plt.title("3x3 Kernel Blurring")
      plt.imshow(blurred)
      kernel_7x7 = np.ones((7, 7), np.float32) / 49
      blurred2 = cv2.filter2D(image, -1, kernel_7x7)
      plt.subplot(1, 3, 3)
      plt.title("7x7 Kernel Blurring")
      plt.imshow(blurred2)
      plt.show()
