# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\PyProjects\ximalaya_qt\uiFile\XMLYWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MatWindow(object):
    def setupUi(self, MatWindow):
        MatWindow.setObjectName("MatWindow")
        MatWindow.resize(1121, 602)
        self.centralwidget = QtWidgets.QWidget(MatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_mini = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mini.setGeometry(QtCore.QRect(1030, 10, 31, 28))
        self.pushButton_mini.setText("")
        self.pushButton_mini.setObjectName("pushButton_mini")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(1080, 10, 31, 28))
        self.pushButton_close.setText("")
        self.pushButton_close.setShortcut("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(0, 10, 93, 28))
        self.pushButton_back.setObjectName("pushButton_back")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 30, 1111, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(410, 40, 20, 101))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_Keyword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Keyword.setGeometry(QtCore.QRect(70, 100, 113, 31))
        self.lineEdit_Keyword.setObjectName("lineEdit_Keyword")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_getid = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_getid.setGeometry(QtCore.QRect(270, 100, 93, 31))
        self.pushButton_getid.setObjectName("pushButton_getid")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 150, 1071, 391))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(530, 100, 113, 31))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.pushButton_download = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_download.setGeometry(QtCore.QRect(1020, 100, 93, 31))
        self.pushButton_download.setObjectName("pushButton_download")
        self.lineEdit_Num = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Num.setGeometry(QtCore.QRect(720, 100, 41, 31))
        self.lineEdit_Num.setObjectName("lineEdit_Num")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(670, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_Path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Path.setGeometry(QtCore.QRect(850, 100, 113, 31))
        self.lineEdit_Path.setObjectName("lineEdit_Path")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(780, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_OpenPath = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OpenPath.setGeometry(QtCore.QRect(970, 100, 31, 31))
        self.pushButton_OpenPath.setObjectName("pushButton_OpenPath")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 130, 1111, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 80, 211, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 80, 391, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 211, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(890, 60, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 60, 311, 20))
        self.label_11.setObjectName("label_11")
        MatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        MatWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MatWindow)
        self.statusbar.setObjectName("statusbar")
        MatWindow.setStatusBar(self.statusbar)
        self.action_Mat = QtWidgets.QAction(MatWindow)
        self.action_Mat.setObjectName("action_Mat")
        self.action_Wav = QtWidgets.QAction(MatWindow)
        self.action_Wav.setObjectName("action_Wav")

        self.retranslateUi(MatWindow)
        QtCore.QMetaObject.connectSlotsByName(MatWindow)

    def retranslateUi(self, MatWindow):
        _translate = QtCore.QCoreApplication.translate
        MatWindow.setWindowTitle(_translate("MatWindow", "MainWindow"))
        self.pushButton_back.setText(_translate("MatWindow", "返回"))
        self.label.setText(_translate("MatWindow", "专辑查询"))
        self.lineEdit_Keyword.setText(_translate("MatWindow", "心理学"))
        self.label_2.setText(_translate("MatWindow", "关键词"))
        self.pushButton_getid.setText(_translate("MatWindow", "查询"))
        self.textBrowser.setHtml(_translate("MatWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">去喜马拉雅官网查找相应专辑的链接然后填写上面的空缺</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">专辑文件夹需要自己建立</span></p></body></html>"))
        self.label_3.setText(_translate("MatWindow", "专辑下载"))
        self.label_4.setText(_translate("MatWindow", "种类和ID"))
        self.lineEdit_ID.setText(_translate("MatWindow", "youshengshu/8625924"))
        self.pushButton_download.setText(_translate("MatWindow", "下载"))
        self.lineEdit_Num.setText(_translate("MatWindow", "1"))
        self.label_5.setText(_translate("MatWindow", "页码"))
        self.lineEdit_Path.setText(_translate("MatWindow", "./"))
        self.label_6.setText(_translate("MatWindow", "保存路径"))
        self.pushButton_OpenPath.setText(_translate("MatWindow", "..."))
        self.label_7.setText(_translate("MatWindow", "例如：youshengshu/8625924"))
        self.label_8.setText(_translate("MatWindow", "例如：1 每页30集 如果某专辑有35集就需要下载1、2两页"))
        self.label_9.setText(_translate("MatWindow", "例如：心理学"))
        self.label_10.setText(_translate("MatWindow", "注意：只能下载免费声音"))
        self.label_11.setText(_translate("MatWindow", "www.ximalaya.com/youshengshu/8625924/"))
        self.action_Mat.setText(_translate("MatWindow", "MatCalculate"))
        self.action_Wav.setText(_translate("MatWindow", "WavView"))

