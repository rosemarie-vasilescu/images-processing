import cv2
from matplotlib import pyplot as plt

class Thresholding:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
      image = cv2.imread(self.image)

      plt.figure(figsize=(30, 30))
      plt.subplot(1, 2, 1)
      plt.title("Original")
      plt.imshow(image)
      ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
      plt.subplot(1, 2, 2)
      plt.title("Threshold Binary")
      plt.imshow(thresh1)


      plt.show()
