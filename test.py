#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
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
import shutil
import nibabel as nib
import numpy as np
from PIL import Image
from ultralytics import YOLO
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QFileDialog, QLabel
import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk, ImageDraw
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from MyLabel import MyLabel

from CMB_Segmentation.evaluate import evaluation

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Ui_MainWindow(QMainWindow):
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        # 在这里为整个窗口启用鼠标跟踪
        self.image_files = None
        self.current_index = 0
        self.image_path = None
        self.setMouseTracking(True)

        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1500, 1200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./dataset/pic/icon.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 4
        self.choosepicture = QtWidgets.QPushButton(self.centralwidget)
        self.choosepicture.setGeometry(QtCore.QRect(570, 30, 211, 50))
        self.choosepicture.setObjectName("choosepicture")

        # 修改
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(70, 550, 150, 70))
        self.changeButton.setObjectName("changeButton")

        self.draw_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_button.setGeometry(QtCore.QRect(250, 550, 150, 70))
        self.draw_button.setObjectName("draw_button")

        self.choices = QtWidgets.QComboBox(self.centralwidget)
        self.choices.setGeometry(QtCore.QRect(230, 30, 300, 50))
        self.choices.setObjectName("choices")
        self.choices.addItem("")
        self.choices.addItem("")
        self.choices.addItem("")
        self.chooseLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseLabel.setGeometry(QtCore.QRect(40, 30, 200, 50))
        self.chooseLabel.setObjectName("chooseLabel")

        # self.BigLabel = ImageLabel()
        # QtWidgets.addWidget(self.label)
        self.BigLabel = QtWidgets.QLabel(self.centralwidget)
        self.BigLabel.setGeometry(QtCore.QRect(40, 120, 400, 400))
        self.BigLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BigLabel.setObjectName("BigLabel")

        self.BigPositionLabel = QtWidgets.QLabel(self.centralwidget)
        self.BigPositionLabel.setGeometry(QtCore.QRect(40, 670, 400, 200))
        self.BigPositionLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BigPositionLabel.setObjectName("BigPositionLabel")
        self.BigPositionLabel.setWordWrap(True)

        self.PositioLabel = QtWidgets.QLabel(self.centralwidget)
        self.PositioLabel.setGeometry(QtCore.QRect(40, 890, 400, 150))
        self.PositioLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PositioLabel.setObjectName("PositioLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 30, 211, 50))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(500, 100, 900, 1000))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 40, 900, 1000))
        self.widget.setObjectName("widget")
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setGeometry(QtCore.QRect(90, 430, 300, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(90, 900, 300, 20))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(500, 900, 300, 20))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(440, 10, 400, 400))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_2 = MyLabel(text='', connect=[self.PositioLabel, self.horizontalSlider], IsClicked=False)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 400, 400))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_2_width = self.label_2.width()
        self.label_2_height = self.label_2.height()
        self.label_3 = MyLabel(text='', connect=[self.PositioLabel, self.horizontalSlider_2], IsClicked=False)
        self.label_3.setGeometry(QtCore.QRect(20, 480, 400, 400))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_3_width = self.label_3.width()
        self.label_3_height = self.label_3.height()
        self.label_4 = MyLabel(text='', connect=[self.PositioLabel, self.horizontalSlider_3], IsClicked=False)
        self.label_4.setGeometry(QtCore.QRect(440, 480, 400, 400))
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

        # 连接下拉框的activated信号到自定义的函数2
        self.choices.activated.connect(self.on_combobox_activated)
        self.choosepicture.clicked.connect(self.on_choosepicture_clicked)
        self.cmb_YOLOoption_selected = False
        self.cmb_FCNoption_selected = False
        # 在初始化中添加一个标志位，表示 "3D CNN 最终CMB" 是否被选择
        self.cmb_CNNoption_selected = False

        # 修改
        self.changeButton.clicked.connect(self.on_changeButton_clicked)

        self.draw_button.clicked.connect(self.startDrawing)

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

        #################################
        self.actionoutput_file.triggered.connect(self.generate_medical_report)

        ##################################
        self.actionoutput_file.triggered.connect(self.out_file)

        self.actiondrawing.triggered.connect(self.startDrawing)

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
        # 1
        self.choosepicture.setText(_translate("MainWindow", "Start Recognition"))

        # 修改
        self.changeButton.setText(_translate("MainWindow", "NEXT"))
        self.draw_button.setText(_translate("MainWindow", "DRAW"))

        self.choices.setItemText(0, _translate("MainWindow", "YOLO Detection"))
        self.choices.setItemText(1, _translate("MainWindow", "FCN Primary Screen"))
        self.choices.setItemText(2, _translate("MainWindow", "3D CNN + UNET Final CMB"))
        self.chooseLabel.setText(_translate("MainWindow", "Function Selection"))
        self.BigLabel.setText(_translate("MainWindow", "YOLO Detection Picture"))
        self.BigPositionLabel.setText(_translate("MainWindow", "YOLO Coordinates"))
        self.PositioLabel.setText(_translate("MainWindow", "Three-dimensional Coordinate"))
        self.pushButton.setText(_translate("MainWindow", "Exit Recognition"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_5.setText(_translate("MainWindow", "Enlarged View"))
        self.label_4.setText(_translate("MainWindow", "Coronal Section"))
        self.label_2.setText(_translate("MainWindow", "Transverse Section"))
        self.label_3.setText(_translate("MainWindow", "Median Sagittal Section"))
        self.menumune.setTitle(_translate("MainWindow", "FILE"))
        self.menuEDIT.setTitle(_translate("MainWindow", "EDIT"))
        self.menuHELP.setTitle(_translate("MainWindow", "HELP"))
        self.actioninput_file.setText(_translate("MainWindow", "input file"))
        self.actionoutput_file.setText(_translate("MainWindow", "output file"))
        self.actionabout_us.setText(_translate("MainWindow", "about us"))
        self.actiondrawing.setText(_translate("MainWindow", "drawing"))

    #####################################################
    def generate_medical_report(self):
        results_folder = './detection_results'

        # 创建存储报告的文件夹
        report_folder = os.path.join('./', "reports")
        os.makedirs(report_folder, exist_ok=True)

        # 报告文件路径
        report_file = os.path.join(report_folder, "medical_report.html")
        with open(report_file, 'w') as report:
            # 写入 HTML 头部
            report.write("<html><head><title>Medical Report</title></head><body>")

            # 遍历detection_results文件夹
            for filename in os.listdir(results_folder):
                if filename.endswith('.txt'):
                    txt_path = os.path.join(results_folder, filename)
                    image_path = os.path.relpath(os.path.join(results_folder, filename.replace('.txt', '.jpg')),
                                                 report_folder)

                    # 读取txt文件中的信息
                    with open(txt_path, 'r') as txt_file:
                        object_type = txt_file.readline().strip().split(': ')[1]
                        coordinates = txt_file.readline().strip().split(': ')[1][1:-1].split(', ')
                        probability = txt_file.readline().strip().split(': ')[1]

                    # 将信息写入报告
                    report.write(f"<p>Object Type: {object_type}</p>\n")
                    report.write(f"<p>Coordinates: {coordinates}</p>\n")
                    report.write(f"<p>Probability: {probability}</p>\n")

                    # 插入图片
                    report.write(f"<img src='{image_path}' alt='Image' width='400'><br><br>")

            # 写入 HTML 尾部
            report.write("</body></html>")

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
            # return self.fp[0]

    def out_file(self):
        print("a")

    def setInitGraph_01(self, value):
        self.number_3 = self.horizontalSlider_3.value()
        img = resize(src=self.slices[value - 1, :, :], dsize=None, fx=1, fy=1)
        img2 = cvtColor(img, COLOR_BGR2RGB)
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        # transform = QTransform().rotate(180)
        # image = image.transformed(transform)

        pixmap_imgSrc_1 = QPixmap.fromImage(image).scaled(self.label_2_width, self.label_2_height)

        # 修改
        borrar_carpeta("./detection_results/")

        return pixmap_imgSrc_1

    def setInitGraph_02(self, value):
        img = resize(src=self.slices[:, :, value - 1], dsize=None, fx=1, fy=1)
        img2 = cvtColor(img, COLOR_BGR2RGB)
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        # transform = QTransform().rotate(180)
        # image = image.transformed(transform)

        self.pixmap_imgSrc_2 = QPixmap.fromImage(image).scaled(self.label_3_width, self.label_3_height)
        return self.pixmap_imgSrc_2

    def setInitGraph_03(self, value):
        img = resize(src=self.slices[:, value - 1, :], dsize=None, fx=1, fy=1)
        img2 = cvtColor(img, COLOR_BGR2RGB)
        image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888)
        #
        # transform = QTransform().rotate(180)
        # image = image.transformed(transform)

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
        # transform = QTransform().rotate(180)
        # image = image.transformed(transform)
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
        # transform = QTransform().rotate(180)
        # image = image.transformed(transform)
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
        # transform = QTransform().rotate(180)
        # image = image.transformed(transform)
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
        # transform = QTransform().rotate(180)
        # image = image.transformed(transform)
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

        ###################################################
        # 获取当前的pixmap
        pixmap = self.label_2.pixmap()

        if pixmap is not None:
            # 获取当前pixmap的大小
            current_size = pixmap.size()

            # 计算放大倍数
            scale_factor = 2.0

            # 计算放大后的宽度和高度
            enlarged_width = current_size.width() * scale_factor
            enlarged_height = current_size.height() * scale_factor

            # 计算放大区域的左上角位置，以鼠标位置为中心
            enlarged_x = max(0, int(self.label_2.xPosition - enlarged_width / 4))
            enlarged_y = max(0, int(self.label_2.yPosition - enlarged_height / 4))

            # 创建一个矩形来表示放大的区域，周围一定范围内的图像
            enlarged_rect = QRect(enlarged_x, enlarged_y, int(enlarged_width / 2), int(enlarged_height / 2))

            # 裁剪并放大图像
            enlarged_pixmap = pixmap.copy(enlarged_rect)
            enlarged_pixmap = enlarged_pixmap.scaled(int(enlarged_width), int(enlarged_height), Qt.KeepAspectRatio)

            # 在 label_5 中显示放大后的图像
            self.label_5.setPixmap(enlarged_pixmap)

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

        ###################################################
        # 获取当前的pixmap
        pixmap = self.label_3.pixmap()

        if pixmap is not None:
            # 获取当前pixmap的大小
            current_size = pixmap.size()

            # 计算放大倍数
            scale_factor = 2.0

            # 计算放大后的宽度和高度
            enlarged_width = current_size.width() * scale_factor
            enlarged_height = current_size.height() * scale_factor

            # 计算放大区域的左上角位置，以鼠标位置为中心
            enlarged_x = max(0, int(self.label_3.xPosition - enlarged_width / 4))
            enlarged_y = max(0, int(self.label_3.yPosition - enlarged_height / 4))

            # 创建一个矩形来表示放大的区域，周围一定范围内的图像
            enlarged_rect = QRect(enlarged_x, enlarged_y, int(enlarged_width / 2), int(enlarged_height / 2))

            # 裁剪并放大图像
            enlarged_pixmap = pixmap.copy(enlarged_rect)
            enlarged_pixmap = enlarged_pixmap.scaled(int(enlarged_width), int(enlarged_height), Qt.KeepAspectRatio)

            # 在 label_5 中显示放大后的图像
            self.label_5.setPixmap(enlarged_pixmap)

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

        ###################################################
        # 获取当前的pixmap
        pixmap = self.label_4.pixmap()

        if pixmap is not None:
            # 获取当前pixmap的大小
            current_size = pixmap.size()

            # 计算放大倍数
            scale_factor = 2.0

            # 计算放大后的宽度和高度
            enlarged_width = current_size.width() * scale_factor
            enlarged_height = current_size.height() * scale_factor

            # 计算放大区域的左上角位置，以鼠标位置为中心
            enlarged_x = max(0, int(self.label_4.xPosition - enlarged_width / 4))
            enlarged_y = max(0, int(self.label_4.yPosition - enlarged_height / 4))

            # 创建一个矩形来表示放大的区域，周围一定范围内的图像
            enlarged_rect = QRect(enlarged_x, enlarged_y, int(enlarged_width / 2), int(enlarged_height / 2))

            # 裁剪并放大图像
            enlarged_pixmap = pixmap.copy(enlarged_rect)
            enlarged_pixmap = enlarged_pixmap.scaled(int(enlarged_width), int(enlarged_height), Qt.KeepAspectRatio)

            # 在 label_5 中显示放大后的图像
            self.label_5.setPixmap(enlarged_pixmap)

    def on_combobox_activated(self, index):
        selected_option = self.choices.itemText(index)
        if selected_option == "YOLO Detection":
            print("成功选择了 'YOLO 检测'")
            self.cmb_YOLOoption_selected = True

        if selected_option == "FCN Primary Screen":
            print("成功选择了 'FCN 初筛'")
            self.cmb_FCNoption_selected = True

        if selected_option == "3D CNN + UNET Final CMB":
            print("成功选择了 '3D CNN 最终CMB'")
            # 设置标志位表示 "3D CNN 最终CMB" 被选择
            self.cmb_CNNoption_selected = True

    def on_choosepicture_clicked(self, slices=zeros((1, 512, 512))):
        print("点击了 '开始识别'")

        if self.cmb_YOLOoption_selected:
            print("成功同时选择了 'YOLO 检测' 和 '开始识别'")
            time.sleep(2)
            print(self.fp[0])
            input_nii_path = self.fp[0]  # 输入NIfTI图像的路径
            output_folder = "./dataset/jpg/"  # JPEG图像的输出文件夹
            nii_to_jpg(input_nii_path, output_folder)
            detect(output_folder)
            self.current_index = 0
            self.image_files = [f for f in os.listdir("./detection_results/") if f.endswith('.jpg')]
            self.showImage(self.current_index)

            self.cmb_YOLOoption_selected = False

        if self.cmb_FCNoption_selected:
            print("成功同时选择了 'FCN ' 和 '开始识别'")
            self.cmb_CNNoption_selected = False
            array = []
            self.fp = ['./CMB_Segmentation/results/sub-222_volume.nii.gz', 'All Files (*)']
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
                self.cmb_FCNoption_selected = False
                evaluation()

        # 检查是否已经选择了 "3D CNN 最终CMB"，如果是，则触发 run_code_2 函数
        if self.cmb_CNNoption_selected:
            print("成功同时选择了 '3D CNN 最终CMB' 和 '开始识别'")
            print("evaluation()运行时间超过半分钟，跳过evaluation()")

            array = []
            self.fp = ['./CMB_Segmentation/results/sub-222_seg.nii.gz', 'All Files (*)']
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
                    Label_Direction = 1
                # 对图像数组进行预处理
                img3D_array = deepcopy(self.preprocessing(img3D_array))
                # 打开图像并显示
                self.open(img3D_array)
                # 设置滑动条的最大值和值
                self.horizontalSlider.setMaximum(self.slices.shape[0])

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
                self.cmb_CNNoption_selected = False
                evaluation()

    def showImage(self, index):
        self.image_path = os.path.join("./detection_results/", self.image_files[index])
        pixmap = QPixmap(self.image_path)
        self.BigLabel.setPixmap(pixmap)
        self.BigLabel.setScaledContents(True)
        self.showPositionInfo(self.current_index)

    def showPositionInfo(self, index):
        image_name = self.image_files[index]
        self.BigPositionLabel.setText(f"{image_name}\n")

        txt_name = os.path.splitext(image_name)[0] + '.txt'
        txt_path = os.path.join("./detection_results/", txt_name)
        if os.path.exists(txt_path):
            with open(txt_path, 'r') as f:
                txt_content = f.read()
            self.BigPositionLabel.setText(f"{image_name}\n{txt_content}")
        else:
            self.BigPositionLabel.setText(f"{image_name}\nNo text file found.")

    def on_changeButton_clicked(self):
        self.current_index = (self.current_index + 1) % len(self.image_files)
        self.showImage(self.current_index)

    def startDrawing(self):
        print("draw")
        root = tk.Tk()
        app = ImageAnnotationApp(root)
        print(self.image_path)
        app.load_image(self.image_path)
        root.mainloop()


def nii_to_jpg(input_nii_path, output_folder):
    # Load NIfTI image
    nii_img = nib.load(input_nii_path)
    nii_data = nii_img.get_fdata()

    # Normalize pixel values to [0, 255]
    normalized_data = (nii_data - np.min(nii_data)) / (np.max(nii_data) - np.min(nii_data)) * 255
    normalized_data = normalized_data.astype(np.uint8)

    # Slice through depth and save each slice as JPEG
    for i in range(nii_data.shape[2]):
        slice_img = normalized_data[:, :, i]
        slice_img = np.rot90(slice_img)  # Optional: Rotate if needed
        slice_img = Image.fromarray(slice_img)
        slice_img.save(f"{output_folder}slice_{i}.jpg")


def detect(images_path):
    # 加载训练好的模型权重
    model = YOLO("runs/detect/best.pt")

    # 指定待预测的图像路径
    # images_path = "./dataset/jpg/"

    # 创建用于保存结果的文件夹
    output_folder = "./detection_results/"
    os.makedirs(output_folder, exist_ok=True)

    # 获取文件夹下所有图像文件
    image_files = [f for f in os.listdir(images_path) if f.endswith('.jpg')]

    for img in image_files:
        print("Processing image:", img)
        img_path = os.path.join('./runs/detect/predict/', img)

        predictions = model.predict(source=images_path + img, save=True, line_width=1)

        for result in predictions:

            if len(result.boxes) > 0:
                shutil.copyfile(img_path, os.path.join(output_folder, img))

                output_file = os.path.join(output_folder, img.replace('.jpg', f'.txt'))

                with open(output_file, 'w') as f:
                    boxes = result.boxes
                    for box in boxes:
                        class_id = result.names[box.cls[0].item()]
                        cords = box.xyxy[0].tolist()
                        cords = [round(x) for x in cords]
                        conf = round(box.conf[0].item(), 2)

                        f.write("Object type: {}\n".format(class_id))
                        f.write("Coordinates: {}\n".format(cords))
                        f.write("Probability: {}\n".format(conf))

            boxes = result.boxes

            for box in boxes:
                class_id = result.names[box.cls[0].item()]
                cords = box.xyxy[0].tolist()
                cords = [round(x) for x in cords]
                conf = round(box.conf[0].item(), 2)
                print("Object type:", class_id)
                print("Coordinates:", cords)
                print("Probability:", conf)
                print("---")
        ruta_a_borrar = './runs/detect/predict'
        borrar_carpeta(ruta_a_borrar)


def borrar_carpeta(path_carpeta):
    try:
        # Utiliza shutil.rmtree para borrar la carpeta y su contenido de forma recursiva
        shutil.rmtree(path_carpeta)
        print(f'Carpeta {path_carpeta} borrada exitosamente.')
    except Exception as e:
        print(f'Error al borrar la carpeta: {e}')


class ImageAnnotationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Annotation App")

        # 获取屏幕的宽度和高度
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 1000
        window_height = 900

        # 计算窗口在屏幕中央的位置
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2 - 50

        # 设置窗口的几何位置
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.canvas_frame = tk.Frame(self.master)
        self.canvas_frame.pack(expand=True, fill=tk.BOTH)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.image = None
        self.photo_image = None
        self.rectangles = []

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.load_button = tk.Button(self.button_frame, text="Load Image", command=self.load_image)
        self.load_button.pack(side=tk.LEFT)

        self.draw_button = tk.Button(self.button_frame, text="Draw Rectangle", command=self.start_draw)
        self.draw_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.button_frame, text="Delete Rectangle", command=self.start_delete)
        self.delete_button.pack(side=tk.LEFT)

        self.export_button = tk.Button(self.button_frame, text="Export Image", command=self.export_image)
        self.export_button.pack(side=tk.LEFT)

        self.draw_mode = False
        self.delete_mode = False
        self.start_point = None
        self.end_point = None
        self.current_rect = None
        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<B1-Motion>", self.handle_drag)

    def load_image(self, file_path=None):
        if not file_path:
            file_path = tk.filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((self.image.width * 2, self.image.height * 2))  # 将图像大小增加一倍
            self.photo_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, -100, anchor=tk.NW, image=self.photo_image)

    def start_draw(self):
        self.draw_mode = True
        self.delete_mode = False

    def start_delete(self):
        self.draw_mode = False
        self.delete_mode = True

    def handle_click(self, event):
        if self.draw_mode:
            self.start_point = (event.x, event.y)
            self.end_point = (event.x, event.y)
            # 设置矩形框的初始线宽为3
            self.current_rect = self.canvas.create_rectangle(event.x, event.y, event.x, event.y, outline='red', width=3)
            self.rectangles.append(self.current_rect)
        elif self.delete_mode:
            self.delete_rectangle(event)

    def handle_drag(self, event):
        if self.draw_mode and self.start_point is not None:
            x0, y0 = self.start_point
            x1, y1 = event.x, event.y
            self.canvas.coords(self.current_rect, x0, y0, x1, y1)

    def delete_rectangle(self, event):
        x, y = event.x, event.y
        items = self.canvas.find_overlapping(x, y, x, y)
        if items:
            for item in items:
                if item in self.rectangles:
                    self.canvas.delete(item)
                    self.rectangles.remove(item)

    def export_image(self):
        if self.image is not None:
            draw = ImageDraw.Draw(self.image)
            for rect_id in self.rectangles:
                x1, y1, x2, y2 = self.canvas.coords(rect_id)
                draw.rectangle([x1, y1, x2, y2], outline='red', width=3)
            file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.image.save(file_path)


if __name__ == "__main__":
    # pyinstaller对多进程支持很差，torch后端使用了多进程，在windows中需要freeze
    multiprocessing.freeze_support()

    app = QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
