import cv2
from matplotlib import pyplot as plt
import numpy as np
class Drawing:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
      image = cv2.imread(self.image)

      plt.figure(figsize=(20, 20))
      plt.subplot(3, 2, 1)
      plt.title("Original")
      plt.imshow(image)
      rec = np.copy(image)
      ccl= np.copy(image)
      wrt= np.copy(image)
      cv2.rectangle(rec, (30, 30), (300, 200), (0, 255, 0), 5)
      plt.subplot(3, 2, 2)
      plt.title("Rectangle")
      plt.imshow(rec)
      cv2.circle(ccl, (200, 200), 80, (255, 0, 0), 3)
      plt.subplot(3, 2, 3)
      plt.title("Original")
      plt.imshow(image)
      plt.subplot(3, 2, 4)
      plt.title("Circle")
      plt.imshow(ccl)
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.putText(wrt, 'Image processing', (50, 200),
                  font, 4, (255,0, 0), 2, cv2.LINE_AA)
      plt.subplot(3, 2, 5)
      plt.title("Original")
      plt.imshow(image)
      plt.subplot(3, 2, 6)
      plt.title("Text")
      plt.imshow(wrt)
      plt.show()
      # plt.subplot(3, 2, 3)
      # plt.title("Original")
      # plt.imshow(image)
      # img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
      # plt.subplot(3, 2, 4)
      # plt.title("Scaling - Cubic Interpolation")
      # plt.imshow(img_scaled)
      # plt.subplot(3, 2, 5)
      # plt.title("Original")
      # plt.imshow(image)
      # img_scaled = cv2.resize(image, (900, 400), interpolation=cv2.INTER_AREA)
      # plt.subplot(3, 2, 6)
      # plt.title("Scaling - Skewed Size")
      # plt.imshow(img_scaled)
