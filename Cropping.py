import cv2
from matplotlib import pyplot as plt

class Cropp:
    def __init__(self,image):
#      image = image = cv2.imread('fruit.jpg')
       self.image=image
    def aplica(self):
      image = cv2.imread(self.image, 0)
      plt.subplot(2, 2, 1)
      plt.title("Original")
      plt.imshow(image)
      img=cv2.imread(self.image,0)
      print("aplica cropp")
      height, width = img.shape[0:2]
      startRow = int(height*.15)

      startCol = int(width*.15)

      endRow = int(height*.85)

      endCol = int(width*.85)
      croppedImage = img[startRow:endRow, startCol:endCol]
      plt.subplot(2, 2, 2)
      plt.title("Cropped Image")
      plt.imshow(croppedImage)
      plt.show()

