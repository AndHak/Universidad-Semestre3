# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1191, 811)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(105, 185, 255);\n"
"}\n"
"QPushButton {\n"
"	color: white;\n"
"	height: 50px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(245, 250, 254);\n"
"	color: rgb(105, 185, 255);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setPixmap(QPixmap(u":/Images/kali.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/Images/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Images/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(20, 20))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.profile_1 = QPushButton(self.icon_only_widget)
        self.profile_1.setObjectName(u"profile_1")
        icon1 = QIcon()
        icon1.addFile(u":/Images/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/Images/profile.png", QSize(), QIcon.Normal, QIcon.On)
        self.profile_1.setIcon(icon1)
        self.profile_1.setIconSize(QSize(20, 20))
        self.profile_1.setCheckable(True)
        self.profile_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profile_1)

        self.messages_1 = QPushButton(self.icon_only_widget)
        self.messages_1.setObjectName(u"messages_1")
        icon2 = QIcon()
        icon2.addFile(u":/Images/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/Images/messages.png", QSize(), QIcon.Normal, QIcon.On)
        self.messages_1.setIcon(icon2)
        self.messages_1.setIconSize(QSize(20, 20))
        self.messages_1.setCheckable(True)
        self.messages_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.messages_1)

        self.notifications_1 = QPushButton(self.icon_only_widget)
        self.notifications_1.setObjectName(u"notifications_1")
        icon3 = QIcon()
        icon3.addFile(u":/Images/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/Images/notifications.png", QSize(), QIcon.Normal, QIcon.On)
        self.notifications_1.setIcon(icon3)
        self.notifications_1.setIconSize(QSize(20, 20))
        self.notifications_1.setCheckable(True)
        self.notifications_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.notifications_1)

        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon4 = QIcon()
        icon4.addFile(u":/Images/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/Images/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_1.setIcon(icon4)
        self.settings_1.setIconSize(QSize(20, 20))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 315, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.singout_1 = QPushButton(self.icon_only_widget)
        self.singout_1.setObjectName(u"singout_1")
        icon5 = QIcon()
        icon5.addFile(u":/Images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.singout_1.setIcon(icon5)
        self.singout_1.setIconSize(QSize(20, 20))
        self.singout_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.singout_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(105, 185, 255);\n"
"	color: white;\n"
"}\n"
"QPushButton {\n"
"	color: white;\n"
"	text-align:left;\n"
"	height: 50px;\n"
"	font-size: 15px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(245, 250, 254);\n"
"	color: rgb(105, 185, 255);\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 60))
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setPixmap(QPixmap(u":/Images/kali.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setIconSize(QSize(20, 20))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.profile_2 = QPushButton(self.icon_name_widget)
        self.profile_2.setObjectName(u"profile_2")
        self.profile_2.setIcon(icon1)
        self.profile_2.setIconSize(QSize(20, 20))
        self.profile_2.setCheckable(True)
        self.profile_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile_2)

        self.messages_2 = QPushButton(self.icon_name_widget)
        self.messages_2.setObjectName(u"messages_2")
        self.messages_2.setIcon(icon2)
        self.messages_2.setIconSize(QSize(20, 20))
        self.messages_2.setCheckable(True)
        self.messages_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.messages_2)

        self.notifications_2 = QPushButton(self.icon_name_widget)
        self.notifications_2.setObjectName(u"notifications_2")
        self.notifications_2.setIcon(icon3)
        self.notifications_2.setIconSize(QSize(20, 20))
        self.notifications_2.setCheckable(True)
        self.notifications_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.notifications_2)

        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setIcon(icon4)
        self.settings_2.setIconSize(QSize(20, 20))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 313, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.singout_2 = QPushButton(self.icon_name_widget)
        self.singout_2.setObjectName(u"singout_2")
        self.singout_2.setIcon(icon5)
        self.singout_2.setIconSize(QSize(20, 20))
        self.singout_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.singout_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu = QPushButton(self.widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border: none;")
        icon6 = QIcon()
        icon6.addFile(u":/Images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.menu)

        self.horizontalSpacer_4 = QSpacerItem(275, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon7 = QIcon()
        icon7.addFile(u":/Images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon7)

        self.horizontalLayout.addWidget(self.pushButton_11)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(275, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/Images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.pushButton_10)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Dashboard_page = QWidget()
        self.Dashboard_page.setObjectName(u"Dashboard_page")
        self.label_4 = QLabel(self.Dashboard_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 50, 211, 61))
        font1 = QFont()
        font1.setFamilies([u"Malgun Gothic"])
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.Dashboard_page)
        self.Messages_page = QWidget()
        self.Messages_page.setObjectName(u"Messages_page")
        self.label_5 = QLabel(self.Messages_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 60, 211, 61))
        self.label_5.setFont(font1)
        self.stackedWidget.addWidget(self.Messages_page)
        self.Notifications_page = QWidget()
        self.Notifications_page.setObjectName(u"Notifications_page")
        self.label_6 = QLabel(self.Notifications_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 60, 271, 61))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.Notifications_page)
        self.Settings_page = QWidget()
        self.Settings_page.setObjectName(u"Settings_page")
        self.label_8 = QLabel(self.Settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(370, 50, 211, 61))
        self.label_8.setFont(font1)
        self.stackedWidget.addWidget(self.Settings_page)
        self.Profile_page = QWidget()
        self.Profile_page.setObjectName(u"Profile_page")
        self.label_7 = QLabel(self.Profile_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(380, 30, 211, 61))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.Profile_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.notifications_1.toggled.connect(self.notifications_2.setChecked)
        self.notifications_2.toggled.connect(self.notifications_1.setChecked)
        self.messages_1.toggled.connect(self.messages_2.setChecked)
        self.messages_2.toggled.connect(self.messages_1.setChecked)
        self.profile_1.toggled.connect(self.profile_2.setChecked)
        self.profile_2.toggled.connect(self.profile_1.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.singout_2.toggled.connect(MainWindow.close)
        self.singout_1.toggled.connect(MainWindow.close)
        self.singout_2.toggled.connect(self.singout_1.setChecked)
        self.singout_1.toggled.connect(self.singout_2.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.profile_1.setText("")
        self.messages_1.setText("")
        self.notifications_1.setText("")
        self.settings_1.setText("")
        self.singout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SideBar", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.profile_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.messages_2.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.notifications_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.singout_2.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
        self.menu.setText("")
        self.pushButton_11.setText("")
        self.pushButton_10.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

