from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from Start import Principal
from matplotlib import pyplot as plt
PLACEHOLDER='Placeholder.png'
import numpy as np
import pickle
import traceback
class Ui_MainWindow(QtWidgets.QWidget):
    _img=PLACEHOLDER

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gbAlegerePr = QtWidgets.QGroupBox(self.centralwidget)
        self.gbAlegerePr.setGeometry(QtCore.QRect(410, 10, 301, 450))
        self.gbAlegerePr.setObjectName("gbAlegerePr")
        self.rbCropp = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbCropp.setGeometry(QtCore.QRect(20, 40, 82, 21))
        self.rbCropp.setObjectName("rbCropp")
        self.rbCropp.setChecked(True)
        self.rbEdge = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbEdge.setGeometry(QtCore.QRect(20, 80, 110, 25))
        self.rbEdge.setObjectName("rbEdge")
        self.rbEdge.setChecked(False)
        self.rbMorphologic = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbMorphologic.setGeometry(QtCore.QRect(20, 120, 110, 25))
        self.rbMorphologic.setObjectName("rbMorphologic")
        self.rbMorphologic.setChecked(False)
        self.rbGeometric = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbGeometric.setGeometry(QtCore.QRect(20, 160, 82, 21))
        self.rbGeometric.setObjectName("rbGeometric")
        self.rbGeometric.setChecked(False)
        self.rbThresholding = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbThresholding.setGeometry(QtCore.QRect(20, 200, 100, 25))
        self.rbThresholding.setObjectName("rbThresholding")
        self.rbThresholding.setChecked(False)
        self.rbBlurring = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbBlurring.setGeometry(QtCore.QRect(20, 240, 82, 21))
        self.rbBlurring.setObjectName("rbBluring")
        self.rbBlurring.setChecked(False)
        self.rbSaltPepper = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbSaltPepper.setGeometry(QtCore.QRect(20, 280, 100, 25))
        self.rbSaltPepper.setObjectName("rbSaltPepper")
        self.rbSaltPepper.setChecked(False)
        self.rbMasking = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbMasking.setGeometry(QtCore.QRect(20, 320, 82, 25))
        self.rbMasking.setObjectName("rbMasking")
        self.rbMasking.setChecked(False)
        self.rbDrawing = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbDrawing.setGeometry(QtCore.QRect(20, 360, 82, 21))
        self.rbDrawing.setObjectName("rbDrawing")
        self.rbDrawing.setChecked(False)
        self.rbHistogram = QtWidgets.QRadioButton(self.gbAlegerePr)
        self.rbHistogram.setGeometry(QtCore.QRect(20, 400, 82, 21))
        self.rbHistogram.setObjectName("rbHistogram")
        self.rbHistogram.setChecked(False)


        self.pushbIncarca = QtWidgets.QPushButton(self.centralwidget)
        self.pushbIncarca.setGeometry(QtCore.QRect(420, 500, 120, 30))
        self.pushbIncarca.setObjectName("pushbIncarca")
        self.pushbCauta = QtWidgets.QPushButton(self.centralwidget)
        self.pushbCauta.setGeometry(QtCore.QRect(580, 500, 120, 30))
        self.pushbCauta.setObjectName("pushbCauta")
        self.pushbCauta.setEnabled(True)
        self.labGasit = QtWidgets.QLabel(self.centralwidget)
        self.labGasit.setGeometry(QtCore.QRect(736, 22, 361, 511))
        self.labGasit.setText("")
        self.labGasit.setPixmap(QtGui.QPixmap("Placeholder.png"))
        self.labGasit.setScaledContents(True)
        self.labGasit.setObjectName("labGasit")
        self.labCautat = QtWidgets.QLabel(self.centralwidget)
        self.labCautat.setGeometry(QtCore.QRect(26, 22, 361, 511))
        self.labCautat.setText("")
        self.labCautat.setPixmap(QtGui.QPixmap("Placeholder.png"))
        self.labCautat.setScaledContents(True)
        self.labCautat.setObjectName("labCautat")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #
        self.pushbCauta.clicked.connect(self.pregatesteDate)
        self.pushbIncarca.clicked.connect(self.incarca)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gbAlegerePr.setTitle(_translate("MainWindow", "Image Processing"))
        self.rbCropp.setText(_translate("MainWindow","Cropping"))
        self.rbEdge.setText(_translate("MainWindow", "Edge detection"))
        self.rbMorphologic.setText(_translate("MainWindow", "Morphological"))
        self.rbGeometric.setText(_translate("MainWindow", "Re-sizing"))
        self.rbThresholding.setText(_translate("MainWindow", "Thresholding"))
        self.rbBlurring.setText(_translate("MainWindow", "Blurring"))
        self.rbSaltPepper.setText(_translate("MainWindow", "Salt & pepper"))
        self.rbMasking.setText(_translate("MainWindow", "Masking"))
        self.rbDrawing.setText(_translate("MainWindow", "Drawing"))
        self.rbHistogram.setText(_translate("MainWindow", "Histogram"))
        self.pushbIncarca.setText(_translate("MainWindow", "Search image"))
        self.pushbCauta.setText(_translate("MainWindow", "Apply"))


    def pregatesteDate(self):
        #restrictioneaza imaginea ce poate fi folosit la png, jpg, formatul
        #folosit in orl, etc


        print("hei")
        self.alg=self.returneazaAlg()
        print(self.alg)
        self.hub = Principal(  self.alg,  self._img)

        print('cauta')
        poza = self.hub.aplica(self._img)

        self.labGasit.setPixmap(QtGui.QPixmap(poza))
        pass
        algoritmi = {'COD': 'COD',
                     'Tensori': 'Tensori',
                     'Eigenfaces': 'Eigenfaces',
                     'Lanczos': 'Lanczos',
                     'Elanbi': 'Elanbi', }

    def returneazaAlg(self):

        if self.rbCropp.isChecked():
                alg = 'Cropping'
        elif self.rbEdge.isChecked():
            alg="Edge"
        elif self.rbMasking.isChecked():
            alg="Masking"
        elif self.rbMorphologic.isChecked():
            alg="Morphologic"
        elif self.rbGeometric.isChecked():
            alg="Geometric"
        elif self.rbThresholding.isChecked():
            alg="Thresholding"
        elif self.rbBlurring.isChecked():
            alg="Blurring"
        elif self.rbSaltPepper.isChecked():
            alg="SaltPepper"
        elif self.rbMasking.isChecked():
            alg="Masking"
        elif self.rbDrawing.isChecked():
            alg="Drawing"
        elif self.rbHistogram.isChecked():
            alg="Histogram"
        return alg


    def incarca(self):
        Tk().withdraw()
        self._img = askopenfilename()
        print('ok')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())