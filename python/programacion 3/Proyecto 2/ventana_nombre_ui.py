# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_nombre.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_nombre(object):
    def setupUi(self, Dialog_nombre):
        if not Dialog_nombre.objectName():
            Dialog_nombre.setObjectName(u"Dialog_nombre")
        Dialog_nombre.resize(400, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_nombre.sizePolicy().hasHeightForWidth())
        Dialog_nombre.setSizePolicy(sizePolicy)
        Dialog_nombre.setMinimumSize(QSize(400, 200))
        Dialog_nombre.setMaximumSize(QSize(400, 200))
        Dialog_nombre.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(226, 224, 239);\n"
"}\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(179, 159, 255);\n"
"}\n"
"QLineEdit {\n"
"    background: white;\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #5c5c5c;\n"
"    outline: none; /* Esto elimina el borde por defecto del sistema al enfocar */\n"
"}\n"
"")
        self.pushButton_aceptar = QPushButton(Dialog_nombre)
        self.pushButton_aceptar.setObjectName(u"pushButton_aceptar")
        self.pushButton_aceptar.setGeometry(QRect(130, 120, 111, 41))
        self.pushButton_aceptar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_aceptar.setCheckable(True)
        self.pushButton_cancel = QPushButton(Dialog_nombre)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(260, 120, 111, 41))
        self.pushButton_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_cancel.setCheckable(True)
        self.lineEdit_nombre = QLineEdit(Dialog_nombre)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")
        self.lineEdit_nombre.setGeometry(QRect(30, 70, 341, 41))
        self.lineEdit_nombre.setCursor(QCursor(Qt.ArrowCursor))
        self.label = QLabel(Dialog_nombre)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 141, 16))

        self.retranslateUi(Dialog_nombre)

        QMetaObject.connectSlotsByName(Dialog_nombre)
    # setupUi

    def retranslateUi(self, Dialog_nombre):
        Dialog_nombre.setWindowTitle(QCoreApplication.translate("Dialog_nombre", u"Dialog", None))
        self.pushButton_aceptar.setText(QCoreApplication.translate("Dialog_nombre", u"Aceptar", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog_nombre", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("Dialog_nombre", u"Escribe tu nombre", None))
    # retranslateUi

