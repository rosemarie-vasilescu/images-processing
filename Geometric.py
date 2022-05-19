import cv2
from matplotlib import pyplot as plt

class Geometric:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
      image = cv2.imread(self.image)

      plt.figure(figsize=(20, 20))
      plt.subplot(3, 2, 1)
      plt.title("Original")
      plt.imshow(image)
      image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
      plt.subplot(3, 2, 2)
      plt.title("Scaling - Linear Interpolation")
      plt.imshow(image_scaled)
      plt.subplot(3, 2, 3)
      plt.title("Original")
      plt.imshow(image)
      img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
      plt.subplot(3, 2, 4)
      plt.title("Scaling - Cubic Interpolation")
      plt.imshow(img_scaled)
      plt.subplot(3, 2, 5)
      plt.title("Original")
      plt.imshow(image)
      img_scaled = cv2.resize(image, (900, 400), interpolation=cv2.INTER_AREA)
      plt.subplot(3, 2, 6)
      plt.title("Scaling - Skewed Size")
      plt.imshow(img_scaled)
      plt.show()