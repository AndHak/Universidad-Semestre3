# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 801, 601))
        self.frame.setStyleSheet(u"\n"
"\n"
"QFrame {\n"
"	background-color: rgb(170, 170, 127);\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 80, 101, 31))
        self.lineEdit.setStyleSheet(u"background-color: #ffffff")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 80, 81, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	font: 900 italic 9pt \"Segoe UI\";\n"
"	background-color: rgb(255, 255, 194);\n"
"}")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 30, 151, 141))
        self.label.setPixmap(QPixmap(u"../../images/yo.jpeg"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lcdNumber = QLCDNumber(self.frame_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(330, 2, 411, 181))
        self.lcdNumber.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.radioButton = QRadioButton(self.frame_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(60, 90, 89, 20))
        self.radioButton.setStyleSheet(u"font: 900 italic 9pt \"Segoe UI\";")
        self.radioButton_2 = QRadioButton(self.frame_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(240, 90, 51, 20))
        self.radioButton_2.setStyleSheet(u"font: 900 italic 9pt \"Segoe UI\";")
        self.radioButton_3 = QRadioButton(self.frame_4)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(400, 90, 61, 20))
        self.radioButton_3.setStyleSheet(u"font: 900 italic 9pt \"Segoe UI\";")
        self.radioButton_4 = QRadioButton(self.frame_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(570, 90, 89, 20))
        self.radioButton_4.setStyleSheet(u"font: 900 italic 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.frame_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.label.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"decimal", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"octal", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"binario", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"hexagecimal", None))
    # retranslateUi

