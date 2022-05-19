import cv2
import random
from matplotlib import pyplot as plt
import numpy as np
class SaltPepper:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
      image = cv2.imread(self.image)

      row, col, ch = image.shape
      s_vs_p = 0.5
      amount = 0.04
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
                for i in image.shape]
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
                for i in image.shape]
      out[coords] = 0

      plt.figure(figsize=(30, 30))
      plt.subplot(1, 2, 1)
      plt.title("Original")
      plt.imshow(image)
      plt.subplot(1, 2, 2)
      plt.title("Add salt and pepper")
      plt.imshow(out)

      plt.show()
