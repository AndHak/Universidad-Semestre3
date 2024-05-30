# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_viajes_final.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import recursos_1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1491, 890)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menus = QWidget(self.centralwidget)
        self.menus.setObjectName(u"menus")
        self.menus.setMinimumSize(QSize(80, 0))
        self.menus.setMaximumSize(QSize(80, 16777215))
        self.menus.setStyleSheet(u"QWidget {\n"
"	background-color: #1B4965;\n"
"}\n"
"QPushButton:checked {\n"
"	color: #1B4965;\n"
"	background-color: #CAE9FF;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"	color: #CAE9FF;\n"
"	padding-left: 10px;\n"
"	text-align: letf;\n"
"	font-size: 15px;\n"
"	padding: 10px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.menus)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 9, 9)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_pic_small1 = QLabel(self.menus)
        self.label_pic_small1.setObjectName(u"label_pic_small1")
        self.label_pic_small1.setMinimumSize(QSize(50, 50))
        self.label_pic_small1.setMaximumSize(QSize(50, 50))
        self.label_pic_small1.setPixmap(QPixmap(u":/Icons/icons/sinfoto.png"))
        self.label_pic_small1.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_pic_small1, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 95, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.home_small_button1 = QPushButton(self.menus)
        self.home_small_button1.setObjectName(u"home_small_button1")
        self.home_small_button1.setMinimumSize(QSize(50, 50))
        self.home_small_button1.setMaximumSize(QSize(50, 50))
        self.home_small_button1.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/icons8-dashboard-48.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Icons/icons/icons8-dashboard-layout-48_2.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_small_button1.setIcon(icon)
        self.home_small_button1.setIconSize(QSize(40, 40))
        self.home_small_button1.setCheckable(True)
        self.home_small_button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_small_button1, 0, Qt.AlignHCenter)

        self.mytravels_small_button1 = QPushButton(self.menus)
        self.mytravels_small_button1.setObjectName(u"mytravels_small_button1")
        self.mytravels_small_button1.setMinimumSize(QSize(50, 50))
        self.mytravels_small_button1.setMaximumSize(QSize(50, 50))
        self.mytravels_small_button1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/icons8-airplane-take-off-26.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/Icons/icons/icons8-airplane-take-off-50_2.png", QSize(), QIcon.Normal, QIcon.On)
        self.mytravels_small_button1.setIcon(icon1)
        self.mytravels_small_button1.setIconSize(QSize(40, 40))
        self.mytravels_small_button1.setCheckable(True)
        self.mytravels_small_button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.mytravels_small_button1, 0, Qt.AlignHCenter)

        self.newtravel_small_button1 = QPushButton(self.menus)
        self.newtravel_small_button1.setObjectName(u"newtravel_small_button1")
        self.newtravel_small_button1.setMinimumSize(QSize(50, 50))
        self.newtravel_small_button1.setMaximumSize(QSize(50, 50))
        self.newtravel_small_button1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/icons8-plus-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/Icons/icons/icons8-plus-math-50_2.png", QSize(), QIcon.Normal, QIcon.On)
        self.newtravel_small_button1.setIcon(icon2)
        self.newtravel_small_button1.setIconSize(QSize(40, 40))
        self.newtravel_small_button1.setCheckable(True)
        self.newtravel_small_button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.newtravel_small_button1, 0, Qt.AlignHCenter)

        self.itinerary_small_button1 = QPushButton(self.menus)
        self.itinerary_small_button1.setObjectName(u"itinerary_small_button1")
        self.itinerary_small_button1.setMinimumSize(QSize(50, 50))
        self.itinerary_small_button1.setMaximumSize(QSize(50, 50))
        self.itinerary_small_button1.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icons/icons8-calendar-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/Icons/icons/icons8-calendar-50_2.png", QSize(), QIcon.Normal, QIcon.On)
        self.itinerary_small_button1.setIcon(icon3)
        self.itinerary_small_button1.setIconSize(QSize(40, 40))
        self.itinerary_small_button1.setCheckable(True)
        self.itinerary_small_button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.itinerary_small_button1, 0, Qt.AlignHCenter)

        self.bills_small_button1 = QPushButton(self.menus)
        self.bills_small_button1.setObjectName(u"bills_small_button1")
        self.bills_small_button1.setMinimumSize(QSize(50, 50))
        self.bills_small_button1.setMaximumSize(QSize(50, 50))
        self.bills_small_button1.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons/icons8-coin-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/Icons/icons/icons8-coin-in-hand-50_2.png", QSize(), QIcon.Normal, QIcon.On)
        self.bills_small_button1.setIcon(icon4)
        self.bills_small_button1.setIconSize(QSize(40, 40))
        self.bills_small_button1.setCheckable(True)
        self.bills_small_button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bills_small_button1, 0, Qt.AlignHCenter)

        self.notify_small_button1 = QPushButton(self.menus)
        self.notify_small_button1.setObjectName(u"notify_small_button1")
        self.notify_small_button1.setMinimumSize(QSize(50, 50))
        self.notify_small_button1.setMaximumSize(QSize(50, 50))
        self.notify_small_button1.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/icons/icons8-notification-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/Icons/icons/icons8-notification-50_2.png", QSize(), QIcon.Normal, QIcon.On)
        self.notify_small_button1.setIcon(icon5)
        self.notify_small_button1.setIconSize(QSize(40, 40))
        self.notify_small_button1.setCheckable(True)
        self.notify_small_button1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.notify_small_button1, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 95, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settings_small_button1 = QPushButton(self.menus)
        self.settings_small_button1.setObjectName(u"settings_small_button1")
        self.settings_small_button1.setMinimumSize(QSize(50, 50))
        self.settings_small_button1.setMaximumSize(QSize(50, 50))
        self.settings_small_button1.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/icons/icons8-settings-48.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/Icons/icons/icons8-settings-48_2.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_small_button1.setIcon(icon6)
        self.settings_small_button1.setIconSize(QSize(40, 40))
        self.settings_small_button1.setCheckable(True)
        self.settings_small_button1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_small_button1, 0, Qt.AlignHCenter)

        self.off1button = QPushButton(self.menus)
        self.off1button.setObjectName(u"off1button")
        self.off1button.setMinimumSize(QSize(50, 50))
        self.off1button.setMaximumSize(QSize(50, 50))
        self.off1button.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/icons/icons8-shutdown-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.off1button.setIcon(icon7)
        self.off1button.setIconSize(QSize(40, 40))
        self.off1button.setCheckable(True)
        self.off1button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.off1button, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addWidget(self.menus)

        self.menub = QWidget(self.centralwidget)
        self.menub.setObjectName(u"menub")
        self.menub.setMinimumSize(QSize(250, 50))
        self.menub.setMaximumSize(QSize(250, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(27, 73, 101, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.menub.setPalette(palette)
        font = QFont()
        font.setKerning(True)
        self.menub.setFont(font)
        self.menub.setStyleSheet(u"QWidget {\n"
"	background-color: #1B4965;\n"
"}\n"
"QLabel {\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: #1B4965;\n"
"	background-color: #CAE9FF;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"	color: #CAE9FF;\n"
"	padding-left: 10px;\n"
"	text-align: letf;\n"
"	font-size: 15px;\n"
"	padding: 10px;\n"
"	width: 250px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.menub)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_pic_small2 = QLabel(self.menub)
        self.label_pic_small2.setObjectName(u"label_pic_small2")
        self.label_pic_small2.setMinimumSize(QSize(50, 50))
        self.label_pic_small2.setMaximumSize(QSize(50, 50))
        self.label_pic_small2.setPixmap(QPixmap(u":/Icons/icons/sinfoto.png"))
        self.label_pic_small2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_pic_small2)

        self.label_4 = QLabel(self.menub)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"	border: none;\n"
"	color: #CAE9FF;\n"
"	padding-left: 10px;\n"
"	text-align: letf;")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 47, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.home_small_button2 = QPushButton(self.menub)
        self.home_small_button2.setObjectName(u"home_small_button2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_small_button2.sizePolicy().hasHeightForWidth())
        self.home_small_button2.setSizePolicy(sizePolicy)
        self.home_small_button2.setMinimumSize(QSize(150, 50))
        self.home_small_button2.setMaximumSize(QSize(180, 50))
        self.home_small_button2.setFont(font)
        self.home_small_button2.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_small_button2.setStyleSheet(u"text-align: left;\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"")
        self.home_small_button2.setIcon(icon)
        self.home_small_button2.setIconSize(QSize(40, 40))
        self.home_small_button2.setCheckable(True)
        self.home_small_button2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.home_small_button2)

        self.mytravels_small_button2 = QPushButton(self.menub)
        self.mytravels_small_button2.setObjectName(u"mytravels_small_button2")
        sizePolicy.setHeightForWidth(self.mytravels_small_button2.sizePolicy().hasHeightForWidth())
        self.mytravels_small_button2.setSizePolicy(sizePolicy)
        self.mytravels_small_button2.setMinimumSize(QSize(150, 50))
        self.mytravels_small_button2.setMaximumSize(QSize(180, 50))
        self.mytravels_small_button2.setCursor(QCursor(Qt.PointingHandCursor))
        self.mytravels_small_button2.setStyleSheet(u"text-align: left;\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"")
        self.mytravels_small_button2.setIcon(icon1)
        self.mytravels_small_button2.setIconSize(QSize(40, 40))
        self.mytravels_small_button2.setCheckable(True)
        self.mytravels_small_button2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.mytravels_small_button2)

        self.newtravel_small_button2 = QPushButton(self.menub)
        self.newtravel_small_button2.setObjectName(u"newtravel_small_button2")
        sizePolicy.setHeightForWidth(self.newtravel_small_button2.sizePolicy().hasHeightForWidth())
        self.newtravel_small_button2.setSizePolicy(sizePolicy)
        self.newtravel_small_button2.setMinimumSize(QSize(150, 50))
        self.newtravel_small_button2.setMaximumSize(QSize(180, 50))
        self.newtravel_small_button2.setCursor(QCursor(Qt.PointingHandCursor))
        self.newtravel_small_button2.setStyleSheet(u"text-align: left;\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"")
        self.newtravel_small_button2.setIcon(icon2)
        self.newtravel_small_button2.setIconSize(QSize(40, 40))
        self.newtravel_small_button2.setCheckable(True)
        self.newtravel_small_button2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.newtravel_small_button2)

        self.itinerary_small_button2 = QPushButton(self.menub)
        self.itinerary_small_button2.setObjectName(u"itinerary_small_button2")
        sizePolicy.setHeightForWidth(self.itinerary_small_button2.sizePolicy().hasHeightForWidth())
        self.itinerary_small_button2.setSizePolicy(sizePolicy)
        self.itinerary_small_button2.setMinimumSize(QSize(150, 50))
        self.itinerary_small_button2.setMaximumSize(QSize(180, 50))
        self.itinerary_small_button2.setCursor(QCursor(Qt.PointingHandCursor))
        self.itinerary_small_button2.setStyleSheet(u"text-align: left;\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"")
        self.itinerary_small_button2.setIcon(icon3)
        self.itinerary_small_button2.setIconSize(QSize(40, 40))
        self.itinerary_small_button2.setCheckable(True)
        self.itinerary_small_button2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.itinerary_small_button2)

        self.bills_small_button2 = QPushButton(self.menub)
        self.bills_small_button2.setObjectName(u"bills_small_button2")
        sizePolicy.setHeightForWidth(self.bills_small_button2.sizePolicy().hasHeightForWidth())
        self.bills_small_button2.setSizePolicy(sizePolicy)
        self.bills_small_button2.setMinimumSize(QSize(150, 50))
        self.bills_small_button2.setMaximumSize(QSize(180, 50))
        self.bills_small_button2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bills_small_button2.setStyleSheet(u"text-align: left;\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"")
        self.bills_small_button2.setIcon(icon4)
        self.bills_small_button2.setIconSize(QSize(40, 40))
        self.bills_small_button2.setCheckable(True)
        self.bills_small_button2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.bills_small_button2)

        self.notify_small_button2 = QPushButton(self.menub)
        self.notify_small_button2.setObjectName(u"notify_small_button2")
        sizePolicy.setHeightForWidth(self.notify_small_button2.sizePolicy().hasHeightForWidth())
        self.notify_small_button2.setSizePolicy(sizePolicy)
        self.notify_small_button2.setMinimumSize(QSize(160, 50))
        self.notify_small_button2.setMaximumSize(QSize(180, 50))
        self.notify_small_button2.setCursor(QCursor(Qt.PointingHandCursor))
        self.notify_small_button2.setStyleSheet(u"text-align: left;\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"")
        self.notify_small_button2.setIcon(icon5)
        self.notify_small_button2.setIconSize(QSize(40, 40))
        self.notify_small_button2.setCheckable(True)
        self.notify_small_button2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.notify_small_button2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 95, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.settings_small_button2 = QPushButton(self.menub)
        self.settings_small_button2.setObjectName(u"settings_small_button2")
        sizePolicy.setHeightForWidth(self.settings_small_button2.sizePolicy().hasHeightForWidth())
        self.settings_small_button2.setSizePolicy(sizePolicy)
        self.settings_small_button2.setMinimumSize(QSize(150, 50))
        self.settings_small_button2.setMaximumSize(QSize(180, 50))
        self.settings_small_button2.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_small_button2.setStyleSheet(u"text-align: left;\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"")
        self.settings_small_button2.setIcon(icon6)
        self.settings_small_button2.setIconSize(QSize(40, 40))
        self.settings_small_button2.setCheckable(True)
        self.settings_small_button2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.settings_small_button2)

        self.off2button = QPushButton(self.menub)
        self.off2button.setObjectName(u"off2button")
        sizePolicy.setHeightForWidth(self.off2button.sizePolicy().hasHeightForWidth())
        self.off2button.setSizePolicy(sizePolicy)
        self.off2button.setMinimumSize(QSize(150, 50))
        self.off2button.setMaximumSize(QSize(180, 50))
        self.off2button.setCursor(QCursor(Qt.PointingHandCursor))
        self.off2button.setStyleSheet(u"text-align: left;\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"")
        self.off2button.setIcon(icon7)
        self.off2button.setIconSize(QSize(40, 40))
        self.off2button.setCheckable(True)
        self.off2button.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.off2button)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_3.addWidget(self.menub)

        self.pages = QWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.gridLayout_3 = QGridLayout(self.pages)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_4 = QWidget(self.pages)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 60))
        self.widget_4.setMaximumSize(QSize(16777215, 60))
        self.widget_4.setStyleSheet(u"background-color: white;\n"
"")
        self.gridLayout_9 = QGridLayout(self.widget_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.menu_button = QPushButton(self.widget_4)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setMinimumSize(QSize(40, 40))
        self.menu_button.setMaximumSize(QSize(40, 40))
        self.menu_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_button.setStyleSheet(u"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/icons/icons8-lines-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon8)
        self.menu_button.setIconSize(QSize(30, 30))
        self.menu_button.setCheckable(True)
        self.menu_button.setChecked(False)

        self.gridLayout_9.addWidget(self.menu_button, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Horas = QLCDNumber(self.widget_4)
        self.Horas.setObjectName(u"Horas")
        self.Horas.setMinimumSize(QSize(40, 40))
        self.Horas.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setPointSize(20)
        self.Horas.setFont(font1)
        self.Horas.setStyleSheet(u"border: none;")
        self.Horas.setProperty("intValue", 12)

        self.horizontalLayout_2.addWidget(self.Horas, 0, Qt.AlignVCenter)

        self.label_38 = QLabel(self.widget_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font-size: 25px;\n"
"font-style: italic;\n"
"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label_38, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.minutos = QLCDNumber(self.widget_4)
        self.minutos.setObjectName(u"minutos")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minutos.sizePolicy().hasHeightForWidth())
        self.minutos.setSizePolicy(sizePolicy1)
        self.minutos.setMinimumSize(QSize(40, 40))
        self.minutos.setMaximumSize(QSize(40, 40))
        self.minutos.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.minutos.setFont(font2)
        self.minutos.setStyleSheet(u"border: none;\n"
"text-align: left;")
        self.minutos.setProperty("intValue", 25)

        self.horizontalLayout_2.addWidget(self.minutos, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.gridLayout_9.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(482, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(482, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.myprofile_button = QPushButton(self.widget_4)
        self.myprofile_button.setObjectName(u"myprofile_button")
        self.myprofile_button.setMinimumSize(QSize(40, 40))
        self.myprofile_button.setMaximumSize(QSize(40, 40))
        self.myprofile_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.myprofile_button.setStyleSheet(u"border: none;")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/icons/icons8-user-50 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.myprofile_button.setIcon(icon9)
        self.myprofile_button.setIconSize(QSize(30, 30))
        self.myprofile_button.setCheckable(True)

        self.gridLayout_9.addWidget(self.myprofile_button, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.stackedWidget = QStackedWidget(self.pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QFrame {\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"QCheckBox {\n"
"    font-size: 14px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color del borde cuando el checkbox est\u00e1 sin marcar y el rat\u00f3n est\u00e1 sobre \u00e9l */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color de fondo cuando est\u00e1 marcado */\n"
"    border: 2px solid #1B4965; /* Color del borde cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.gridLayout_11 = QGridLayout(self.home_page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_10 = QFrame(self.home_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_10)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 20px;")

        self.horizontalLayout_16.addWidget(self.label_8)

        self.horizontalSpacer_19 = QSpacerItem(588, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)

        self.money_combobox_apoyo_2 = QComboBox(self.frame_10)
        self.money_combobox_apoyo_2.addItem("")
        self.money_combobox_apoyo_2.addItem("")
        self.money_combobox_apoyo_2.addItem("")
        self.money_combobox_apoyo_2.setObjectName(u"money_combobox_apoyo_2")
        self.money_combobox_apoyo_2.setMinimumSize(QSize(100, 40))
        self.money_combobox_apoyo_2.setMaximumSize(QSize(100, 40))
        self.money_combobox_apoyo_2.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.money_combobox_apoyo_2)


        self.gridLayout_42.addLayout(self.horizontalLayout_16, 0, 0, 1, 2)

        self.widget = QWidget(self.frame_10)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setStyleSheet(u"QWidget {\n"
"    background-color: #BEE9E8;\n"
"    font-family: sans-serif;\n"
"    color: #CAE9FF;\n"
"    border-radius: 25px;\n"
"    padding: 25px;\n"
"}\n"
"QLabel {\n"
"	color: rgb(27, 73, 101);\n"
"	background: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_40 = QGridLayout(self.widget)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setVerticalSpacing(0)
        self.gridLayout_40.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 25))
        self.label_22.setMaximumSize(QSize(16777215, 25))
        font3 = QFont()
        font3.setFamilies([u"sans-serif"])
        font3.setBold(True)
        self.label_22.setFont(font3)

        self.verticalLayout_19.addWidget(self.label_22)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(400, 250))
        self.label_6.setMaximumSize(QSize(400, 250))
        self.label_6.setFocusPolicy(Qt.WheelFocus)
        self.label_6.setStyleSheet(u"border: none;\n"
"background: transparent;")
        self.label_6.setPixmap(QPixmap(u":/Icons/icons/cartagena.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(False)

        self.verticalLayout_19.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.gridLayout_40.addLayout(self.verticalLayout_19, 0, 0, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 25))
        self.label_26.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_25.addWidget(self.label_26)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(350, 300))
        self.label_28.setPixmap(QPixmap(u":/Icons/icons/hotel_almirante.jpg"))
        self.label_28.setScaledContents(True)

        self.verticalLayout_25.addWidget(self.label_28, 0, Qt.AlignHCenter)


        self.gridLayout_40.addLayout(self.verticalLayout_25, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 25))
        self.label_29.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_6.addWidget(self.label_29)

        self.label_39 = QLabel(self.widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 25))
        self.label_39.setMaximumSize(QSize(16777215, 25))
        self.label_39.setStyleSheet(u"color: green;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_39)


        self.gridLayout_40.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)


        self.gridLayout_42.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.frame_10)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setStyleSheet(u"QWidget {\n"
"    background-color: #BEE9E8;\n"
"    font-family: sans-serif;\n"
"    color: #CAE9FF;\n"
"    border-radius: 25px;\n"
"    padding: 20px;\n"
"}\n"
"QLabel {\n"
"	color: rgb(27, 73, 101);\n"
"	background: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_41 = QGridLayout(self.widget_2)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setVerticalSpacing(0)
        self.gridLayout_41.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 25))
        self.label_23.setMaximumSize(QSize(16777215, 25))
        self.label_23.setFont(font3)

        self.verticalLayout_37.addWidget(self.label_23)

        self.label_31 = QLabel(self.widget_2)
        self.label_31.setObjectName(u"label_31")
        sizePolicy3.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy3)
        self.label_31.setMinimumSize(QSize(400, 250))
        self.label_31.setMaximumSize(QSize(400, 250))
        self.label_31.setFocusPolicy(Qt.WheelFocus)
        self.label_31.setStyleSheet(u"border: none;\n"
"background: transparent;")
        self.label_31.setPixmap(QPixmap(u":/Icons/icons/sanandres.jpg"))
        self.label_31.setScaledContents(True)
        self.label_31.setWordWrap(False)

        self.verticalLayout_37.addWidget(self.label_31, 0, Qt.AlignHCenter)


        self.gridLayout_41.addLayout(self.verticalLayout_37, 0, 0, 1, 1)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_32 = QLabel(self.widget_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 25))
        self.label_32.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_38.addWidget(self.label_32)

        self.label_40 = QLabel(self.widget_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(350, 300))
        self.label_40.setPixmap(QPixmap(u":/Icons/icons/hotel_sea.jpg"))
        self.label_40.setScaledContents(True)

        self.verticalLayout_38.addWidget(self.label_40, 0, Qt.AlignHCenter)


        self.gridLayout_41.addLayout(self.verticalLayout_38, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_41 = QLabel(self.widget_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 25))
        self.label_41.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_15.addWidget(self.label_41)

        self.label_42 = QLabel(self.widget_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 25))
        self.label_42.setMaximumSize(QSize(120, 25))
        self.label_42.setStyleSheet(u"color: green;\n"
"")

        self.horizontalLayout_15.addWidget(self.label_42)


        self.gridLayout_41.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)


        self.gridLayout_42.addWidget(self.widget_2, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.frame_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.mis_viajes_page = QWidget()
        self.mis_viajes_page.setObjectName(u"mis_viajes_page")
        self.mis_viajes_page.setStyleSheet(u"QCheckBox {\n"
"    font-size: 14px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color del borde cuando el checkbox est\u00e1 sin marcar y el rat\u00f3n est\u00e1 sobre \u00e9l */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color de fondo cuando est\u00e1 marcado */\n"
"    border: 2px solid #1B4965; /* Color del borde cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"")
        self.gridLayout_12 = QGridLayout(self.mis_viajes_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_mis_viajes = QFrame(self.mis_viajes_page)
        self.frame_mis_viajes.setObjectName(u"frame_mis_viajes")
        self.frame_mis_viajes.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"    font-family: 'Roboto', sans-serif;\n"
"    color: #212121; \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"	padding: 0 8px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */"
                        "\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B49"
                        "65; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: white;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: "
                        "italic;\n"
"}\n"
"\n"
"/* Estilo para QProgressBar */\n"
"QProgressBar {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font-size: 15px;\n"
"    color: #212121; /* Color del texto */\n"
"    background-color: #FAFAFA; /* Color de fondo */\n"
"    height: 10px; /* Alto m\u00e1s peque\u00f1o */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border-radius: 5px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* Estilo para QDateEdit */\n"
"QDateEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left"
                        "-style: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Estilo para QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left-style: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTimeEdit::down-arrow {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Estilo para QCheckBox */\n"
"QCheckBox {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"    color: #1B4965;\n"
"}\n"
""
                        "\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"")
        self.frame_mis_viajes.setFrameShape(QFrame.StyledPanel)
        self.frame_mis_viajes.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_mis_viajes)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setVerticalSpacing(6)
        self.gridLayout_44.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setVerticalSpacing(30)
        self.label_9 = QLabel(self.frame_mis_viajes)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 20px;")

        self.gridLayout_43.addWidget(self.label_9, 0, 0, 1, 1)

        self.list_widget_viajes_guardados = QListWidget(self.frame_mis_viajes)
        self.list_widget_viajes_guardados.setObjectName(u"list_widget_viajes_guardados")
        self.list_widget_viajes_guardados.setStyleSheet(u"QListWidget {\n"
"    font-size: 15px; /* Aumenta el tama\u00f1o de la fuente para los elementos */\n"
"    padding: 5px; /* A\u00f1ade un padding alrededor del contenido del QListWidget */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px; /* A\u00f1ade padding a cada elemento para aumentar el espacio entre ellos */\n"
"    margin: 5px 0; /* A\u00f1ade un margen entre cada elemento para mayor separaci\u00f3n vertical*/\n"
"	width: 200px:\n"
"	height: 25px;\n"
"}\n"
"")
        self.list_widget_viajes_guardados.setWordWrap(False)

        self.gridLayout_43.addWidget(self.list_widget_viajes_guardados, 1, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_20 = QSpacerItem(738, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_20)

        self.ver_viaje_guardado_button = QPushButton(self.frame_mis_viajes)
        self.ver_viaje_guardado_button.setObjectName(u"ver_viaje_guardado_button")
        self.ver_viaje_guardado_button.setMinimumSize(QSize(60, 60))
        self.ver_viaje_guardado_button.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"border: none;\n"
"background-color: #CAE9FF;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/icons/icons8-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ver_viaje_guardado_button.setIcon(icon10)
        self.ver_viaje_guardado_button.setIconSize(QSize(35, 35))
        self.ver_viaje_guardado_button.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.ver_viaje_guardado_button)

        self.eliminar_viajeguardado_button = QPushButton(self.frame_mis_viajes)
        self.eliminar_viajeguardado_button.setObjectName(u"eliminar_viajeguardado_button")
        self.eliminar_viajeguardado_button.setMinimumSize(QSize(60, 60))
        self.eliminar_viajeguardado_button.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"border: none;\n"
"background-color: #CAE9FF;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/icons/icons8-trash-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminar_viajeguardado_button.setIcon(icon11)
        self.eliminar_viajeguardado_button.setIconSize(QSize(35, 35))
        self.eliminar_viajeguardado_button.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.eliminar_viajeguardado_button)


        self.gridLayout_43.addLayout(self.horizontalLayout_29, 2, 0, 1, 1)


        self.gridLayout_44.addLayout(self.gridLayout_43, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_mis_viajes, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.mis_viajes_page)
        self.nuevo_viaje_page = QWidget()
        self.nuevo_viaje_page.setObjectName(u"nuevo_viaje_page")
        self.gridLayout_17 = QGridLayout(self.nuevo_viaje_page)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_12 = QFrame(self.nuevo_viaje_page)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy4)
        self.frame_12.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"    font-family: 'Roboto', sans-serif;\n"
