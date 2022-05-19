import cv2
from matplotlib import pyplot as plt

class Histogram:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
       image = cv2.imread(self.image)
       image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       plt.figure()
       plt.imshow(image)
       # #
       # # find frequency of pixels in range 0-255
       histr = cv2.calcHist([image], [0], None, [256], [0, 256])
       #
       plt.figure()
       plt.title("Histogram")
       plt.xlabel('Bins')  # Intervals of pixels along x axis
       plt.ylabel('No. of pixels')
       plt.plot(histr)
       plt.xlim([0, 256])  # Limit of x axis
       plt.show()
       # # show the plotting graph of an image

       # plt.imshow(histr)
       # plt.show()


