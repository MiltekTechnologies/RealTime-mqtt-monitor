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
import boto3


client = boto3.client('s3')
bucket_name = 'demo-blugraph-services'


class Ui_MainWindow(object):
    count=0
    Wwidth=0
    Wheight=0
    def addData(self):
        connection=sqlite3.connect('data_from_mqtt.sqlite3')
        query = "SELECT name,class_st,cpn,image FROM(SELECT * FROM CarData ORDER BY id DESC LIMIT 11)ORDER BY id DESC"
        result= connection.execute(query)
        row_count = connection.execute("select * from CarData")
        #print(result)
        
        row_num = len(row_count.fetchall())
        if self.count==1:
            pass
        else:
            self.tableWidget.setRowCount(0)
            for row_no, row_data in enumerate(result):
                #self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(row_no)
                for col_no, data in enumerate(row_data):
                    if(col_no==3):
                        pic = client.generate_presigned_url('get_object', Params = { 'Bucket': bucket_name, 'Key':data, }, 
                                                ExpiresIn = 86400, )
                        r = requests.get(pic, stream=True)
                        assert r.status_code == 200
                        img = QtGui.QImage()
                        assert img.loadFromData(r.content)
                        self.label = QtWidgets.QLabel()
                        self.label.setAlignment(QtCore.Qt.AlignCenter)
                        self.label.setPixmap(QtGui.QPixmap(img).scaled(QtCore.QSize(250, 150), QtCore.Qt.KeepAspectRatio))
                        self.tableWidget.setCellWidget(row_no, col_no, self.label)
                    else:
                        self.tableWidget.setItem(row_no, col_no, QtWidgets.QTableWidgetItem(str(data)))
            
        if row_num==1:
            self.count=1
        else:
            self.count=0
        connection.close()
        # db.close()
        QtCore.QTimer.singleShot(100, self.addData)
        
    def setupUi(self, MainWindow,rect):
        self.Wwidth = rect.width() - rect.width()/48
        self.Wheight = rect.height()-rect.height()/17
        MainWindow.setObjectName("MainWindow")
        # MainWindow.r

        # MainWindow.resize(850, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.setGeometry(showMaximized())
        self.tableWidget.setGeometry(QtCore.QRect(10, 0,self.Wwidth ,self.Wheight ))
        # self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.rowResized(50, 50, 50)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setFont(QtGui.QFont('Arial',20))
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderLabels(
            ['Name', 'Class', 'cpn', 'image_cpn'])

        

        Hheader = self.tableWidget.horizontalHeader()
        # Hheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        Hheader.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # Hheader.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        Hheader.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        Vheader = self.tableWidget.verticalHeader()
        Vheader.setDefaultSectionSize(150)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
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
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        # self.load_button.setText(_translate("MainWindow", "Load Data"))


if __name__ == "__main__":
    import sys
    db = sqlite3.connect('data_from_mqtt' + '.sqlite3')
    db.execute('DELETE FROM CarData')
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