"    color: #212121; \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"	padding: 0 8px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px s"
                        "olid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
""
                        "    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: white;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"/* Estilo para QProgressBar */\n"
"QProgressBar {\n"
"    border: 2"
                        "px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font-size: 15px;\n"
"    color: #212121; /* Color del texto */\n"
"    background-color: #FAFAFA; /* Color de fondo */\n"
"    height: 10px; /* Alto m\u00e1s peque\u00f1o */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border-radius: 5px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* Estilo para QDateEdit */\n"
"QDateEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left-style: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3p"
                        "x;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Estilo para QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left-style: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTimeEdit::down-arrow {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Estilo para QCheckBox */\n"
"QCheckBox {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"    color: #1B4965;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border: 2p"
                        "x solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"/* Estilo desactivado para QLineEdit */\n"
"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9; /* Color de texto desactivado */\n"
"}\n"
"\n"
"/* Estilo desactivado para QGroupBox */\n"
"QGroupBox:disabled {\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"}\n"
"\n"
"/* Estilo desactivado para QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9;"
                        " /* Color de texto desactivado */\n"
"}\n"
"\n"
"/* Estilo desactivado para QPlainTextEdit */\n"
"QPlainTextEdit:disabled {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9; /* Color de texto desactivado */\n"
"}\n"
"/* Estilo desactivado para QLabel */\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Color de texto desactivado */\n"
"	color: #A9A9A9;\n"
"}\n"
"QGroupBox::title:disabled {\n"
"    background-color: #F0F0F0; /* Color de texto desactivado */\n"
"	color: #A9A9A9;\n"
"	border-radius: 5px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_12)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setHorizontalSpacing(15)
        self.gridLayout_26.setVerticalSpacing(30)
        self.gridLayout_26.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.frame_12)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1198, 1226))
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.scrollAreaWidgetContents.setStyleSheet(u"QCheckBox {\n"
"    font-size: 14px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color del borde cuando el checkbox est\u00e1 sin marcar y el rat\u00f3n est\u00e1 sobre \u00e9l */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color de fondo cuando est\u00e1 marcado */\n"
"    border: 2px solid #1B4965; /* Color del borde cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"")
        self.gridLayout_34 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setHorizontalSpacing(30)
        self.gridLayout_34.setVerticalSpacing(25)
        self.gridLayout_34.setContentsMargins(50, 50, 50, 50)
        self.label_36 = QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 20px;")

        self.gridLayout_34.addWidget(self.label_36, 0, 0, 1, 1)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(100, 20))
        self.label_33.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout_30.addWidget(self.label_33)

        self.lineedit_titulo_nuevo_viaje = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_titulo_nuevo_viaje.setObjectName(u"lineedit_titulo_nuevo_viaje")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineedit_titulo_nuevo_viaje.sizePolicy().hasHeightForWidth())
        self.lineedit_titulo_nuevo_viaje.setSizePolicy(sizePolicy5)
        self.lineedit_titulo_nuevo_viaje.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        self.lineedit_titulo_nuevo_viaje.setFont(font4)

        self.verticalLayout_30.addWidget(self.lineedit_titulo_nuevo_viaje)


        self.gridLayout_34.addLayout(self.verticalLayout_30, 1, 0, 1, 1)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_35 = QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(100, 20))
        self.label_35.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout_31.addWidget(self.label_35)

        self.lineedit_destino_nuevo_viaje = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_destino_nuevo_viaje.setObjectName(u"lineedit_destino_nuevo_viaje")
        sizePolicy5.setHeightForWidth(self.lineedit_destino_nuevo_viaje.sizePolicy().hasHeightForWidth())
        self.lineedit_destino_nuevo_viaje.setSizePolicy(sizePolicy5)
        self.lineedit_destino_nuevo_viaje.setMinimumSize(QSize(0, 40))

        self.verticalLayout_31.addWidget(self.lineedit_destino_nuevo_viaje)


        self.gridLayout_34.addLayout(self.verticalLayout_31, 1, 1, 1, 1)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_37 = QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(100, 20))
        self.label_37.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout_32.addWidget(self.label_37)

        self.lineedit_fechainicio_nuevo_viaje = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_fechainicio_nuevo_viaje.setObjectName(u"lineedit_fechainicio_nuevo_viaje")
        sizePolicy5.setHeightForWidth(self.lineedit_fechainicio_nuevo_viaje.sizePolicy().hasHeightForWidth())
        self.lineedit_fechainicio_nuevo_viaje.setSizePolicy(sizePolicy5)
        self.lineedit_fechainicio_nuevo_viaje.setMinimumSize(QSize(0, 40))

        self.verticalLayout_32.addWidget(self.lineedit_fechainicio_nuevo_viaje)


        self.gridLayout_34.addLayout(self.verticalLayout_32, 1, 2, 1, 1)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_34 = QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(100, 20))
        self.label_34.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout_33.addWidget(self.label_34)

        self.lineedit_fechafin_nuevo_viaje = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_fechafin_nuevo_viaje.setObjectName(u"lineedit_fechafin_nuevo_viaje")
        sizePolicy5.setHeightForWidth(self.lineedit_fechafin_nuevo_viaje.sizePolicy().hasHeightForWidth())
        self.lineedit_fechafin_nuevo_viaje.setSizePolicy(sizePolicy5)
        self.lineedit_fechafin_nuevo_viaje.setMinimumSize(QSize(0, 40))

        self.verticalLayout_33.addWidget(self.lineedit_fechafin_nuevo_viaje)


        self.gridLayout_34.addLayout(self.verticalLayout_33, 1, 3, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(40)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_33.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineedit_presupuesto_nuevo_viaje = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_presupuesto_nuevo_viaje.setObjectName(u"lineedit_presupuesto_nuevo_viaje")

        self.gridLayout_33.addWidget(self.lineedit_presupuesto_nuevo_viaje, 1, 0, 1, 1)


        self.horizontalLayout_22.addLayout(self.gridLayout_33)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setHorizontalSpacing(0)
        self.line_edit_familia_nuevo_viaje = QLineEdit(self.scrollAreaWidgetContents)
        self.line_edit_familia_nuevo_viaje.setObjectName(u"line_edit_familia_nuevo_viaje")
        self.line_edit_familia_nuevo_viaje.setEnabled(False)
        self.line_edit_familia_nuevo_viaje.setStyleSheet(u"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9; /* Color de texto desactivado */\n"
"}")

        self.gridLayout_29.addWidget(self.line_edit_familia_nuevo_viaje, 1, 6, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_29.addWidget(self.label_14, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_11, 1, 1, 1, 1)

        self.boton_pareja_nuevo_viaje = QPushButton(self.scrollAreaWidgetContents)
        self.boton_pareja_nuevo_viaje.setObjectName(u"boton_pareja_nuevo_viaje")
        self.boton_pareja_nuevo_viaje.setMinimumSize(QSize(60, 60))
        self.boton_pareja_nuevo_viaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_pareja_nuevo_viaje.setStyleSheet(u"QPushButton {\n"
"	border-radius: 30px;\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(95, 168, 211);\n"
"	border: none;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/icons/icons8-couple-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_pareja_nuevo_viaje.setIcon(icon12)
        self.boton_pareja_nuevo_viaje.setIconSize(QSize(40, 40))
        self.boton_pareja_nuevo_viaje.setCheckable(True)
        self.boton_pareja_nuevo_viaje.setAutoExclusive(True)

        self.gridLayout_29.addWidget(self.boton_pareja_nuevo_viaje, 1, 2, 1, 1)

        self.boton_familia_nuevo_viaje = QPushButton(self.scrollAreaWidgetContents)
        self.boton_familia_nuevo_viaje.setObjectName(u"boton_familia_nuevo_viaje")
        self.boton_familia_nuevo_viaje.setMinimumSize(QSize(60, 60))
        self.boton_familia_nuevo_viaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_familia_nuevo_viaje.setStyleSheet(u"QPushButton {\n"
"	border-radius: 30px;\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(95, 168, 211);\n"
"	border: none;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/icons/icons8-family-40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_familia_nuevo_viaje.setIcon(icon13)
        self.boton_familia_nuevo_viaje.setIconSize(QSize(40, 40))
        self.boton_familia_nuevo_viaje.setCheckable(True)
        self.boton_familia_nuevo_viaje.setAutoExclusive(True)

        self.gridLayout_29.addWidget(self.boton_familia_nuevo_viaje, 1, 4, 1, 1)

        self.boton_solo_nuevo_viaje = QPushButton(self.scrollAreaWidgetContents)
        self.boton_solo_nuevo_viaje.setObjectName(u"boton_solo_nuevo_viaje")
        self.boton_solo_nuevo_viaje.setMinimumSize(QSize(60, 60))
        self.boton_solo_nuevo_viaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_solo_nuevo_viaje.setStyleSheet(u"QPushButton {\n"
"	border-radius: 30px;\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(95, 168, 211);\n"
"	border: none;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/icons/icons8-me-58.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_solo_nuevo_viaje.setIcon(icon14)
        self.boton_solo_nuevo_viaje.setIconSize(QSize(40, 40))
        self.boton_solo_nuevo_viaje.setCheckable(True)
        self.boton_solo_nuevo_viaje.setChecked(True)
        self.boton_solo_nuevo_viaje.setAutoExclusive(True)

        self.gridLayout_29.addWidget(self.boton_solo_nuevo_viaje, 1, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_13, 1, 7, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_12, 1, 3, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_15, 1, 5, 1, 1)


        self.horizontalLayout_22.addLayout(self.gridLayout_29)


        self.gridLayout_34.addLayout(self.horizontalLayout_22, 2, 0, 1, 4)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(40)
        self.checkbox_vuelos_nuevo_viaje = QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_vuelos_nuevo_viaje.setObjectName(u"checkbox_vuelos_nuevo_viaje")

        self.gridLayout_25.addWidget(self.checkbox_vuelos_nuevo_viaje, 0, 0, 1, 1)

        self.grupo_ida_viaje = QGroupBox(self.scrollAreaWidgetContents)
        self.grupo_ida_viaje.setObjectName(u"grupo_ida_viaje")
        self.grupo_ida_viaje.setEnabled(False)
        self.grupo_ida_viaje.setStyleSheet(u"")
        self.gridLayout_28 = QGridLayout(self.grupo_ida_viaje)
        self.gridLayout_28.setSpacing(15)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_54 = QLabel(self.grupo_ida_viaje)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_28.addWidget(self.label_54, 0, 0, 1, 1)

        self.lineedit_hora_ida_nuevo_viaje = QLineEdit(self.grupo_ida_viaje)
        self.lineedit_hora_ida_nuevo_viaje.setObjectName(u"lineedit_hora_ida_nuevo_viaje")

        self.gridLayout_28.addWidget(self.lineedit_hora_ida_nuevo_viaje, 0, 1, 1, 1)

        self.combobox_ampm_hora_ida_nuevo_viaje = QComboBox(self.grupo_ida_viaje)
        self.combobox_ampm_hora_ida_nuevo_viaje.addItem("")
        self.combobox_ampm_hora_ida_nuevo_viaje.addItem("")
        self.combobox_ampm_hora_ida_nuevo_viaje.setObjectName(u"combobox_ampm_hora_ida_nuevo_viaje")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.combobox_ampm_hora_ida_nuevo_viaje.sizePolicy().hasHeightForWidth())
        self.combobox_ampm_hora_ida_nuevo_viaje.setSizePolicy(sizePolicy6)
        self.combobox_ampm_hora_ida_nuevo_viaje.setMinimumSize(QSize(100, 40))
        self.combobox_ampm_hora_ida_nuevo_viaje.setMaximumSize(QSize(100, 40))

        self.gridLayout_28.addWidget(self.combobox_ampm_hora_ida_nuevo_viaje, 0, 2, 1, 1)

        self.label_55 = QLabel(self.grupo_ida_viaje)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_28.addWidget(self.label_55, 1, 0, 1, 1)

        self.lineedit_fecha_ida_nuevo_viaje = QLineEdit(self.grupo_ida_viaje)
        self.lineedit_fecha_ida_nuevo_viaje.setObjectName(u"lineedit_fecha_ida_nuevo_viaje")

        self.gridLayout_28.addWidget(self.lineedit_fecha_ida_nuevo_viaje, 1, 1, 1, 1)

        self.label_56 = QLabel(self.grupo_ida_viaje)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_28.addWidget(self.label_56, 2, 0, 1, 1)

        self.lineedit_costo_ida_nuevo_viaje = QLineEdit(self.grupo_ida_viaje)
        self.lineedit_costo_ida_nuevo_viaje.setObjectName(u"lineedit_costo_ida_nuevo_viaje")
        self.lineedit_costo_ida_nuevo_viaje.setMinimumSize(QSize(0, 40))
        self.lineedit_costo_ida_nuevo_viaje.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_28.addWidget(self.lineedit_costo_ida_nuevo_viaje, 2, 1, 1, 1)


        self.gridLayout_25.addWidget(self.grupo_ida_viaje, 1, 0, 1, 1)

        self.grupo_regreso_viaje = QGroupBox(self.scrollAreaWidgetContents)
        self.grupo_regreso_viaje.setObjectName(u"grupo_regreso_viaje")
        self.grupo_regreso_viaje.setEnabled(False)
        self.gridLayout_27 = QGridLayout(self.grupo_regreso_viaje)
        self.gridLayout_27.setSpacing(15)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_67 = QLabel(self.grupo_regreso_viaje)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_27.addWidget(self.label_67, 0, 0, 1, 1)

        self.lineedit_hora_regreso_nuevo_viaje = QLineEdit(self.grupo_regreso_viaje)
        self.lineedit_hora_regreso_nuevo_viaje.setObjectName(u"lineedit_hora_regreso_nuevo_viaje")

        self.gridLayout_27.addWidget(self.lineedit_hora_regreso_nuevo_viaje, 0, 1, 1, 1)

        self.combobox_ampm_hora_regreso_nuevo_viaje = QComboBox(self.grupo_regreso_viaje)
        self.combobox_ampm_hora_regreso_nuevo_viaje.addItem("")
        self.combobox_ampm_hora_regreso_nuevo_viaje.addItem("")
        self.combobox_ampm_hora_regreso_nuevo_viaje.setObjectName(u"combobox_ampm_hora_regreso_nuevo_viaje")
        sizePolicy6.setHeightForWidth(self.combobox_ampm_hora_regreso_nuevo_viaje.sizePolicy().hasHeightForWidth())
        self.combobox_ampm_hora_regreso_nuevo_viaje.setSizePolicy(sizePolicy6)
        self.combobox_ampm_hora_regreso_nuevo_viaje.setMinimumSize(QSize(100, 40))
        self.combobox_ampm_hora_regreso_nuevo_viaje.setMaximumSize(QSize(100, 40))

        self.gridLayout_27.addWidget(self.combobox_ampm_hora_regreso_nuevo_viaje, 0, 2, 1, 1)

        self.label_68 = QLabel(self.grupo_regreso_viaje)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_27.addWidget(self.label_68, 1, 0, 1, 1)

        self.lineedit_fecha_regreso_nuevo_viaje = QLineEdit(self.grupo_regreso_viaje)
        self.lineedit_fecha_regreso_nuevo_viaje.setObjectName(u"lineedit_fecha_regreso_nuevo_viaje")

        self.gridLayout_27.addWidget(self.lineedit_fecha_regreso_nuevo_viaje, 1, 1, 1, 1)

        self.label_69 = QLabel(self.grupo_regreso_viaje)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_27.addWidget(self.label_69, 2, 0, 1, 1)

        self.lineedit_costo_regreso_nuevo_viaje = QLineEdit(self.grupo_regreso_viaje)
        self.lineedit_costo_regreso_nuevo_viaje.setObjectName(u"lineedit_costo_regreso_nuevo_viaje")

        self.gridLayout_27.addWidget(self.lineedit_costo_regreso_nuevo_viaje, 2, 1, 1, 1)


        self.gridLayout_25.addWidget(self.grupo_regreso_viaje, 1, 1, 1, 1)


        self.gridLayout_34.addLayout(self.gridLayout_25, 3, 0, 1, 4)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.checkbox_alojaimento_nuevo_viaje = QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_alojaimento_nuevo_viaje.setObjectName(u"checkbox_alojaimento_nuevo_viaje")

        self.verticalLayout_40.addWidget(self.checkbox_alojaimento_nuevo_viaje)

        self.groupbox_alojamiento_viaje = QGroupBox(self.scrollAreaWidgetContents)
        self.groupbox_alojamiento_viaje.setObjectName(u"groupbox_alojamiento_viaje")
        self.groupbox_alojamiento_viaje.setEnabled(False)
        self.gridLayout_32 = QGridLayout(self.groupbox_alojamiento_viaje)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(40)
        self.gridLayout_32.setVerticalSpacing(25)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_57 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_20.addWidget(self.label_57)

        self.combobox_hote_o_airbnb_nuevo_viaje = QComboBox(self.groupbox_alojamiento_viaje)
        self.combobox_hote_o_airbnb_nuevo_viaje.addItem("")
        self.combobox_hote_o_airbnb_nuevo_viaje.addItem("")
        self.combobox_hote_o_airbnb_nuevo_viaje.setObjectName(u"combobox_hote_o_airbnb_nuevo_viaje")
        self.combobox_hote_o_airbnb_nuevo_viaje.setEditable(True)

        self.horizontalLayout_20.addWidget(self.combobox_hote_o_airbnb_nuevo_viaje)


        self.gridLayout_32.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_7 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_19.addWidget(self.label_7)

        self.lineedit_direccion_nuevo_viaje = QLineEdit(self.groupbox_alojamiento_viaje)
        self.lineedit_direccion_nuevo_viaje.setObjectName(u"lineedit_direccion_nuevo_viaje")

        self.horizontalLayout_19.addWidget(self.lineedit_direccion_nuevo_viaje)


        self.gridLayout_32.addLayout(self.horizontalLayout_19, 0, 1, 1, 2)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setSpacing(15)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_59 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_30.addWidget(self.label_59, 0, 0, 1, 1)

        self.label_61 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_30.addWidget(self.label_61, 1, 0, 1, 1)

        self.lineedit_hora_inicio_nuevo_viaje_alojamiento = QLineEdit(self.groupbox_alojamiento_viaje)
        self.lineedit_hora_inicio_nuevo_viaje_alojamiento.setObjectName(u"lineedit_hora_inicio_nuevo_viaje_alojamiento")

        self.gridLayout_30.addWidget(self.lineedit_hora_inicio_nuevo_viaje_alojamiento, 1, 1, 1, 1)

        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento = QComboBox(self.groupbox_alojamiento_viaje)
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.addItem("")
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.addItem("")
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.setObjectName(u"combobox_ampm_hora_inicio_nuevo_viaje_alojamiento")
        sizePolicy6.setHeightForWidth(self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.sizePolicy().hasHeightForWidth())
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.setSizePolicy(sizePolicy6)
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.setMinimumSize(QSize(100, 40))
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.setMaximumSize(QSize(100, 40))

        self.gridLayout_30.addWidget(self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento, 1, 2, 1, 1)

        self.label_66 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_30.addWidget(self.label_66, 2, 0, 1, 1)

        self.lineedit_fecha_inicio_alojamiento_nuevo_viaje = QLineEdit(self.groupbox_alojamiento_viaje)
        self.lineedit_fecha_inicio_alojamiento_nuevo_viaje.setObjectName(u"lineedit_fecha_inicio_alojamiento_nuevo_viaje")

        self.gridLayout_30.addWidget(self.lineedit_fecha_inicio_alojamiento_nuevo_viaje, 2, 1, 1, 2)


        self.gridLayout_32.addLayout(self.gridLayout_30, 1, 0, 1, 2)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setSpacing(15)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_60 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_31.addWidget(self.label_60, 0, 0, 1, 1)

        self.label_62 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_31.addWidget(self.label_62, 1, 0, 1, 1)

        self.lineedit_hora_fin_nuevo_viaje_alojamiento = QLineEdit(self.groupbox_alojamiento_viaje)
        self.lineedit_hora_fin_nuevo_viaje_alojamiento.setObjectName(u"lineedit_hora_fin_nuevo_viaje_alojamiento")

        self.gridLayout_31.addWidget(self.lineedit_hora_fin_nuevo_viaje_alojamiento, 1, 1, 1, 1)

        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento = QComboBox(self.groupbox_alojamiento_viaje)
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.addItem("")
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.addItem("")
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.setObjectName(u"combobox_ampm_hora_fin_nuevo_viaje_alojamiento")
        sizePolicy6.setHeightForWidth(self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.sizePolicy().hasHeightForWidth())
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.setSizePolicy(sizePolicy6)
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.setMinimumSize(QSize(100, 40))
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.setMaximumSize(QSize(100, 40))

        self.gridLayout_31.addWidget(self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento, 1, 2, 1, 1)

        self.label_64 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_31.addWidget(self.label_64, 2, 0, 1, 1)

        self.lineedit_fecha_fin_alojamiento_nuevo_viaje = QLineEdit(self.groupbox_alojamiento_viaje)
        self.lineedit_fecha_fin_alojamiento_nuevo_viaje.setObjectName(u"lineedit_fecha_fin_alojamiento_nuevo_viaje")

        self.gridLayout_31.addWidget(self.lineedit_fecha_fin_alojamiento_nuevo_viaje, 2, 1, 1, 2)


        self.gridLayout_32.addLayout(self.gridLayout_31, 1, 2, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_58 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_21.addWidget(self.label_58)

        self.line_edit_costo_alojamiento_nuevo_viaje = QLineEdit(self.groupbox_alojamiento_viaje)
        self.line_edit_costo_alojamiento_nuevo_viaje.setObjectName(u"line_edit_costo_alojamiento_nuevo_viaje")

        self.horizontalLayout_21.addWidget(self.line_edit_costo_alojamiento_nuevo_viaje)


        self.gridLayout_32.addLayout(self.horizontalLayout_21, 2, 0, 1, 2)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(15)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_65 = QLabel(self.groupbox_alojamiento_viaje)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(200, 20))
        self.label_65.setMaximumSize(QSize(200, 20))

        self.verticalLayout_34.addWidget(self.label_65)

        self.plaintextedit_info_adicional_nuevo_viaje = QPlainTextEdit(self.groupbox_alojamiento_viaje)
        self.plaintextedit_info_adicional_nuevo_viaje.setObjectName(u"plaintextedit_info_adicional_nuevo_viaje")
        self.plaintextedit_info_adicional_nuevo_viaje.setMaximumSize(QSize(16777215, 100))
        self.plaintextedit_info_adicional_nuevo_viaje.setAcceptDrops(True)
        self.plaintextedit_info_adicional_nuevo_viaje.setTabChangesFocus(False)
        self.plaintextedit_info_adicional_nuevo_viaje.setUndoRedoEnabled(True)
        self.plaintextedit_info_adicional_nuevo_viaje.setOverwriteMode(False)
        self.plaintextedit_info_adicional_nuevo_viaje.setCenterOnScroll(True)

        self.verticalLayout_34.addWidget(self.plaintextedit_info_adicional_nuevo_viaje)


        self.gridLayout_32.addLayout(self.verticalLayout_34, 3, 0, 1, 3)


        self.verticalLayout_40.addWidget(self.groupbox_alojamiento_viaje)


        self.gridLayout_34.addLayout(self.verticalLayout_40, 4, 0, 1, 4)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_14 = QSpacerItem(788, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_14)

        self.save_new_travel_button = QPushButton(self.scrollAreaWidgetContents)
        self.save_new_travel_button.setObjectName(u"save_new_travel_button")
        self.save_new_travel_button.setMinimumSize(QSize(250, 45))
        self.save_new_travel_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.save_new_travel_button)


        self.gridLayout_34.addLayout(self.horizontalLayout_23, 5, 0, 1, 4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_26.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.frame_12, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.nuevo_viaje_page)
        self.Iinerario_page = QWidget()
        self.Iinerario_page.setObjectName(u"Iinerario_page")
        self.Iinerario_page.setStyleSheet(u"QCheckBox {\n"
"    font-size: 14px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color del borde cuando el checkbox est\u00e1 sin marcar y el rat\u00f3n est\u00e1 sobre \u00e9l */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color de fondo cuando est\u00e1 marcado */\n"
"    border: 2px solid #1B4965; /* Color del borde cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"")
        self.gridLayout_7 = QGridLayout(self.Iinerario_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_13 = QFrame(self.Iinerario_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"    font-family: 'Roboto', sans-serif;\n"
"    color: #212121; \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"	padding: 0 8px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */"
                        "\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B49"
                        "65; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: white;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: "
                        "italic;\n"
"}\n"
"\n"
"/* Estilo para QProgressBar */\n"
"QProgressBar {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font-size: 15px;\n"
"    color: #212121; /* Color del texto */\n"
"    background-color: #FAFAFA; /* Color de fondo */\n"
"    height: 10px; /* Alto m\u00e1s peque\u00f1o */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border-radius: 5px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* Estilo para QDateEdit */\n"
"QDateEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left"
                        "-style: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Estilo para QTimeEdit */\n"
"QTimeEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: none;\n"
"    border-left-style: none;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTimeEdit::down-arrow {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Estilo para QCheckBox */\n"
"QCheckBox {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"    color: #1B4965;\n"
"}\n"
""
                        "\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_13)
        self.gridLayout_36.setSpacing(15)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(50, 50, 50, 50)
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 20px;")

        self.gridLayout_36.addWidget(self.label_11, 0, 0, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_25.addWidget(self.label_15)

        self.seleccionar_viaje_itinerario = QComboBox(self.frame_13)
        self.seleccionar_viaje_itinerario.addItem("")
        self.seleccionar_viaje_itinerario.setObjectName(u"seleccionar_viaje_itinerario")
        self.seleccionar_viaje_itinerario.setMinimumSize(QSize(0, 40))
        self.seleccionar_viaje_itinerario.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_25.addWidget(self.seleccionar_viaje_itinerario)


        self.gridLayout_36.addLayout(self.horizontalLayout_25, 1, 0, 1, 2)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.list_widget_de_planes = QListWidget(self.frame_13)
        self.list_widget_de_planes.setObjectName(u"list_widget_de_planes")
        self.list_widget_de_planes.setStyleSheet(u"QListWidget {\n"
"    font-size: 15px; /* Aumenta el tama\u00f1o de la fuente para los elementos */\n"
"    padding: 5px; /* A\u00f1ade un padding alrededor del contenido del QListWidget */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px; /* A\u00f1ade padding a cada elemento para aumentar el espacio entre ellos */\n"
"    margin: 5px 0; /* A\u00f1ade un margen entre cada elemento para mayor separaci\u00f3n vertical */\n"
"}")

        self.verticalLayout_35.addWidget(self.list_widget_de_planes)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)

        self.eliminar_plan_button = QPushButton(self.frame_13)
        self.eliminar_plan_button.setObjectName(u"eliminar_plan_button")
        self.eliminar_plan_button.setMinimumSize(QSize(60, 60))
        self.eliminar_plan_button.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"border: none;\n"
"background-color: #CAE9FF;\n"
"}")
        self.eliminar_plan_button.setIcon(icon11)
        self.eliminar_plan_button.setIconSize(QSize(35, 35))
        self.eliminar_plan_button.setCheckable(True)

        self.horizontalLayout_24.addWidget(self.eliminar_plan_button)


        self.verticalLayout_35.addLayout(self.horizontalLayout_24)


        self.gridLayout_36.addLayout(self.verticalLayout_35, 2, 1, 1, 1)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setSpacing(15)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_35.addWidget(self.label_16, 0, 0, 1, 2)

        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_35.addWidget(self.label_17, 1, 0, 1, 1)

        self.descripcion_del_plan = QLineEdit(self.frame_13)
        self.descripcion_del_plan.setObjectName(u"descripcion_del_plan")
        self.descripcion_del_plan.setMinimumSize(QSize(0, 40))

        self.gridLayout_35.addWidget(self.descripcion_del_plan, 1, 1, 1, 2)

        self.label_71 = QLabel(self.frame_13)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_35.addWidget(self.label_71, 2, 0, 1, 1)

        self.hora_del_plan = QLineEdit(self.frame_13)
        self.hora_del_plan.setObjectName(u"hora_del_plan")

        self.gridLayout_35.addWidget(self.hora_del_plan, 2, 1, 1, 1)

        self.am_pm_del_plan = QComboBox(self.frame_13)
        self.am_pm_del_plan.addItem("")
        self.am_pm_del_plan.addItem("")
        self.am_pm_del_plan.setObjectName(u"am_pm_del_plan")
        sizePolicy6.setHeightForWidth(self.am_pm_del_plan.sizePolicy().hasHeightForWidth())
        self.am_pm_del_plan.setSizePolicy(sizePolicy6)
        self.am_pm_del_plan.setMinimumSize(QSize(100, 40))
        self.am_pm_del_plan.setMaximumSize(QSize(100, 40))

        self.gridLayout_35.addWidget(self.am_pm_del_plan, 2, 2, 1, 1)

        self.label_70 = QLabel(self.frame_13)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_35.addWidget(self.label_70, 3, 0, 1, 1)

        self.fecha_del_plan = QLineEdit(self.frame_13)
        self.fecha_del_plan.setObjectName(u"fecha_del_plan")

        self.gridLayout_35.addWidget(self.fecha_del_plan, 3, 1, 1, 1)

        self.boton_guardar_plan = QPushButton(self.frame_13)
        self.boton_guardar_plan.setObjectName(u"boton_guardar_plan")
        self.boton_guardar_plan.setMinimumSize(QSize(60, 60))
        self.boton_guardar_plan.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"border: none;\n"
"background-color: #CAE9FF;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/Icons/icons/icons8-done-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_guardar_plan.setIcon(icon15)
        self.boton_guardar_plan.setIconSize(QSize(30, 30))
        self.boton_guardar_plan.setCheckable(True)

        self.gridLayout_35.addWidget(self.boton_guardar_plan, 3, 2, 1, 1)


        self.gridLayout_36.addLayout(self.gridLayout_35, 3, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_13, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Iinerario_page)
        self.gastos_page = QWidget()
        self.gastos_page.setObjectName(u"gastos_page")
        self.gridLayout = QGridLayout(self.gastos_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_14 = QFrame(self.gastos_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"\n"
"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"    font-family: 'Roboto', sans-serif;\n"
"    color: #212121; \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"	padding: 0 8px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: "
                        "2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-"
                        "position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: white;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"\n"
"\n"
"/* Estilo para QCheckBox */\n"
"QCheckBox {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"    color: #1B4965;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_14)
        self.gridLayout_39.setSpacing(15)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(50, 50, 50, 50)
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 20px;")

        self.gridLayout_39.addWidget(self.label_12, 0, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_26.addWidget(self.label_18)

        self.seleccionar_viaje_gasto = QComboBox(self.frame_14)
        self.seleccionar_viaje_gasto.addItem("")
        self.seleccionar_viaje_gasto.setObjectName(u"seleccionar_viaje_gasto")
        self.seleccionar_viaje_gasto.setMinimumSize(QSize(0, 40))
        self.seleccionar_viaje_gasto.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_26.addWidget(self.seleccionar_viaje_gasto)


        self.gridLayout_39.addLayout(self.horizontalLayout_26, 1, 0, 1, 1)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.list_widget_gastos = QListWidget(self.frame_14)
        self.list_widget_gastos.setObjectName(u"list_widget_gastos")
        self.list_widget_gastos.setStyleSheet(u"QListWidget {\n"
"    font-size: 15px; /* Aumenta el tama\u00f1o de la fuente para los elementos */\n"
"    padding: 5px; /* A\u00f1ade un padding alrededor del contenido del QListWidget */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px; /* A\u00f1ade padding a cada elemento para aumentar el espacio entre ellos */\n"
"    margin: 5px 0; /* A\u00f1ade un margen entre cada elemento para mayor separaci\u00f3n vertical*/\n"
"	width: 200px:\n"
"	height: 25px;\n"
"}\n"
"")

        self.verticalLayout_36.addWidget(self.list_widget_gastos)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_17)

        self.eliminar_gasto_button = QPushButton(self.frame_14)
        self.eliminar_gasto_button.setObjectName(u"eliminar_gasto_button")
        self.eliminar_gasto_button.setMinimumSize(QSize(60, 60))
        self.eliminar_gasto_button.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"border: none;\n"
"background-color: #CAE9FF;\n"
"}")
        self.eliminar_gasto_button.setIcon(icon11)
        self.eliminar_gasto_button.setIconSize(QSize(35, 35))
        self.eliminar_gasto_button.setCheckable(True)

        self.horizontalLayout_27.addWidget(self.eliminar_gasto_button)


        self.verticalLayout_36.addLayout(self.horizontalLayout_27)


        self.gridLayout_39.addLayout(self.verticalLayout_36, 2, 0, 1, 1)

        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setHorizontalSpacing(20)
        self.gridLayout_37.setVerticalSpacing(15)
        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_37.addWidget(self.label_19, 0, 0, 1, 2)

        self.label_20 = QLabel(self.frame_14)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_37.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_72 = QLabel(self.frame_14)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_37.addWidget(self.label_72, 2, 0, 1, 1)

        self.costo_del_gasto = QLineEdit(self.frame_14)
        self.costo_del_gasto.setObjectName(u"costo_del_gasto")

        self.gridLayout_37.addWidget(self.costo_del_gasto, 2, 1, 1, 1)

        self.label_73 = QLabel(self.frame_14)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_37.addWidget(self.label_73, 3, 0, 1, 1)

        self.fecha_del_gasto = QLineEdit(self.frame_14)
        self.fecha_del_gasto.setObjectName(u"fecha_del_gasto")

        self.gridLayout_37.addWidget(self.fecha_del_gasto, 3, 1, 1, 1)

        self.boton_guardar_gasto = QPushButton(self.frame_14)
        self.boton_guardar_gasto.setObjectName(u"boton_guardar_gasto")
        self.boton_guardar_gasto.setMinimumSize(QSize(60, 60))
        self.boton_guardar_gasto.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"border: none;\n"
"background-color: #CAE9FF;\n"
"}")
        self.boton_guardar_gasto.setIcon(icon15)
        self.boton_guardar_gasto.setIconSize(QSize(30, 30))
        self.boton_guardar_gasto.setCheckable(True)

        self.gridLayout_37.addWidget(self.boton_guardar_gasto, 3, 2, 1, 1)

        self.descripcion_del_gasto = QLineEdit(self.frame_14)
        self.descripcion_del_gasto.setObjectName(u"descripcion_del_gasto")
        self.descripcion_del_gasto.setMinimumSize(QSize(0, 40))

        self.gridLayout_37.addWidget(self.descripcion_del_gasto, 1, 1, 1, 1)


        self.gridLayout_39.addLayout(self.gridLayout_37, 3, 0, 1, 1)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setHorizontalSpacing(0)
        self.gridLayout_38.setVerticalSpacing(15)
        self.label_21 = QLabel(self.frame_14)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(170, 16777215))

        self.gridLayout_38.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_presupuesto_del_viaje = QLabel(self.frame_14)
        self.label_presupuesto_del_viaje.setObjectName(u"label_presupuesto_del_viaje")

        self.gridLayout_38.addWidget(self.label_presupuesto_del_viaje, 0, 1, 1, 1)

        self.label_27 = QLabel(self.frame_14)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(170, 16777215))

        self.gridLayout_38.addWidget(self.label_27, 0, 2, 1, 1)

        self.label_total_de_los_gastos_varios = QLabel(self.frame_14)
        self.label_total_de_los_gastos_varios.setObjectName(u"label_total_de_los_gastos_varios")

        self.gridLayout_38.addWidget(self.label_total_de_los_gastos_varios, 0, 3, 1, 1)

        self.label_24 = QLabel(self.frame_14)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(170, 16777215))

        self.gridLayout_38.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_costo_de_los_vuelos = QLabel(self.frame_14)
        self.label_costo_de_los_vuelos.setObjectName(u"label_costo_de_los_vuelos")

        self.gridLayout_38.addWidget(self.label_costo_de_los_vuelos, 1, 1, 1, 1)

        self.label_30 = QLabel(self.frame_14)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(170, 16777215))

        self.gridLayout_38.addWidget(self.label_30, 1, 2, 1, 1)

        self.label_total_total_gastos = QLabel(self.frame_14)
        self.label_total_total_gastos.setObjectName(u"label_total_total_gastos")

        self.gridLayout_38.addWidget(self.label_total_total_gastos, 1, 3, 1, 1)

        self.label_25 = QLabel(self.frame_14)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(170, 16777215))

        self.gridLayout_38.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_costo_del_alojamiento = QLabel(self.frame_14)
        self.label_costo_del_alojamiento.setObjectName(u"label_costo_del_alojamiento")

        self.gridLayout_38.addWidget(self.label_costo_del_alojamiento, 2, 1, 1, 1)


        self.gridLayout_39.addLayout(self.gridLayout_38, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_14, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.gastos_page)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.gridLayout_16 = QGridLayout(self.notifications_page)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_17 = QFrame(self.notifications_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"    font-family: 'Roboto', sans-serif;\n"
"    color: #212121; \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"	padding: 0 8px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px s"
                        "olid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
""
                        "    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid white:; /* Color principal */\n"
"}\n"
"\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: white;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"\n"
"/* Estilo para QCheckBox */\n"
"QCheckBox {\n"
"    font-size: 14px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"   "
                        " border: 2px solid #1B4965; /* Color del borde cuando el checkbox est\u00e1 sin marcar y el rat\u00f3n est\u00e1 sobre \u00e9l */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color de fondo cuando est\u00e1 marcado */\n"
"    border: 2px solid #1B4965; /* Color del borde cuando est\u00e1 marcado */\n"
"}\n"
"\n"
"/* Estilo desactivado para QLabel */\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Color de texto desactivado */\n"
"	color: #A9A9A9;\n"
"}\n"
"QGroupBox::title:disabled {\n"
"    background-color: #F0F0F0; /* Color de texto desactivado */\n"
"	color: #A9A9A9;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_17)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(50, 50, 50, 50)
        self.notifications_stacked = QStackedWidget(self.frame_17)
        self.notifications_stacked.setObjectName(u"notifications_stacked")
        self.notifications_stacked.setStyleSheet(u"\n"
"QLabel {\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.recordatorios_page = QWidget()
        self.recordatorios_page.setObjectName(u"recordatorios_page")
        self.gridLayout_23 = QGridLayout(self.recordatorios_page)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setVerticalSpacing(6)
        self.gridLayout_23.setContentsMargins(9, -1, -1, -1)
        self.frame = QFrame(self.recordatorios_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-ra"
                        "dius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-c"
                        "olor: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: white;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"/* Estilo para QProgressBar */\n"
"QProgressBar {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font-size: 15px;\n"
"    color: #212121; /* Color del texto */\n"
"    background-color: #FAFAFA; /* Color de fondo */\n"
"    height: 10px"
                        "; /* Alto m\u00e1s peque\u00f1o */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border-radius: 5px;\n"
"    margin: 0px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame)
        self.gridLayout_20.setSpacing(15)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 20px;")

        self.verticalLayout_12.addWidget(self.label_13)

        self.lista_agregar_recordatorios = QListWidget(self.frame)
        self.lista_agregar_recordatorios.setObjectName(u"lista_agregar_recordatorios")
        self.lista_agregar_recordatorios.setStyleSheet(u"QListWidget {\n"
"    font-size: 15px; /* Aumenta el tama\u00f1o de la fuente para los elementos */\n"
"    padding: 5px; /* A\u00f1ade un padding alrededor del contenido del QListWidget */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px; /* A\u00f1ade padding a cada elemento para aumentar el espacio entre ellos */\n"
"    margin: 5px 0; /* A\u00f1ade un margen entre cada elemento para mayor separaci\u00f3n vertical*/\n"
"	width: 200px:\n"
"	height: 25px;\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.lista_agregar_recordatorios)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_18)

        self.eliminar_recordatorio_button = QPushButton(self.frame)
        self.eliminar_recordatorio_button.setObjectName(u"eliminar_recordatorio_button")
        self.eliminar_recordatorio_button.setMinimumSize(QSize(60, 60))
        self.eliminar_recordatorio_button.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"border: none;\n"
"background-color: #CAE9FF;\n"
"}")
        self.eliminar_recordatorio_button.setIcon(icon11)
        self.eliminar_recordatorio_button.setIconSize(QSize(35, 35))
        self.eliminar_recordatorio_button.setCheckable(True)

        self.horizontalLayout_28.addWidget(self.eliminar_recordatorio_button)


        self.verticalLayout_12.addLayout(self.horizontalLayout_28)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_9 = QSpacerItem(658, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.agregar_recordatorio_nuevo = QPushButton(self.frame)
        self.agregar_recordatorio_nuevo.setObjectName(u"agregar_recordatorio_nuevo")
        self.agregar_recordatorio_nuevo.setMinimumSize(QSize(200, 40))
        self.agregar_recordatorio_nuevo.setMaximumSize(QSize(200, 40))
        self.agregar_recordatorio_nuevo.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}")

        self.horizontalLayout.addWidget(self.agregar_recordatorio_nuevo)


        self.verticalLayout_12.addLayout(self.horizontalLayout)


        self.gridLayout_20.addLayout(self.verticalLayout_12, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame, 0, 0, 1, 1)

        self.notifications_stacked.addWidget(self.recordatorios_page)
        self.nuevo_recordatorio_page = QWidget()
        self.nuevo_recordatorio_page.setObjectName(u"nuevo_recordatorio_page")
        self.nuevo_recordatorio_page.setStyleSheet(u"QCheckBox {\n"
"	font-size: 13px;\n"
"	background: transparent;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 13px;\n"
"}\n"
"")
        self.gridLayout_22 = QGridLayout(self.nuevo_recordatorio_page)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_2 = QFrame(self.nuevo_recordatorio_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"}\n"
"QCheckBox {\n"
"    font-size: 14px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 3px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color del borde cuando el checkbox est\u00e1 sin marcar y el rat\u00f3n est\u00e1 sobre \u00e9l */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #1B4965; /* Color de fondo cuando est\u00e1 marcado */\n"
"    border: 2px solid #1B4965; /* Color del borde cuando est\u00e1 marcado */\n"
"}\n"
"/* Estilo desactivado para QLabel */\n"
"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9; /* Color de texto desactivado */\n"
"}\n"
"\n"
"/* Estilo desactivado para QGroupBox */\n"
"QGroupBox"
                        ":disabled {\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"}\n"
"\n"
"/* Estilo desactivado para QComboBox */\n"
"QComboBox:disabled {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9; /* Color de texto desactivado */\n"
"}\n"
"\n"
"/* Estilo desactivado para QPlainTextEdit */\n"
"QPlainTextEdit:disabled {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9; /* Color de texto desactivado */\n"
"}\n"
"/* Estilo desactivado para QLabel */\n"
"QLabel:disabled {\n"
"    background-color: #F0F0F0; /* Color de texto desactivado */\n"
"	color: #A9A9A9;\n"
"}\n"
"QGroupBox::title:disabled {\n"
"    background-color: #F0F0F0; /* Color de texto desactivado */\n"
"	color: #A9A9A9;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPlainTextEdit:disabled"
                        " {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9; /* Color de texto desactivado */\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.volver_recordatorios_agregar_recordatorio_page = QPushButton(self.frame_2)
        self.volver_recordatorios_agregar_recordatorio_page.setObjectName(u"volver_recordatorios_agregar_recordatorio_page")
        self.volver_recordatorios_agregar_recordatorio_page.setMinimumSize(QSize(50, 50))
        self.volver_recordatorios_agregar_recordatorio_page.setStyleSheet(u"border: none;\n"
"background: transparent;")
        icon16 = QIcon()
        icon16.addFile(u":/Icons/icons/icons8-back-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.volver_recordatorios_agregar_recordatorio_page.setIcon(icon16)
        self.volver_recordatorios_agregar_recordatorio_page.setIconSize(QSize(50, 50))

        self.verticalLayout_24.addWidget(self.volver_recordatorios_agregar_recordatorio_page)

        self.verticalSpacer_7 = QSpacerItem(20, 268, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_7)


        self.horizontalLayout_14.addLayout(self.verticalLayout_24)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 20px;")

        self.verticalLayout_16.addWidget(self.lineEdit_2)

        self.text_edit_recordatorio = QTextEdit(self.frame_2)
        self.text_edit_recordatorio.setObjectName(u"text_edit_recordatorio")
        self.text_edit_recordatorio.setMaximumSize(QSize(16777215, 50))
        self.text_edit_recordatorio.setStyleSheet(u"border-bottom: 2px solid gray;\n"
"border-radius: 0px;\n"
"")

        self.verticalLayout_16.addWidget(self.text_edit_recordatorio)


        self.verticalLayout_14.addLayout(self.verticalLayout_16)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.check_box_hora_recordatorio = QCheckBox(self.frame_2)
        self.check_box_hora_recordatorio.setObjectName(u"check_box_hora_recordatorio")

        self.verticalLayout_13.addWidget(self.check_box_hora_recordatorio)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_12.addWidget(self.label_5)

        self.lineedit_hora_recordatorio = QLineEdit(self.frame_2)
        self.lineedit_hora_recordatorio.setObjectName(u"lineedit_hora_recordatorio")
        self.lineedit_hora_recordatorio.setEnabled(False)

        self.horizontalLayout_12.addWidget(self.lineedit_hora_recordatorio)

        self.am_pm_hora_recordatorio = QComboBox(self.frame_2)
        self.am_pm_hora_recordatorio.addItem("")
        self.am_pm_hora_recordatorio.addItem("")
        self.am_pm_hora_recordatorio.setObjectName(u"am_pm_hora_recordatorio")
        self.am_pm_hora_recordatorio.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.am_pm_hora_recordatorio.sizePolicy().hasHeightForWidth())
        self.am_pm_hora_recordatorio.setSizePolicy(sizePolicy6)
        self.am_pm_hora_recordatorio.setMinimumSize(QSize(100, 40))
        self.am_pm_hora_recordatorio.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_12.addWidget(self.am_pm_hora_recordatorio)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lineedit_fecha_recordatorio = QLineEdit(self.frame_2)
        self.lineedit_fecha_recordatorio.setObjectName(u"lineedit_fecha_recordatorio")
        self.lineedit_fecha_recordatorio.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.lineedit_fecha_recordatorio)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.checkbox_lugar_recordatorio = QCheckBox(self.frame_2)
        self.checkbox_lugar_recordatorio.setObjectName(u"checkbox_lugar_recordatorio")

        self.verticalLayout_15.addWidget(self.checkbox_lugar_recordatorio)

        self.lineedit_lugar_recordatorio = QLineEdit(self.frame_2)
        self.lineedit_lugar_recordatorio.setObjectName(u"lineedit_lugar_recordatorio")
        self.lineedit_lugar_recordatorio.setEnabled(False)
        self.lineedit_lugar_recordatorio.setMinimumSize(QSize(0, 30))
        self.lineedit_lugar_recordatorio.setMaximumSize(QSize(16777215, 30))
        self.lineedit_lugar_recordatorio.setStyleSheet(u"QLineEdit{\n"
"background: transparent;\n"
"border: none;\n"
"font-size: 13px;\n"
"border-bottom: 2px solid gray;\n"
"}\n"
"QLineEdit:disabled {\n"
"    background-color: #F0F0F0; /* Color de fondo desactivado */\n"
"    border: 2px solid #D9D9D9; /* Borde desactivado */\n"
"    color: #A9A9A9; /* Color de texto desactivado */\n"
"}")

        self.verticalLayout_15.addWidget(self.lineedit_lugar_recordatorio)


        self.verticalLayout_14.addLayout(self.verticalLayout_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_4 = QSpacerItem(558, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.agregar_recordatorio_button = QPushButton(self.frame_2)
        self.agregar_recordatorio_button.setObjectName(u"agregar_recordatorio_button")
        self.agregar_recordatorio_button.setMinimumSize(QSize(200, 40))
        self.agregar_recordatorio_button.setMaximumSize(QSize(200, 40))
        self.agregar_recordatorio_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}")

        self.horizontalLayout_13.addWidget(self.agregar_recordatorio_button)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_10)


        self.verticalLayout_18.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_8)


        self.gridLayout_5.addLayout(self.verticalLayout_18, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frame_2, 0, 0, 1, 1)

        self.notifications_stacked.addWidget(self.nuevo_recordatorio_page)

        self.gridLayout_24.addWidget(self.notifications_stacked, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_17, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.notifications_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.gridLayout_19 = QGridLayout(self.settings_page)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.frame_16 = QFrame(self.settings_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_16)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(50, 50, 50, 50)
        self.widget_settings = QWidget(self.frame_16)
        self.widget_settings.setObjectName(u"widget_settings")
        self.widget_settings.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_8 = QGridLayout(self.widget_settings)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.configuraciones_stacked = QStackedWidget(self.widget_settings)
        self.configuraciones_stacked.setObjectName(u"configuraciones_stacked")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.configuraciones_stacked.sizePolicy().hasHeightForWidth())
        self.configuraciones_stacked.setSizePolicy(sizePolicy7)
        self.configuraciones_stacked.setStyleSheet(u"background: transparent;")
        self.apoyo_about_us_page = QWidget()
        self.apoyo_about_us_page.setObjectName(u"apoyo_about_us_page")
        self.apoyo_about_us_page.setStyleSheet(u"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"    font-family: 'Roboto', sans-serif;\n"
"    color: #212121; \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-si"
                        "ze: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
""
                        "    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: #FAFAFA;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"/* Estilo para QProgressBar */\n"
"QProgressBar {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font-size: 15px;\n"
"    color: #212121; /* Color del texto */\n"
"    background-color: #FAFAFA; /* Color de fondo */\n"
"    height: 10px; /* Alto m\u00e1s peque\u00f1o */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #1B4965; /* Color princ"
                        "ipal */\n"
"    border-radius: 5px;\n"
"    margin: 0px;\n"
"}\n"
"")
        self.gridLayout_18 = QGridLayout(self.apoyo_about_us_page)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(10)
        self.gridLayout_18.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(20)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.suppor_button_settings = QPushButton(self.apoyo_about_us_page)
        self.suppor_button_settings.setObjectName(u"suppor_button_settings")
        sizePolicy2.setHeightForWidth(self.suppor_button_settings.sizePolicy().hasHeightForWidth())
        self.suppor_button_settings.setSizePolicy(sizePolicy2)
        self.suppor_button_settings.setMinimumSize(QSize(110, 40))

        self.verticalLayout_9.addWidget(self.suppor_button_settings)

        self.label_2 = QLabel(self.apoyo_about_us_page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_9.addWidget(self.label_2)


        self.verticalLayout_28.addLayout(self.verticalLayout_9)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(20)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.about_us_button_settings = QPushButton(self.apoyo_about_us_page)
        self.about_us_button_settings.setObjectName(u"about_us_button_settings")
        sizePolicy2.setHeightForWidth(self.about_us_button_settings.sizePolicy().hasHeightForWidth())
        self.about_us_button_settings.setSizePolicy(sizePolicy2)
        self.about_us_button_settings.setMinimumSize(QSize(110, 40))

        self.verticalLayout_27.addWidget(self.about_us_button_settings)

        self.label = QLabel(self.apoyo_about_us_page)
        self.label.setObjectName(u"label")

        self.verticalLayout_27.addWidget(self.label)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_11)


        self.gridLayout_18.addLayout(self.verticalLayout_28, 0, 0, 1, 1)

        self.configuraciones_stacked.addWidget(self.apoyo_about_us_page)
        self.apoyo_page = QWidget()
        self.apoyo_page.setObjectName(u"apoyo_page")
        self.apoyo_page.setStyleSheet(u"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"    font-family: 'Roboto', sans-serif;\n"
"    color: #212121; \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-si"
                        "ze: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
""
                        "    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: #FAFAFA;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_21 = QGridLayout(self.apoyo_page)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.back_button_support = QPushButton(self.apoyo_page)
        self.back_button_support.setObjectName(u"back_button_support")
        self.back_button_support.setMinimumSize(QSize(50, 50))
        self.back_button_support.setStyleSheet(u"background: transparent;")
        self.back_button_support.setIcon(icon16)
        self.back_button_support.setIconSize(QSize(50, 50))

        self.verticalLayout_29.addWidget(self.back_button_support)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_12)


        self.horizontalLayout_18.addLayout(self.verticalLayout_29)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.list_apoyo = QListWidget(self.apoyo_page)
        QListWidgetItem(self.list_apoyo)
        QListWidgetItem(self.list_apoyo)
        QListWidgetItem(self.list_apoyo)
        QListWidgetItem(self.list_apoyo)
        self.list_apoyo.setObjectName(u"list_apoyo")
        self.list_apoyo.setMinimumSize(QSize(0, 200))
        self.list_apoyo.setMaximumSize(QSize(16777215, 200))
        self.list_apoyo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size: 17px;\n"
"padding: 30px;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_10.addWidget(self.list_apoyo)

        self.plaintext_apoyo = QPlainTextEdit(self.apoyo_page)
        self.plaintext_apoyo.setObjectName(u"plaintext_apoyo")
        self.plaintext_apoyo.setMinimumSize(QSize(0, 100))
        self.plaintext_apoyo.setMaximumSize(QSize(16777215, 100))
        self.plaintext_apoyo.setTabStopDistance(80.000000000000000)
        self.plaintext_apoyo.setCenterOnScroll(True)

        self.verticalLayout_10.addWidget(self.plaintext_apoyo)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.money_edit_apoyo = QLineEdit(self.apoyo_page)
        self.money_edit_apoyo.setObjectName(u"money_edit_apoyo")
        sizePolicy5.setHeightForWidth(self.money_edit_apoyo.sizePolicy().hasHeightForWidth())
        self.money_edit_apoyo.setSizePolicy(sizePolicy5)
        self.money_edit_apoyo.setMinimumSize(QSize(0, 40))
        self.money_edit_apoyo.setMaximumSize(QSize(16777215, 40))
        self.money_edit_apoyo.setMaxLength(10)

        self.horizontalLayout_7.addWidget(self.money_edit_apoyo)

        self.money_combobox_apoyo = QComboBox(self.apoyo_page)
        self.money_combobox_apoyo.addItem("")
        self.money_combobox_apoyo.addItem("")
        self.money_combobox_apoyo.addItem("")
        self.money_combobox_apoyo.setObjectName(u"money_combobox_apoyo")
        self.money_combobox_apoyo.setMinimumSize(QSize(100, 40))
        self.money_combobox_apoyo.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_7.addWidget(self.money_combobox_apoyo)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.enviar_buttton_apoyo = QPushButton(self.apoyo_page)
        self.enviar_buttton_apoyo.setObjectName(u"enviar_buttton_apoyo")
        sizePolicy2.setHeightForWidth(self.enviar_buttton_apoyo.sizePolicy().hasHeightForWidth())
        self.enviar_buttton_apoyo.setSizePolicy(sizePolicy2)
        self.enviar_buttton_apoyo.setMinimumSize(QSize(110, 40))
        self.enviar_buttton_apoyo.setMaximumSize(QSize(110, 40))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setBold(True)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.enviar_buttton_apoyo.setFont(font5)
        self.enviar_buttton_apoyo.setStyleSheet(u"")
        self.enviar_buttton_apoyo.setCheckable(True)

        self.verticalLayout_10.addWidget(self.enviar_buttton_apoyo)


        self.horizontalLayout_18.addLayout(self.verticalLayout_10)


        self.gridLayout_21.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)

        self.configuraciones_stacked.addWidget(self.apoyo_page)
        self.about_us_page = QWidget()
        self.about_us_page.setObjectName(u"about_us_page")
        self.about_us_page.setStyleSheet(u"\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"    font-family: 'Roboto', sans-serif;\n"
"    color: #212121; \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-si"
                        "ze: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: #FAFAFA;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
""
                        "    padding: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: #FAFAFA;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"/* Estilo para QProgressBar */\n"
"QProgressBar {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font-size: 15px;\n"
"    color: #212121; /* Color del texto */\n"
"    background-color: #FAFAFA; /* Color de fondo */\n"
"    height: 10px; /* Alto m\u00e1s peque\u00f1o */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #1B4965; /* Color princ"
                        "ipal */\n"
"    border-radius: 5px;\n"
"    margin: 0px;\n"
"}\n"
"")
        self.gridLayout_13 = QGridLayout(self.about_us_page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.back_button_about_us = QPushButton(self.about_us_page)
        self.back_button_about_us.setObjectName(u"back_button_about_us")
        self.back_button_about_us.setMinimumSize(QSize(50, 50))
        self.back_button_about_us.setStyleSheet(u"background: transparent;")
        self.back_button_about_us.setIcon(icon16)
        self.back_button_about_us.setIconSize(QSize(50, 50))

        self.verticalLayout_26.addWidget(self.back_button_about_us)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_10)


        self.horizontalLayout_17.addLayout(self.verticalLayout_26)

        self.textBrowser = QTextBrowser(self.about_us_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 20px;\n"
"border-radius: 30px;")

        self.horizontalLayout_17.addWidget(self.textBrowser)


        self.gridLayout_13.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.configuraciones_stacked.addWidget(self.about_us_page)

        self.gridLayout_8.addWidget(self.configuraciones_stacked, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_settings, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_16, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.settings_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.gridLayout_4 = QGridLayout(self.profile_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_15 = QFrame(self.profile_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel {\n"
"    color: #1B4965;\n"
"    font-size: 15px;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(27, 73, 101);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #163B52; \n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 0 8px; \n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"    width: 230px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: white; \n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px; \n"
"    padding: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPlainTextEdi"
                        "t:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 15px;\n"
"    spacing: 8px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #BDBDBD;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #1B4965; /* Color principal */\n"
"    border: 2px solid #1B4965;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    padd"
                        "ing: 0 8px;\n"
"    font-size: 15px;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid #1B4965; /* Color principal */\n"
"}\n"
"\n"
"/* Estilo para QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    background-color: white;\n"
"    color: #1B4965; \n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"/* Estilo para QProgressBar */\n"
"QProgressBar {\n"
"    border: 2px solid #BDBDBD;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font-size: 15px;\n"
"    color: #212121; /* Color del texto */\n"
"    background-color: #FAFAFA; /* Color de fondo */\n"
"    height: 10px; /* Alto m\u00e1s peque\u00f1o */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    backgrou"
                        "nd-color: #1B4965; /* Color principal */\n"
"    border-radius: 5px;\n"
"    margin: 0px;\n"
"}\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(30)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(40)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.age_label_profile_2 = QLabel(self.frame_15)
        self.age_label_profile_2.setObjectName(u"age_label_profile_2")

        self.verticalLayout_20.addWidget(self.age_label_profile_2)

        self.age_spinbox_profile_2 = QSpinBox(self.frame_15)
        self.age_spinbox_profile_2.setObjectName(u"age_spinbox_profile_2")
        self.age_spinbox_profile_2.setEnabled(False)
        self.age_spinbox_profile_2.setMinimumSize(QSize(230, 35))
        self.age_spinbox_profile_2.setMaximumSize(QSize(230, 35))
        self.age_spinbox_profile_2.setReadOnly(False)
        self.age_spinbox_profile_2.setMinimum(16)

        self.verticalLayout_20.addWidget(self.age_spinbox_profile_2)

        self.id_label_profile_2 = QLabel(self.frame_15)
        self.id_label_profile_2.setObjectName(u"id_label_profile_2")

        self.verticalLayout_20.addWidget(self.id_label_profile_2)

        self.id_edit_profile_2 = QLineEdit(self.frame_15)
        self.id_edit_profile_2.setObjectName(u"id_edit_profile_2")
        self.id_edit_profile_2.setEnabled(False)
        self.id_edit_profile_2.setMinimumSize(QSize(230, 35))
        self.id_edit_profile_2.setMaximumSize(QSize(230, 35))

        self.verticalLayout_20.addWidget(self.id_edit_profile_2)

        self.country_label_profile_2 = QLabel(self.frame_15)
        self.country_label_profile_2.setObjectName(u"country_label_profile_2")

        self.verticalLayout_20.addWidget(self.country_label_profile_2)

        self.country_edit_profile_2 = QComboBox(self.frame_15)
        self.country_edit_profile_2.addItem("")
        self.country_edit_profile_2.addItem("")
        self.country_edit_profile_2.addItem("")
        self.country_edit_profile_2.addItem("")
        self.country_edit_profile_2.setObjectName(u"country_edit_profile_2")
        self.country_edit_profile_2.setEnabled(False)
        self.country_edit_profile_2.setMinimumSize(QSize(230, 35))
        self.country_edit_profile_2.setMaximumSize(QSize(230, 35))
        self.country_edit_profile_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.country_edit_profile_2.setEditable(True)

        self.verticalLayout_20.addWidget(self.country_edit_profile_2)

        self.adress_label_profile_2 = QLabel(self.frame_15)
        self.adress_label_profile_2.setObjectName(u"adress_label_profile_2")

        self.verticalLayout_20.addWidget(self.adress_label_profile_2)

        self.adress_edit_profile_2 = QLineEdit(self.frame_15)
        self.adress_edit_profile_2.setObjectName(u"adress_edit_profile_2")
        self.adress_edit_profile_2.setEnabled(False)
        self.adress_edit_profile_2.setMinimumSize(QSize(230, 35))
        self.adress_edit_profile_2.setMaximumSize(QSize(230, 35))

        self.verticalLayout_20.addWidget(self.adress_edit_profile_2)

        self.telefono_label_profile_2 = QLabel(self.frame_15)
        self.telefono_label_profile_2.setObjectName(u"telefono_label_profile_2")

        self.verticalLayout_20.addWidget(self.telefono_label_profile_2)

        self.telefono_edit_profile_3 = QLineEdit(self.frame_15)
        self.telefono_edit_profile_3.setObjectName(u"telefono_edit_profile_3")
        self.telefono_edit_profile_3.setEnabled(False)
        self.telefono_edit_profile_3.setMinimumSize(QSize(230, 35))
        self.telefono_edit_profile_3.setMaximumSize(QSize(230, 35))

        self.verticalLayout_20.addWidget(self.telefono_edit_profile_3)


        self.gridLayout_2.addLayout(self.verticalLayout_20, 0, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.name_label_profile_2 = QLabel(self.frame_15)
        self.name_label_profile_2.setObjectName(u"name_label_profile_2")

        self.verticalLayout_17.addWidget(self.name_label_profile_2)

        self.name_edit_profile_2 = QLineEdit(self.frame_15)
        self.name_edit_profile_2.setObjectName(u"name_edit_profile_2")
        self.name_edit_profile_2.setEnabled(False)
        self.name_edit_profile_2.setMinimumSize(QSize(230, 35))
        self.name_edit_profile_2.setMaximumSize(QSize(230, 35))
        self.name_edit_profile_2.setMaxLength(40)

        self.verticalLayout_17.addWidget(self.name_edit_profile_2)

        self.lastname_label_profile_2 = QLabel(self.frame_15)
        self.lastname_label_profile_2.setObjectName(u"lastname_label_profile_2")

        self.verticalLayout_17.addWidget(self.lastname_label_profile_2)

        self.lastname_edit_profile_2 = QLineEdit(self.frame_15)
        self.lastname_edit_profile_2.setObjectName(u"lastname_edit_profile_2")
        self.lastname_edit_profile_2.setEnabled(False)
        self.lastname_edit_profile_2.setMinimumSize(QSize(230, 35))
        self.lastname_edit_profile_2.setMaximumSize(QSize(230, 35))

        self.verticalLayout_17.addWidget(self.lastname_edit_profile_2)

        self.email_label_profile_2 = QLabel(self.frame_15)
        self.email_label_profile_2.setObjectName(u"email_label_profile_2")

        self.verticalLayout_17.addWidget(self.email_label_profile_2)

        self.email_edit_profile_2 = QLineEdit(self.frame_15)
        self.email_edit_profile_2.setObjectName(u"email_edit_profile_2")
        self.email_edit_profile_2.setEnabled(False)
        self.email_edit_profile_2.setMinimumSize(QSize(230, 35))
        self.email_edit_profile_2.setMaximumSize(QSize(230, 35))

        self.verticalLayout_17.addWidget(self.email_edit_profile_2)

        self.pass_label_profile_2 = QLabel(self.frame_15)
        self.pass_label_profile_2.setObjectName(u"pass_label_profile_2")

        self.verticalLayout_17.addWidget(self.pass_label_profile_2)

        self.pass_edit_profile_2 = QLineEdit(self.frame_15)
        self.pass_edit_profile_2.setObjectName(u"pass_edit_profile_2")
        self.pass_edit_profile_2.setEnabled(False)
        self.pass_edit_profile_2.setMinimumSize(QSize(230, 35))
        self.pass_edit_profile_2.setMaximumSize(QSize(230, 35))

        self.verticalLayout_17.addWidget(self.pass_edit_profile_2)

        self.passport_label_profile_2 = QLabel(self.frame_15)
        self.passport_label_profile_2.setObjectName(u"passport_label_profile_2")

        self.verticalLayout_17.addWidget(self.passport_label_profile_2)

        self.passport_edit_profile_2 = QLineEdit(self.frame_15)
        self.passport_edit_profile_2.setObjectName(u"passport_edit_profile_2")
        self.passport_edit_profile_2.setEnabled(False)
        self.passport_edit_profile_2.setMinimumSize(QSize(230, 35))
        self.passport_edit_profile_2.setMaximumSize(QSize(230, 35))

        self.verticalLayout_17.addWidget(self.passport_edit_profile_2)


        self.gridLayout_2.addLayout(self.verticalLayout_17, 0, 1, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.boigraphy_label_profile_2 = QLabel(self.frame_15)
        self.boigraphy_label_profile_2.setObjectName(u"boigraphy_label_profile_2")

        self.verticalLayout_21.addWidget(self.boigraphy_label_profile_2)

        self.biography_paintext_profile_2 = QPlainTextEdit(self.frame_15)
        self.biography_paintext_profile_2.setObjectName(u"biography_paintext_profile_2")
        self.biography_paintext_profile_2.setEnabled(False)
        self.biography_paintext_profile_2.setMinimumSize(QSize(500, 70))
        self.biography_paintext_profile_2.setMaximumSize(QSize(500, 70))
        self.biography_paintext_profile_2.setCenterOnScroll(True)

        self.verticalLayout_21.addWidget(self.biography_paintext_profile_2)


        self.gridLayout_2.addLayout(self.verticalLayout_21, 1, 1, 1, 2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_myprofile_page_photo_2 = QLabel(self.frame_15)
        self.label_myprofile_page_photo_2.setObjectName(u"label_myprofile_page_photo_2")
        self.label_myprofile_page_photo_2.setMinimumSize(QSize(250, 250))
        self.label_myprofile_page_photo_2.setMaximumSize(QSize(250, 250))
        self.label_myprofile_page_photo_2.setPixmap(QPixmap(u":/Icons/icons/sinfoto.png"))
        self.label_myprofile_page_photo_2.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_myprofile_page_photo_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.open_pic_to_profile_pic_2 = QPushButton(self.frame_15)
        self.open_pic_to_profile_pic_2.setObjectName(u"open_pic_to_profile_pic_2")
        self.open_pic_to_profile_pic_2.setEnabled(False)
        self.open_pic_to_profile_pic_2.setMinimumSize(QSize(40, 40))
        self.open_pic_to_profile_pic_2.setMaximumSize(QSize(40, 40))
        self.open_pic_to_profile_pic_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_pic_to_profile_pic_2.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/Icons/icons/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_pic_to_profile_pic_2.setIcon(icon17)
        self.open_pic_to_profile_pic_2.setIconSize(QSize(40, 40))
        self.open_pic_to_profile_pic_2.setCheckable(False)

        self.horizontalLayout_9.addWidget(self.open_pic_to_profile_pic_2)

        self.delete_profile_pic_2 = QPushButton(self.frame_15)
        self.delete_profile_pic_2.setObjectName(u"delete_profile_pic_2")
        self.delete_profile_pic_2.setEnabled(False)
        self.delete_profile_pic_2.setMinimumSize(QSize(30, 30))
        self.delete_profile_pic_2.setMaximumSize(QSize(30, 30))
        self.delete_profile_pic_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_profile_pic_2.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        self.delete_profile_pic_2.setIcon(icon11)
        self.delete_profile_pic_2.setIconSize(QSize(40, 40))
        self.delete_profile_pic_2.setCheckable(False)

        self.horizontalLayout_9.addWidget(self.delete_profile_pic_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.label_progressbar_profile_2 = QLabel(self.frame_15)
        self.label_progressbar_profile_2.setObjectName(u"label_progressbar_profile_2")

        self.verticalLayout_11.addWidget(self.label_progressbar_profile_2)

        self.progressbar_profile_2 = QProgressBar(self.frame_15)
        self.progressbar_profile_2.setObjectName(u"progressbar_profile_2")
        self.progressbar_profile_2.setValue(24)

        self.verticalLayout_11.addWidget(self.progressbar_profile_2)

        self.sexo_groupbox_profile_2 = QGroupBox(self.frame_15)
        self.sexo_groupbox_profile_2.setObjectName(u"sexo_groupbox_profile_2")
        self.sexo_groupbox_profile_2.setEnabled(False)
        self.gridLayout_10 = QGridLayout(self.sexo_groupbox_profile_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.hombre_radio_profile_2 = QRadioButton(self.sexo_groupbox_profile_2)
        self.hombre_radio_profile_2.setObjectName(u"hombre_radio_profile_2")

        self.gridLayout_10.addWidget(self.hombre_radio_profile_2, 0, 0, 1, 1)

        self.otro_radio_profile_2 = QRadioButton(self.sexo_groupbox_profile_2)
        self.otro_radio_profile_2.setObjectName(u"otro_radio_profile_2")

        self.gridLayout_10.addWidget(self.otro_radio_profile_2, 0, 1, 1, 1)

        self.mujer_radio_profile_2 = QRadioButton(self.sexo_groupbox_profile_2)
        self.mujer_radio_profile_2.setObjectName(u"mujer_radio_profile_2")

        self.gridLayout_10.addWidget(self.mujer_radio_profile_2, 1, 0, 1, 1)

        self.none_radio_profile_2 = QRadioButton(self.sexo_groupbox_profile_2)
        self.none_radio_profile_2.setObjectName(u"none_radio_profile_2")
        self.none_radio_profile_2.setChecked(True)

        self.gridLayout_10.addWidget(self.none_radio_profile_2, 1, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.sexo_groupbox_profile_2)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 0, 0, 2, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.edit_profile_2 = QPushButton(self.frame_15)
        self.edit_profile_2.setObjectName(u"edit_profile_2")
        self.edit_profile_2.setMinimumSize(QSize(110, 45))
        self.edit_profile_2.setMaximumSize(QSize(110, 45))
        self.edit_profile_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_profile_2.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.edit_profile_2)


        self.verticalLayout_22.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)


        self.verticalLayout_23.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_6)


        self.gridLayout_15.addLayout(self.verticalLayout_23, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_15, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.profile_page)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.pages)


        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.off2button.toggled.connect(MainWindow.close)
        self.menu_button.toggled.connect(self.menub.setVisible)
        self.itinerary_small_button1.toggled.connect(self.itinerary_small_button2.setChecked)
        self.mytravels_small_button2.toggled.connect(self.mytravels_small_button1.setChecked)
        self.home_small_button2.toggled.connect(self.home_small_button1.setChecked)
        self.settings_small_button2.toggled.connect(self.settings_small_button1.setChecked)
        self.notify_small_button2.toggled.connect(self.notify_small_button1.setChecked)
        self.newtravel_small_button2.toggled.connect(self.newtravel_small_button1.setChecked)
        self.itinerary_small_button2.toggled.connect(self.itinerary_small_button1.setChecked)
        self.off1button.toggled.connect(MainWindow.close)
        self.off1button.toggled.connect(self.off2button.setChecked)
        self.newtravel_small_button1.toggled.connect(self.newtravel_small_button2.setChecked)
        self.bills_small_button2.toggled.connect(self.bills_small_button1.setChecked)
        self.mytravels_small_button1.toggled.connect(self.mytravels_small_button2.setChecked)
        self.bills_small_button1.toggled.connect(self.bills_small_button2.setChecked)
        self.settings_small_button1.toggled.connect(self.settings_small_button2.setChecked)
        self.notify_small_button1.toggled.connect(self.notify_small_button2.setChecked)
        self.menu_button.toggled.connect(self.menus.setHidden)
        self.home_small_button1.toggled.connect(self.home_small_button2.setChecked)
        self.off2button.toggled.connect(self.off1button.setChecked)

        self.stackedWidget.setCurrentIndex(5)
        self.notifications_stacked.setCurrentIndex(0)
        self.configuraciones_stacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_pic_small1.setText("")
        self.home_small_button1.setText("")
        self.mytravels_small_button1.setText("")
        self.newtravel_small_button1.setText("")
        self.itinerary_small_button1.setText("")
        self.bills_small_button1.setText("")
        self.notify_small_button1.setText("")
        self.settings_small_button1.setText("")
        self.off1button.setText("")
        self.label_pic_small2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mi Perfil", None))
        self.home_small_button2.setText(QCoreApplication.translate("MainWindow", u"  Inicio", None))
        self.mytravels_small_button2.setText(QCoreApplication.translate("MainWindow", u"  Mis viajes", None))
        self.newtravel_small_button2.setText(QCoreApplication.translate("MainWindow", u"  Nuevo viaje", None))
        self.itinerary_small_button2.setText(QCoreApplication.translate("MainWindow", u"  Itinerario", None))
        self.bills_small_button2.setText(QCoreApplication.translate("MainWindow", u"  Gastos", None))
        self.notify_small_button2.setText(QCoreApplication.translate("MainWindow", u"  Notificaciones", None))
        self.settings_small_button2.setText(QCoreApplication.translate("MainWindow", u"  Configuracion", None))
        self.off2button.setText(QCoreApplication.translate("MainWindow", u"  Cerrar sesi\u00f3n", None))
        self.menu_button.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-style:normal;\">:</span></p></body></html>", None))
        self.myprofile_button.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Viajes Recomendados", None))
        self.money_combobox_apoyo_2.setItemText(0, QCoreApplication.translate("MainWindow", u"$ COP", None))
        self.money_combobox_apoyo_2.setItemText(1, QCoreApplication.translate("MainWindow", u"$ USD", None))
        self.money_combobox_apoyo_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u20ac Euro", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Paquete a Cartagena de Indias", None))
        self.label_6.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Hotel + vuelo desde Bogot\u00e1", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Hotel Almirante: 5 d\u00edas/4 noches:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"$790.000", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Paquete a San Andr\u00e9s", None))
        self.label_31.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Hotel + vuelo desde Bogot\u00e1", None))
        self.label_40.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Hotel SeaAvenue: 5 d\u00edas/4 noches:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"$1.690.000", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Mis viajes", None))
        self.ver_viaje_guardado_button.setText("")
        self.eliminar_viajeguardado_button.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Nuevo viaje", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.lineedit_titulo_nuevo_viaje.setPlaceholderText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Fecha inicio", None))
        self.lineedit_fechainicio_nuevo_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"d\u00eda-mes-a\u00f1o", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Fecha fin", None))
        self.lineedit_fechafin_nuevo_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"d\u00eda-mes-a\u00f1o", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Presupuesto", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Personas", None))
        self.boton_pareja_nuevo_viaje.setText("")
        self.boton_familia_nuevo_viaje.setText("")
        self.boton_solo_nuevo_viaje.setText("")
        self.checkbox_vuelos_nuevo_viaje.setText(QCoreApplication.translate("MainWindow", u"Vuelos", None))
        self.grupo_ida_viaje.setTitle(QCoreApplication.translate("MainWindow", u"Ida", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.lineedit_hora_ida_nuevo_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.combobox_ampm_hora_ida_nuevo_viaje.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.combobox_ampm_hora_ida_nuevo_viaje.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.lineedit_fecha_ida_nuevo_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"d\u00eda-mes-a\u00f1o", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Costo:", None))
        self.grupo_regreso_viaje.setTitle(QCoreApplication.translate("MainWindow", u"Regreso", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.lineedit_hora_regreso_nuevo_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.combobox_ampm_hora_regreso_nuevo_viaje.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.combobox_ampm_hora_regreso_nuevo_viaje.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.lineedit_fecha_regreso_nuevo_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"d\u00eda-mes-a\u00f1o", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Costo:", None))
        self.checkbox_alojaimento_nuevo_viaje.setText(QCoreApplication.translate("MainWindow", u"Alojamiento", None))
        self.groupbox_alojamiento_viaje.setTitle("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Hospedaje:", None))
        self.combobox_hote_o_airbnb_nuevo_viaje.setItemText(0, QCoreApplication.translate("MainWindow", u"Hotel", None))
        self.combobox_hote_o_airbnb_nuevo_viaje.setItemText(1, QCoreApplication.translate("MainWindow", u"Airbnb", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n o lugar:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.lineedit_hora_inicio_nuevo_viaje_alojamiento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.lineedit_fecha_inicio_alojamiento_nuevo_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"d\u00eda-mes-a\u00f1o", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Fin", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.lineedit_hora_fin_nuevo_viaje_alojamiento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.lineedit_fecha_fin_alojamiento_nuevo_viaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"d\u00eda-mes-a\u00f1o", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Costo:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Informacion adicional", None))
        self.save_new_travel_button.setText(QCoreApplication.translate("MainWindow", u"Guardar Viaje", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Itinerario", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Seleccionar viaje:", None))
        self.seleccionar_viaje_itinerario.setItemText(0, QCoreApplication.translate("MainWindow", u"No Seleccionado", None))

        self.eliminar_plan_button.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Agregar plan:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Plan:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.am_pm_del_plan.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.am_pm_del_plan.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.boton_guardar_plan.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Gastos", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Seleccionar viaje:", None))
        self.seleccionar_viaje_gasto.setItemText(0, QCoreApplication.translate("MainWindow", u"No Seleccionado", None))

        self.eliminar_gasto_button.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Agregar gasto:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.boton_guardar_gasto.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Presupuesto del viaje:", None))
        self.label_presupuesto_del_viaje.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Gastos varios:", None))
        self.label_total_de_los_gastos_varios.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Vuelos:", None))
        self.label_costo_de_los_vuelos.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_total_total_gastos.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Alojamiento:", None))
        self.label_costo_del_alojamiento.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Recordatorios", None))
        self.eliminar_recordatorio_button.setText("")
        self.agregar_recordatorio_nuevo.setText(QCoreApplication.translate("MainWindow", u"Agregar recordatorio", None))
        self.volver_recordatorios_agregar_recordatorio_page.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Recordatorio", None))
        self.check_box_hora_recordatorio.setText(QCoreApplication.translate("MainWindow", u"Hora", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.am_pm_hora_recordatorio.setItemText(0, QCoreApplication.translate("MainWindow", u"AM", None))
        self.am_pm_hora_recordatorio.setItemText(1, QCoreApplication.translate("MainWindow", u"PM", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.checkbox_lugar_recordatorio.setText(QCoreApplication.translate("MainWindow", u"Lugar", None))
        self.agregar_recordatorio_button.setText(QCoreApplication.translate("MainWindow", u"Agregar recordatorio", None))
        self.suppor_button_settings.setText(QCoreApplication.translate("MainWindow", u"Apoyo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sugerencias/comentarios/donate us", None))
        self.about_us_button_settings.setText(QCoreApplication.translate("MainWindow", u"Acerca De", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n acerca de los creadores", None))
        self.back_button_support.setText("")

        __sortingEnabled = self.list_apoyo.isSortingEnabled()
        self.list_apoyo.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_apoyo.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Sugerencias", None));
        ___qlistwidgetitem1 = self.list_apoyo.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Comentarios", None));
        ___qlistwidgetitem2 = self.list_apoyo.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Donaci\u00f3n", None));
        ___qlistwidgetitem3 = self.list_apoyo.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Otro", None));
        self.list_apoyo.setSortingEnabled(__sortingEnabled)

        self.plaintext_apoyo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escribe aqui", None))
        self.money_combobox_apoyo.setItemText(0, QCoreApplication.translate("MainWindow", u"$ COP", None))
        self.money_combobox_apoyo.setItemText(1, QCoreApplication.translate("MainWindow", u"$ USD", None))
        self.money_combobox_apoyo.setItemText(2, QCoreApplication.translate("MainWindow", u"\u20ac Euro", None))

        self.enviar_buttton_apoyo.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.back_button_about_us.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto','sans-serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Desarrolladores:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;"
                        "\">Andres Felipe Martinez Guerra:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Universidad de Nari\u00f1o, estudiante de ingenier\u00eda de sistemas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sebastian David Ordo\u00f1ez Bola\u00f1oz:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Universidad de Nari\u00f1o, estudiante de ingenier\u00eda de sistemas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "
                        "-qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Acerca de la app:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">es una aplicaci\u00f3n de planificaci\u00f3n de viajes personalizada dise\u00f1ada para ayudarte a crear, organizar y disfrutar de tus aventuras de manera m\u00e1s eficiente y agradable.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margi"
                        "n-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Contactos:<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">afmartinez23a@udenar.edu.co</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sdordonez23a@udenar.edu.co</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-s"
                        "ize:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.age_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Edad", None))
        self.id_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"T.I/C.C", None))
        self.country_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Nacionalidad", None))
        self.country_edit_profile_2.setItemText(0, QCoreApplication.translate("MainWindow", u"No Especificar", None))
        self.country_edit_profile_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Colombia", None))
        self.country_edit_profile_2.setItemText(2, QCoreApplication.translate("MainWindow", u"M\u00e9xico", None))
        self.country_edit_profile_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Espa\u00f1a", None))

        self.adress_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.telefono_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.name_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.name_edit_profile_2.setPlaceholderText("")
        self.lastname_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.email_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.pass_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.passport_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Pasaporte", None))
        self.boigraphy_label_profile_2.setText(QCoreApplication.translate("MainWindow", u"Biograf\u00eda", None))
        self.label_myprofile_page_photo_2.setText("")
        self.open_pic_to_profile_pic_2.setText("")
        self.delete_profile_pic_2.setText("")
        self.label_progressbar_profile_2.setText(QCoreApplication.translate("MainWindow", u"Completa tu perfil", None))
        self.sexo_groupbox_profile_2.setTitle(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.hombre_radio_profile_2.setText(QCoreApplication.translate("MainWindow", u"Hombre", None))
        self.otro_radio_profile_2.setText(QCoreApplication.translate("MainWindow", u"Otro", None))
        self.mujer_radio_profile_2.setText(QCoreApplication.translate("MainWindow", u"Mujer", None))
        self.none_radio_profile_2.setText(QCoreApplication.translate("MainWindow", u"No especificar", None))
        self.edit_profile_2.setText(QCoreApplication.translate("MainWindow", u"Editar perfil", None))
    # retranslateUi

