# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ayylmbo\Desktop\Python\Python Automation Project\Resume_Builder.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MaxCharactersText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.MaxCharactersText.setGeometry(QtCore.QRect(160, 160, 61, 31))
        self.MaxCharactersText.setObjectName("MaxCharactersText")
        self.ResumePathText = QtWidgets.QTextEdit(self.centralwidget)
        self.ResumePathText.setGeometry(QtCore.QRect(160, 85, 399, 31))
        self.ResumePathText.setObjectName("ResumePathText")
        self.PdfPathBut = QtWidgets.QPushButton(self.centralwidget)
        self.PdfPathBut.setGeometry(QtCore.QRect(70, 130, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PdfPathBut.setFont(font)
        self.PdfPathBut.setObjectName("PdfPathBut")
        self.ResumePathBut = QtWidgets.QPushButton(self.centralwidget)
        self.ResumePathBut.setGeometry(QtCore.QRect(50, 90, 100, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResumePathBut.setFont(font)
        self.ResumePathBut.setObjectName("ResumePathBut")
        self.PdfPathText = QtWidgets.QTextEdit(self.centralwidget)
        self.PdfPathText.setGeometry(QtCore.QRect(160, 120, 399, 31))
        self.PdfPathText.setObjectName("PdfPathText")
        self.StartBut = QtWidgets.QPushButton(self.centralwidget)
        self.StartBut.setGeometry(QtCore.QRect(440, 280, 115, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StartBut.setFont(font)
        self.StartBut.setObjectName("StartBut")
        self.ResumeBuilderLab = QtWidgets.QLabel(self.centralwidget)
        self.ResumeBuilderLab.setGeometry(QtCore.QRect(30, 35, 109, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResumeBuilderLab.setFont(font)
        self.ResumeBuilderLab.setObjectName("ResumeBuilderLab")
        self.UrlText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.UrlText.setGeometry(QtCore.QRect(160, 200, 399, 31))
        self.UrlText.setObjectName("UrlText")
        self.UrlLab = QtWidgets.QLabel(self.centralwidget)
        self.UrlLab.setGeometry(QtCore.QRect(60, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UrlLab.setFont(font)
        self.UrlLab.setObjectName("UrlLab")
        self.MaxCharactersLab = QtWidgets.QLabel(self.centralwidget)
        self.MaxCharactersLab.setGeometry(QtCore.QRect(20, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MaxCharactersLab.setFont(font)
        self.MaxCharactersLab.setObjectName("MaxCharactersLab")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 170, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PdfPathBut.setText(_translate("MainWindow", "Pdf Path"))
        self.ResumePathBut.setText(_translate("MainWindow", "Resume Path"))
        self.StartBut.setText(_translate("MainWindow", "Start"))
        self.ResumeBuilderLab.setText(_translate("MainWindow", "Resume Builder"))
        self.UrlLab.setText(_translate("MainWindow", "URL Here"))
        self.MaxCharactersLab.setText(_translate("MainWindow", "Max Characters"))
        self.label.setText(_translate("MainWindow", "Normally 35, if you have a long name set it lower"))
