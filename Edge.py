import cv2
from matplotlib import pyplot as plt

class Edge:
    def __init__(self,image):

       self.image=image
    def aplica(self):
      image = cv2.imread(self.image)
      image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      plt.subplot(2, 2, 1)
      plt.title("Original")
      plt.imshow(image)

      edge_img = cv2.Canny(image, 100, 200)
      plt.subplot(2, 2, 2)
      plt.title("Canny")
      plt.imshow(edge_img,cmap='gray')
      plt.show()

      image = cv2.imread(self.image)
      iamge=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      plt.subplot(2, 2, 3)
      plt.title("Original")
      plt.imshow(image)
      laplacian = cv2.Laplacian(image, cv2.CV_64F)
      plt.subplot(2, 2, 4)
      plt.title("Laplacian")
      plt.imshow(laplacian)
      plt.show()
