from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class MyLabel(QLabel):
    clicked = pyqtSignal()
    released = pyqtSignal()
    def __init__(self, text, connect=0,IsClicked=True,parent=None):
        super().__init__(text,parent)
        self.x = 0
        self.y= 0
        self.xPosition=0
        self.yPosition=0
        self.connect=connect
        self.IsClicked=IsClicked

    def setIsClicked(self, judge):
        self.IsClicked = judge

    def getIsClicked(self):
        return self.IsClicked


    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        self.x=e.x()
        self.y=e.y()
        if self.connect:
            self.xPosition = round(self.x * (512.0 / self.width()))
            self.yPosition = round(self.y * (512.0 / self.height()))
            #self.connect[0].setText("X: "+str(self.xPosition)+"\nY: " + str(self.yPosition)+"\nZ: " + str(self.connect[1].value()))
            if(self.xPosition<0):
                self.xPosition=0
            if(self.yPosition<0):
                self.yPosition=0
            if(self.xPosition>511):
                self.xPosition=511
            if(self.yPosition>511):
                self.yPosition=511
            self.setIsClicked(True)

        self.clicked.emit()
        e.ignore()

    def mouseMoveEvent(self, e):
        print("Internal")
        self.x=e.x()
        self.y=e.y()
        if self.connect:
            self.xPosition = round(self.x * (512.0 / self.width()))
            self.yPosition = round(self.y * (512.0 / self.height()))
            #self.connect[0].setText("X: "+str(self.xPosition)+"\nY: " + str(self.yPosition)+"\nZ: " + str(self.connect[1].value()))
            if(self.xPosition<0):
                self.xPosition=0
            if(self.yPosition<0):
                self.yPosition=0
            if(self.xPosition>511):
                self.xPosition=511
            if(self.yPosition>511):
                self.yPosition=511
            self.setIsClicked(True)
        e.ignore()

    def mouseReleaseEvent(self, e):
        # 发射释放信号
        self.released.emit()
        e.ignore()




