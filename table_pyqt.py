# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import random
import json
import requests
import sqlite3
import time





# class ImgWidget1(QtWidgets.QLabel):

#     def __init__(self, imagePath, parent=None):
#         super(ImgWidget1, self).__init__(parent)
#         pic = QtGui.QPixmap(imagePath)
#         self.setAlignment(QtCore.Qt.AlignCenter)
#         self.setPixmap(pic)

# class ImageWidget(QtWidgets.QWidget):

#     def __init__(self, imagePath, parent):
#         super(ImageWidget, self).__init__(parent)
#         self.picture = QtGui.QPixmap(imagePath)

#     def paintEvent(self, event):
#         painter = QtGui.QPainter(self)
#         painter.drawPixmap(0, 0, self.picture)


class Ui_MainWindow(object):
    
    def addData(self):
        # db = sqlite3.connect('whatever.sqlite3')
        # c = db.cursor()
        # c.execute(
        #     'SELECT * FROM(SELECT * FROM CarData ORDER BY id DESC LIMIT 10)ORDER BY id ASC')
        # items = c.fetchall()
        # print(items)
        # for item in items:
            # print(items)
            # print("{}{}{}{}".format(
            #     item[0], item[1], item[2], item[3]))
        
        connection=sqlite3.connect('data_from_mqtt.sqlite3')
        query = "SELECT * FROM(SELECT * FROM CarData ORDER BY id DESC LIMIT 11)ORDER BY id DESC"
        result= connection.execute(query)
        # print(result)
        self.tableWidget.setRowCount(0)
        for row_no, row_data in enumerate(result ):
            self.tableWidget.insertRow(row_no)
            for col_no, data in enumerate(row_data):

                self.tableWidget.setItem(
                    row_no, col_no, QtWidgets.QTableWidgetItem(str(data)))
                # if(col_no==4):
                #     pic = QtGui.QPixmap(
                #         "https://flyawaysimulation.com/images/downloadshots/7592-road-v11zip-84-screen-9.jpg")
                #     self.label = QtWidgets.QLabel()
                #     self.label.setPixmap(pic)
                #     self.tableWidget.setItem(
                #         row_no, col_no, self.label)
        connection.close()
        # db.close()
        QtCore.QTimer.singleShot(100, self.addData)
    def setupUi(self, MainWindow,rect):
        Wwidth=rect.width()
        Wheight=rect.height()
        MainWindow.setObjectName("MainWindow")
        # MainWindow.r

        # MainWindow.resize(850, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.setGeometry(showMaximized())
        self.tableWidget.setGeometry(QtCore.QRect(0, 0,Wwidth ,Wheight ))
        # self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.rowResized(50, 50, 50)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderLabels(
            ['id', 'Name', 'cpn', 'image_cpn'])
        # self.tableWidget.setRowCount(5)


        pic = "https://flyawaysimulation.com/images/downloadshots/7592-road-v11zip-84-screen-9.jpg"
        # url = "https://flyawaysimulation.com/images/downloadshots/7592-road-v11zip-84-screen-9.jpg"
        
        # image extension *.png,*.jpg
        
        # pic = Image.open(requests.get(url, stream=True).raw)
        
        # new_width = 100
        # new_height = 100
        # pic = pic.resize((new_width, new_height), Image.ANTIALIAS)

        r = requests.get(pic, stream=True)
        assert r.status_code == 200
        img = QtGui.QImage()

        assert img.loadFromData(r.content)

        self.label = QtWidgets.QLabel()
        # self.label.setFixedHeight(100)
        # self.label.setPixmap(QtGui.QPixmap.fromImage(img))
        self.label.setPixmap(QtGui.QPixmap(img).scaled(
            QtCore.QSize(250, 100), QtCore.Qt.KeepAspectRatio))
        

        Hheader = self.tableWidget.horizontalHeader()
        # Hheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        Hheader.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # Hheader.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # Hheader.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        Vheader = self.tableWidget.verticalHeader()
        # Vheader.setSectionResizeMode(0, QtWidgets.QHeaderView.)
        Vheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # Vheader.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # Vheader.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        # self.tableWidget.setItem(
        #     1, 0, QtWidgets.QTableWidgetItem("1"))
        # self.tableWidget.setItem(
        #     1, 1, QtWidgets.QTableWidgetItem("Honda"))
        # self.tableWidget.setItem(
        #     1, 2, QtWidgets.QTableWidgetItem("KL08U0045"))

        # self.tableWidget.setCellWidget(1, 3, (self.label))

        # self.load_button = QtWidgets.QPushButton(self.centralwidget)
        # self.load_button.setGeometry(QtCore.QRect(110, 320, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)

        # self.load_button.setFont(font)
        # self.load_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.load_button.setObjectName("load_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.load_button.clicked.connect((self.addData))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        QtCore.QTimer.singleShot(100, self.addData)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("MainWindow", "Block"))
        # item = self.tableWidget.item(0, 1)
        # item.setText(_translate("MainWindow", "CPN"))
        # item = self.tableWidget.item(0, 2)
        # item.setText(_translate("MainWindow", "DIR"))
        # item = self.tableWidget.item(0, 3)
        # item.setText(_translate("MainWindow", "img_bb"))
        # item = self.tableWidget.item(0, 4)
        # item.setText(_translate("MainWindow", "img_cpn"))
        # item = self.tableWidget.item(0, 5)
        # item.setText(_translate("MainWindow", "img_usr"))
        # item = self.tableWidget.item(0, 6)
        # item.setText(_translate("MainWindow", "SID"))
        # item = self.tableWidget.item(0, 7)
        # item.setText(_translate("MainWindow", "TS"))
        # item = self.tableWidget.item(0, 8)
        # item.setText(_translate("MainWindow", "TS_r"))
        # item = self.tableWidget.item(0, 9)
        # item.setText(_translate("MainWindow", "VID"))
        # item = self.tableWidget.item(0, 10)
        # item.setText(_translate("MainWindow", "VT"))
        # item = self.tableWidget.item(0, 11)
        # item.setText(_translate("MainWindow", "Zone"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        # self.load_button.setText(_translate("MainWindow", "Load Data"))


if __name__ == "__main__":
    import sys
    db = sqlite3.connect('data_from_mqtt.sqlite3')
    db.execute('DELETE FROM CarData;')
    db.commit()
    db.close()
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    # print('Screen: %s' % screen.name())
    size = screen.size()
    # print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    # print('Available: %d x %d' % (rect.width(), rect.height()))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,rect)
    # MainWindow.show()

    MainWindow.showMaximized()
    sys.exit(app.exec_())
