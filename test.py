import os
import subprocess
import time
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QImageReader
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, \
    QPushButton, QFrame, QApplication, QDesktopWidget, QAction, QMessageBox, QFileDialog
from PyQt5.QtGui import QImage, QPixmap, QIcon
from SimpleITK import ReadImage, GetArrayFromImage, GetImageFromArray, WriteImage
from numpy import stack, zeros, resize, uint8, int16, float32, where
from copy import deepcopy
from cv2 import resize, cvtColor, COLOR_BGR2RGB
from copy import deepcopy
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import scipy.io as sio
from MyLabel import MyLabel

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#git完版本

class Ui_MainWindow(QMainWindow):

    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        # 在这里为整个窗口启用鼠标跟踪
        self.setMouseTracking(True)

        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(802, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/LvPin/Pictures/屏幕截图 2023-10-07 153156.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choosepicture = QtWidgets.QPushButton(self.centralwidget)
        self.choosepicture.setGeometry(QtCore.QRect(370, 20, 111, 41))
        self.choosepicture.setObjectName("choosepicture")
        self.choices = QtWidgets.QComboBox(self.centralwidget)
        self.choices.setGeometry(QtCore.QRect(150, 30, 151, 31))
        self.choices.setObjectName("choices")
        self.choices.addItem("")
        self.choices.addItem("")
        self.choices.addItem("")
        self.chooseLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseLabel.setGeometry(QtCore.QRect(40, 40, 111, 16))
        self.chooseLabel.setObjectName("chooseLabel")
        self.BigLabel = QtWidgets.QLabel(self.centralwidget)
        self.BigLabel.setGeometry(QtCore.QRect(40, 110, 211, 181))
        self.BigLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BigLabel.setObjectName("BigLabel")
        self.PositioLabel = QtWidgets.QLabel(self.centralwidget)
        self.PositioLabel.setGeometry(QtCore.QRect(40, 310, 211, 111))
        self.PositioLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PositioLabel.setObjectName("PositioLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 20, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(300, 70, 451, 531))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(0, 10, 451, 511))
        self.widget.setObjectName("widget")
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 220, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(40, 470, 160, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(250, 470, 160, 16))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(240, 10, 200, 200))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_2 = MyLabel(text='', connect=[self.PositioLabel, self.horizontalSlider], IsClicked=False)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 200, 200))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_2_width = self.label_2.width()
        self.label_2_height = self.label_2.height()
        self.label_3 = MyLabel(text='', connect=[self.PositioLabel, self.horizontalSlider_2], IsClicked=False)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 200, 200))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_3_width = self.label_3.width()
        self.label_3_height = self.label_3.height()
        self.label_4 = MyLabel(text='', connect=[self.PositioLabel, self.horizontalSlider_3], IsClicked=False)
        self.label_4.setGeometry(QtCore.QRect(240, 260, 200, 200))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_4_width = self.label_4.width()
        self.label_4_height = self.label_4.height()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 802, 22))
        self.menuBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuBar.setDefaultUp(True)
        self.menuBar.setObjectName("menuBar")
        self.menumune = QtWidgets.QMenu(self.menuBar)
        self.menumune.setObjectName("menumune")
        self.menuEDIT = QtWidgets.QMenu(self.menuBar)
        self.menuEDIT.setObjectName("menuEDIT")
        self.menuHELP = QtWidgets.QMenu(self.menuBar)
        self.menuHELP.setObjectName("menuHELP")
        MainWindow.setMenuBar(self.menuBar)
        self.actioninput_file = QtWidgets.QAction(MainWindow)
        self.actioninput_file.setObjectName("actioninput_file")
        # 将 "input file" 操作连接到槽函数
        self.actionoutput_file = QtWidgets.QAction(MainWindow)
        self.actionoutput_file.setObjectName("actionoutput_file")

        # 连接下拉框的activated信号到自定义的函数
        self.choices.activated.connect(self.on_combobox_activated)
        self.choosepicture.clicked.connect(self.on_choosepicture_clicked)
        # 在初始化中添加一个标志位，表示 "3D CNN 最终CMB" 是否被选择
        self.cmb_option_selected = False

        self.actionabout_us = QtWidgets.QAction(MainWindow)
        self.actionabout_us.setObjectName("actionabout_us")
        self.actiondrawing = QtWidgets.QAction(MainWindow)
        self.actiondrawing.setObjectName("actiondrawing")
        self.menumune.addAction(self.actioninput_file)
        self.menumune.addAction(self.actionoutput_file)
        self.menuEDIT.addAction(self.actiondrawing)
        self.menuHELP.addAction(self.actionabout_us)
        self.menuBar.addAction(self.menumune.menuAction())
        self.menuBar.addAction(self.menuEDIT.menuAction())
        self.menuBar.addAction(self.menuHELP.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actioninput_file.triggered.connect(self.load_nii_file)
        self.horizontalSlider.valueChanged.connect(self.sliderMoved_01)
        self.horizontalSlider_2.valueChanged.connect(self.sliderMoved_02)
        self.horizontalSlider_3.valueChanged.connect(self.sliderMoved_03)

        self.nifti_image = None
        self.current_slice = [0, 0, 0]

        self.label_2.setParent(self.widget)
        self.label_3.setParent(self.widget)
        self.label_4.setParent(self.widget)

        self.label_2.clicked.connect(self.label_2_clicked)
        self.label_2.released.connect(self.label_released)
        self.label_3.clicked.connect(self.label_3_clicked)
        self.label_3.released.connect(self.label_released)
        self.label_4.clicked.connect(self.label_4_clicked)
        self.label_4.released.connect(self.label_released)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIrecognition"))
        self.choosepicture.setText(_translate("MainWindow", "开始识别"))
        self.choices.setItemText(0, _translate("MainWindow", "原始"))
        self.choices.setItemText(1, _translate("MainWindow", "3D FCN 初筛"))
        self.choices.setItemText(2, _translate("MainWindow", "3D CNN 最终CMB"))
        self.chooseLabel.setText(_translate("MainWindow", "选择筛选阶段"))
        self.BigLabel.setText(_translate("MainWindow", "大图"))
        self.PositioLabel.setText(_translate("MainWindow", "坐标"))
        self.pushButton.setText(_translate("MainWindow", "退出识别"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_5.setText(_translate("MainWindow", "3D"))
        self.label_4.setText(_translate("MainWindow", "Z"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.menumune.setTitle(_translate("MainWindow", "FILE"))
        self.menuEDIT.setTitle(_translate("MainWindow", "EDIT"))
        self.menuHELP.setTitle(_translate("MainWindow", "HELP"))
        self.actioninput_file.setText(_translate("MainWindow", "input file"))
        self.actionoutput_file.setText(_translate("MainWindow", "output file"))
        self.actionabout_us.setText(_translate("MainWindow", "about us"))
        self.actiondrawing.setText(_translate("MainWindow", "drawing"))

    def load_nii_file(self, slices=zeros((1, 512, 512))):
        self.slices = slices
        self.number = 0
        self.yPosition = 0
        self.xPosition = 0

        array = []
        # 弹出文件选择对话框，并获取选择的文件路径
        self.fp = QFileDialog.getOpenFileName()
        print(self.fp)
        print(self.fp[0])
        # 检查用户是否选择了文件
        if self.fp[0]:
            # 读取图像文件
            imgs = ReadImage(self.fp[0])
            # 定义测试方向
            TestDirection = (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
            # 获取图像数组
            img3D_array = GetArrayFromImage(imgs)
            # 如果图像的方向与测试方向相同，进行一些处理
            if imgs.GetDirection() == TestDirection:
                for i in range(len(img3D_array)):
                    array.append(img3D_array[len(img3D_array) - i - 1, :, :])
                img3D_array = stack([s for s in array])
                global Label_Direction
                Label_Direction = 1
            # 对图像数组进行预处理
            img3D_array = deepcopy(self.preprocessing(img3D_array))
            # 打开图像并显示
            self.open(img3D_array)
            # 设置滑动条的最大值和值
            self.horizontalSlider.setMaximum(self.slices.shape[0])
            #            self.horizontalSlider.setValue(self.slices.shape[0] // 2)

            # 显示图像在标签上
            pixmap_imgSrc_01 = self.setInitGraph_01(self.horizontalSlider.value())
            self.label_2.setPixmap(pixmap_imgSrc_01)
            self.label_2.setAlignment(Qt.AlignCenter)

            self.horizontalSlider_2.setMaximum(self.slices.shape[1])
            pixmap_imgSrc_02 = self.setInitGraph_02(self.horizontalSlider_2.value())
            self.label_3.setPixmap(pixmap_imgSrc_02)
            self.label_3.setAlignment(Qt.AlignCenter)

            self.horizontalSlider_3.setMaximum(self.slices.shape[2])
            pixmap_imgSrc_03 = self.setInitGraph_03(self.horizontalSlider_3.value())
            self.label_4.setPixmap(pixmap_imgSrc_03)
            self.label_4.setAlignment(Qt.AlignCenter)

            return self.fp
            #return self.fp[0]

    def setInitGraph_01(self, value):
        self.number_3 = self.horizontalSlider_3.value()
        img = resize(src=self.slices[value - 1, :, :], dsize=None, fx=1, fy=1)
        img2 = cvtColor(img, COLOR_BGR2RGB)
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        pixmap_imgSrc_1 = QPixmap.fromImage(image).scaled(self.label_2_width, self.label_2_height)
        return pixmap_imgSrc_1

    def setInitGraph_02(self, value):
        img = resize(src=self.slices[:, :, value - 1], dsize=None, fx=1, fy=1)
        img2 = cvtColor(img, COLOR_BGR2RGB)
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        self.pixmap_imgSrc_2 = QPixmap.fromImage(image).scaled(self.label_3_width, self.label_3_height)
        return self.pixmap_imgSrc_2

    def setInitGraph_03(self, value):
        img = resize(src=self.slices[:, value - 1, :], dsize=None, fx=1, fy=1)
        img2 = cvtColor(img, COLOR_BGR2RGB)
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        self.pixmap_imgSrc_3 = QPixmap.fromImage(image).scaled(self.label_4_width, self.label_4_height)
        return self.pixmap_imgSrc_3

    def sliderMoved_01(self):
        self.number = self.horizontalSlider.value()
        img = abs(self.slices[self.number - 1, :, :]) / 255
        img = (pow(img, 1) * 255)
        self.refeshGraph_01(img)

    def sliderMoved_02(self):
        self.number_2 = self.horizontalSlider_2.value()
        img = abs(self.slices[:, :, self.number_2 - 1]) / 255
        img = (pow(img, 1) * 255)
        self.refeshGraph_02(img)

    def sliderMoved_03(self):
        self.number_3 = self.horizontalSlider_3.value()
        img = abs(self.slices[:, self.number_3 - 1, :]) / 255
        img = (pow(img, 1) * 255).astype(uint8)
        self.refeshGraph_03(img)

    def preprocessing(self, img3D_array):
        image = img3D_array.copy()
        image = image.astype(int16)
        img3D_array_ = img3D_array.astype(float32)  # 把数据从 int32转为 float32类型
        img3D_array_ = (img3D_array - img3D_array.min()) / (img3D_array.max() - img3D_array.min())
        # 把数据范围变为0--1浮点,或许还有其他转换方法,效果能更好一些.
        img3D_array = (img3D_array_ * 255).astype(uint8)  # 转换为0--255的灰度uint8类型
        return img3D_array

    def open(self, img3D_array):
        # 复制传入的3D图像数据
        self.slices = deepcopy(img3D_array)
        # 计算图像中某一层的像素平均值
        HHH = self.slices[len(self.slices) // 2 - 1].sum() / (512 * 512)
        # 如果平均值小于6，则进行像素值的调整
        if HHH < 6:
            adj = (6 - HHH) / 10.972
            self.slices = ((pow(abs(self.slices) / 255, 1 - adj) * 255)).astype(uint8)

        # 如果白色像素点数量小于15000，则将像素值大于220的像素设置为220
        if len(self.slices[self.slices == 255]) < 15000:
            self.slices[self.slices > 220] = 220

        # 存一个slices的备份
        self.slices_Wang = deepcopy(self.slices)
        self.slices_Yuan = deepcopy(self.slices)
        # print("Open:", self.slices.shape)
        self.slicesRGB = deepcopy(self.slices)

    def refeshGraph_01(self, img):
        img = img.astype(uint8)  # 转换为0--255的灰度uint8类型
        try:
            img = resize(src=img, dsize=None, fx=1, fy=1)
        except:
            print("IndexError")
        img2 = cvtColor(img, COLOR_BGR2RGB)
        img2[where((img2 == [255, 255, 255]).all(axis=2))] = [255, 0, 0]
        img2[where((img2 == [254, 254, 254]).all(axis=2))] = [0, 255, 0]
        img2[where((img2 == [253, 253, 253]).all(axis=2))] = [152, 245, 255]

        # 将nparray转化成QImage对象显示在QLabel中
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        self.pixmap_imgSrc_1 = QPixmap.fromImage(image).scaled(self.label_2_width, self.label_2_height)
        self.label_2.setPixmap(self.pixmap_imgSrc_1)
        # 图片在label中居中显示
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setScaledContents(False)

    def refeshMaxGraph_01(self, img, img_x, img_y):
        img = img.astype(uint8)  # 转换为0--255的灰度uint8类型
        try:
            img = resize(src=img, dsize=None, fx=1, fy=1)
        except:
            print("IndexError")
        img2 = cvtColor(img, COLOR_BGR2RGB)
        img2[where((img2 == [255, 255, 255]).all(axis=2))] = [255, 0, 0]
        img2[where((img2 == [254, 254, 254]).all(axis=2))] = [0, 255, 0]
        img2[where((img2 == [253, 253, 253]).all(axis=2))] = [152, 245, 255]

        # 将nparray转化成QImage对象显示在QLabel中
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)

        # 计算图像应该显示的左上角坐标
        label_x = max(0, img_x - self.label_2_width // 2)
        label_y = max(0, img_y - self.label_2_height // 2)

        self.pixmap_imgSrc_1 = QPixmap.fromImage(image).scaled(self.label_2_width, self.label_2_height)
        self.label_2.setPixmap(self.pixmap_imgSrc_1)
        # 图片在label中居中显示
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setScaledContents(False)

    def refeshGraph_02(self, img):
        img = img.astype(uint8)  # 转换为0--255的灰度uint8类型
        try:
            img = resize(src=img, dsize=None, fx=1, fy=1)
        except:
            print("IndexError")
        img2 = cvtColor(img, COLOR_BGR2RGB)
        img2[where((img2 == [255, 255, 255]).all(axis=2))] = [255, 0, 0]
        img2[where((img2 == [254, 254, 254]).all(axis=2))] = [0, 255, 0]
        img2[where((img2 == [253, 253, 253]).all(axis=2))] = [152, 245, 255]
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        self.pixmap_imgSrc_2 = QPixmap.fromImage(image).scaled(self.label_3_width, self.label_3_height)
        self.label_3.setPixmap(self.pixmap_imgSrc_2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setScaledContents(False)

    def refeshGraph_03(self, img):
        img = img.astype(uint8)  # 转换为0--255的灰度uint8类型
        try:
            img = resize(src=img, dsize=None, fx=1, fy=1)
        except:
            print("IndexError")
        img2 = cvtColor(img, COLOR_BGR2RGB)
        img2[where((img2 == [255, 255, 255]).all(axis=2))] = [255, 0, 0]
        img2[where((img2 == [254, 254, 254]).all(axis=2))] = [0, 255, 0]
        img2[where((img2 == [253, 253, 253]).all(axis=2))] = [152, 245, 255]
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        self.pixmap_imgSrc_3 = QPixmap.fromImage(image).scaled(self.label_4_width, self.label_4_height)
        self.label_4.setPixmap(self.pixmap_imgSrc_3)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setScaledContents(False)


    def label_released(self):
        self.slices = deepcopy(self.Pre_slices)
        self.refeshGraph_01(self.slices[self.number - 1, :, :])
        self.refeshGraph_02(self.slices[:, :, self.number_2 - 1])
        self.refeshGraph_03(self.slices[:, self.number_3 - 1, :])
        del self.Pre_slices

    def label_2_clicked(self):
        self.Pre_slices = deepcopy(self.slices)

        self.label_2.IsClicked = False
        self.number = self.horizontalSlider.value()
        self.number_2 = round(len(self.slices[0, 0]) * (self.label_2.xPosition / 512))
        self.number_3 = round(len(self.slices[0, 0]) * (self.label_2.yPosition / 512))

        combined_text = "X: " + str(self.label_2.xPosition) + "\nY: " + str(
            self.label_2.yPosition) + "\nZ: " + str(self.number)
        self.PositioLabel.setText(combined_text)

        self.xPosition = self.label_2.xPosition
        self.yPosition = self.label_2.yPosition

        try:
            self.slices[self.number - 1, :, self.label_2.xPosition] = 253
            self.slices[self.number - 1, :, self.label_2.xPosition - 1] = 253
            self.slices[self.number - 1, self.label_2.yPosition, :] = 253
            self.slices[self.number - 1, self.label_2.yPosition - 1, :] = 253
            self.slices[:, self.number_3 - 1, self.number_2 - 1] = 253
            self.slices[:, self.number_3, self.number_2 - 1] = 253
            self.slices[:, self.number_3 - 1, self.number_2] = 253
        except:
            pass

        self.refeshGraph_01(self.slices[self.number - 1, :, :])
        self.refeshGraph_02(self.slices[:, :, self.number_2 - 1])
        self.refeshGraph_03(self.slices[:, self.number_3 - 1, :])
        self.horizontalSlider_2.setValue(self.number_2)
        self.horizontalSlider_3.setValue(self.number_3)

    def label_3_clicked(self):
        self.Pre_slices = deepcopy(self.slices)

        self.label_3.IsClicked = False
        self.number = round(len(self.slices) * (self.label_3.yPosition / 512))
        self.number_3 = round(len(self.slices[0, 0]) * (self.label_3.xPosition / 512))

        combined_text = "X: " + str(self.number_2) + "\nY: " + str(
            self.label_3.xPosition) + "\nZ: " + str(self.number)
        self.PositioLabel.setText(combined_text)

        self.Pre_slices = deepcopy(self.slices)
        try:
            self.slices[self.number - 1, :, self.number_2] = 253
            self.slices[self.number - 1, :, self.number_2 - 1] = 253
            self.slices[self.number - 1, self.label_3.xPosition, :] = 253
            self.slices[self.number - 1, self.label_3.xPosition - 1, :] = 253
            self.slices[:, self.number_3 - 1, self.number_2 - 1] = 253
            self.slices[:, self.number_3, self.number_2 - 1] = 253
            self.slices[:, self.number_3 - 1, self.number_2] = 253
        except:
            pass

        self.refeshGraph_01(self.slices[self.number - 1, :, :])
        self.refeshGraph_02(self.slices[:, :, self.number_2 - 1])
        self.refeshGraph_03(self.slices[:, self.number_3 - 1, :])
        self.horizontalSlider.setValue(self.number)
        self.horizontalSlider_3.setValue(self.number_3)

    def label_4_clicked(self):
        self.Pre_slices = deepcopy(self.slices)

        self.label_4.IsClicked = False
        self.number = round(len(self.slices) * (self.label_4.yPosition / 512))
        self.number_2 = round(len(self.slices[0, 0]) * (self.label_4.xPosition / 512))

        combined_text = "X: " + str(self.label_4.xPosition) + "\nY: " + str(
            self.number_3) + "\nZ: " + str(self.number)
        self.PositioLabel.setText(combined_text)
        self.Pre_slices = deepcopy(self.slices)
        try:
            self.slices[self.number - 1, :, self.label_4.xPosition] = 253
            self.slices[self.number - 1, :, self.label_4.xPosition - 1] = 253
            self.slices[self.number - 1, self.number_3, :] = 253
            self.slices[self.number - 1, self.number_3 - 1, :] = 253
            self.slices[:, self.number_3 - 1, self.number_2 - 1] = 253
            self.slices[:, self.number_3, self.number_2 - 1] = 253
            self.slices[:, self.number_3 - 1, self.number_2] = 253
        except:
            pass
        self.refeshGraph_01(self.slices[self.number - 1, :, :])
        self.refeshGraph_02(self.slices[:, :, self.number_2 - 1])
        self.refeshGraph_03(self.slices[:, self.number_3 - 1, :])
        self.horizontalSlider.setValue(self.number)
        self.horizontalSlider_2.setValue(self.number_2)

    def on_combobox_activated(self, index):
        selected_option = self.choices.itemText(index)
        if selected_option == "3D CNN 最终CMB":
            print("成功选择了 '3D CNN 最终CMB'")
            # 设置标志位表示 "3D CNN 最终CMB" 被选择
            self.cmb_option_selected = True

    def on_choosepicture_clicked(self):
        print("点击了 '开始识别'")

        # 运行 data_preprocess_v2.py
        preprocess_script = "data_preprocess_v2.py"
        try:
            subprocess.call(["python", preprocess_script])
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                print(f"无法找到脚本：{preprocess_script}")
            else:
                print(f"运行脚本时发生错误：{e}")


        # 检查是否已经选择了 "3D CNN 最终CMB"，如果是，则触发 run_code_2 函数
        if self.cmb_option_selected:
            print("成功同时选择了 '3D CNN 最终CMB' 和 '开始识别'")

            time.sleep(2)

            # 添加调用 evaluate.py 的命令
            evaluate_script = "evaluate.py"
            try:
                subprocess.call(
                    ["python", evaluate_script, "-f", "1", "-sn", "SCREEN1", "-dn", "DISCRI1", "-un", "UNET1"])
            except OSError as e:
                if e.errno == os.errno.ENOENT:
                    print(f"无法找到脚本：{evaluate_script}")
                else:
                    print(f"运行脚本时发生错误：{e}")

"""            self.run_code_2_z(self.fp[0])
            time.sleep(2)
            self.run_code_2_y(self.fp[0])
            time.sleep(2)
            self.run_code_2_x(self.fp[0])"""
"""
    def run_code_2_z(self, nii_file_path):

        # 读取.mat文件
        data = sio.loadmat("modified_detection.mat")

        # 获取三维坐标
        cmb = data['cmb']

        # 在新图像上标记已知点
        known_points = []
        for x in cmb:
            for y in x:
                m = y[0]
                x = m[0]
                y = m[1]
                z = m[2]
                known_points.append((x, y, z))

        plt.figure()

        # 读取NIfTI格式的脑部图像
        img = nib.load(nii_file_path)
        brain_image = img.get_fdata()

        # z切片
        plt.imshow(brain_image[:, :, z].T, cmap='gray')  # z_slice是所选的切片
        plt.axis('off')  # 关闭坐标轴
        plt.title('')  # 清空标题
        for point in known_points:
            x, y, z = point
            plt.scatter(x, y, c='red', marker='o', s=50)  # 使用红色圆圈标记点
            # plt.text(x, y, f'({x}, {y}, {z})', fontsize=12, color='red', ha='right')

        plt.savefig('temp_image1.png')  # 保存图像为临时文件
        plt.show()

        # 读取临时图像文件，将其显示在 label_2 中，并填充整个 label_2
        image = QImage('temp_image1.png')
        pixmap = QPixmap.fromImage(image).scaledToWidth(self.label_2_width).scaledToHeight(self.label_2_height)
        self.label_2.setPixmap(pixmap)

        # 图片在label中居中显示
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setScaledContents(False)

    def run_code_2_y(self, nii_file_path):

        # 读取.mat文件
        data = sio.loadmat('modified_detection.mat')

        # 获取三维坐标
        cmb = data['cmb']

        # 在新图像上标记已知点
        known_points = []
        for x in cmb:
            for y in x:
                m = y[0]
                x = m[0]
                y = m[1]
                z = m[2]
                known_points.append((x, y, z))

        plt.figure()

        # 读取NIfTI格式的脑部图像
        img = nib.load(nii_file_path)
        brain_image = img.get_fdata()

        # z切片
        plt.imshow(brain_image[:, y, :].T, cmap='gray')  # z_slice是所选的切片
        plt.axis('off')  # 关闭坐标轴
        plt.title('')  # 清空标题
        for point in known_points:
            x, y, z = point
            plt.scatter(x, z, c='red', marker='o', s=50)  # 使用红色圆圈标记点
            # plt.text(x, y, f'({x}, {y}, {z})', fontsize=12, color='red', ha='right'    )

        plt.savefig('temp_image2.png')  # 保存图像为临时文件
        plt.show()
        # 读取临时图像文件，将其显示在 label_2 中，并填充整个 label_2
        image = QImage('temp_image2.png')
        pixmap = QPixmap.fromImage(image).scaledToWidth(self.label_4_width).scaledToHeight(self.label_4_height)
        self.label_4.setPixmap(pixmap)

        # 图片在label中居中显示
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setScaledContents(False)

    def run_code_2_x(self, nii_file_path):

        # 读取.mat文件
        data = sio.loadmat('modified_detection.mat')

        # 获取三维坐标
        cmb = data['cmb']

        # 在新图像上标记已知点
        known_points = []
        for x in cmb:
            for y in x:
                m = y[0]
                x = m[0]
                y = m[1]
                z = m[2]
                known_points.append((x, y, z))

        plt.figure()

        # 读取NIfTI格式的脑部图像
        img = nib.load(nii_file_path)
        brain_image = img.get_fdata()

        # z切片
        plt.imshow(brain_image[x, :, :].T, cmap='gray')  # z_slice是所选的切片
        plt.axis('off')  # 关闭坐标轴
        plt.title('')  # 清空标题
        for point in known_points:
            x, y, z = point
            plt.scatter(y, z, c='red', marker='o', s=50)  # 使用红色圆圈标记点
            # plt.text(x, y, f'({x}, {y}, {z})', fontsize=12, color='red', ha='right')

        plt.savefig('temp_image3.png')  # 保存图像为临时文件
        plt.show()

        # 读取临时图像文件，将其显示在 label_2 中，并填充整个 label_2
        image = QImage('temp_image3.png')
        pixmap = QPixmap.fromImage(image).scaledToWidth(self.label_3_width).scaledToHeight(self.label_3_height)
        self.label_3.setPixmap(pixmap)

        # 图片在label中居中显示
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setScaledContents(True)


"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
