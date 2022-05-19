import cv2
from matplotlib import pyplot as plt
import numpy as np
class Morphological:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
        image = cv2.imread(self.image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.figure(figsize=(100,100))
        plt.subplot(2, 2, 1)
        plt.title("Original")
        plt.imshow(image, cmap='gray')

        kernel = np.ones((5, 5), np.uint8)

        erosion = cv2.erode(image, kernel, iterations=1)
        plt.subplot(2, 2, 2)
        plt.title("Erosion")
        plt.imshow(erosion, cmap='gray')
        plt.subplot(2, 2, 3)
        plt.title("Original")
        plt.imshow(image, cmap='gray')

        dilation = cv2.dilate(image, kernel, iterations=1)
        plt.subplot(2, 2, 4)
        plt.title("Dilation")
        plt.imshow(dilation, cmap='gray')


        # opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        # plt.subplot(4, 2, 6)
        # plt.title("Opening")
        # plt.imshow(opening, cmap='gray')
        # plt.subplot(4, 2, 7)
        # plt.title("Original")
        # plt.imshow(image, cmap='gray')
        #
        # closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        # plt.subplot(4, 2,8)
        # plt.title("Closing")
        # plt.imshow(closing, cmap='gray')
        plt.show()