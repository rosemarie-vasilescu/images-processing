
import cv2
import time
import statistics
import math
from Cropping import Cropp
from Edge import Edge
from Morphological import Morphological
from Histogram import Histogram
from Masking import Masking
from Geometric import Geometric
from Thresholding import Thresholding
from Blurring import Blurring
from SaltPepper import SaltPepper
from Drawing import Drawing
from PyQt5.QtWidgets import QInputDialog
class Principal:

    def __init__(self, alg, img):

        self.alg=alg
        self.img=img
        print(alg)
        if alg=='Cropping':

            self.solutie=Cropp(self.img)

        elif alg=="Edge":
            self.solutie = Edge(self.img)
        elif alg == "Morphologic":
            self.solutie = Morphological(self.img)
        elif alg == "Histogram":
            self.solutie=Histogram(self.img)
        elif alg=="Masking":
            self.solutie = Masking(self.img)

        elif alg=="Geometric":
            self.solutie=Geometric(self.img)
        elif alg=="Thresholding":
            self.solutie=Thresholding(self.img)
        elif alg=="Blurring":
            self.solutie=Blurring(self.img)
        elif alg=="SaltPepper":
            self.solutie=SaltPepper(self.img)
        elif alg=="Drawing":
            self.solutie=Drawing(self.img)





    def aplica(self,img):
        print(img)
        poza_cautata = cv2.imread(img, 0)
        poza_cautata = poza_cautata.reshape(-1, )
        self.solutie.poza_cautata=poza_cautata
        print('cautapoza')

        return self.solutie.aplica()

