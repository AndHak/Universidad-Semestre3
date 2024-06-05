# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reproductor_de_musica_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDial,
    QFontComboBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QTextBrowser, QVBoxLayout, QWidget)
import recurses_rc
import recurses_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1243, 787)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(251, 249, 255);\n"
"")
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.setting_page.setCursor(QCursor(Qt.ArrowCursor))
        self.setting_page.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(179, 159, 255);\n"
"}")
        self.gridLayout_26 = QGridLayout(self.setting_page)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(100)
        self.gridLayout_25.setVerticalSpacing(50)
        self.gridLayout_25.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(50)
        self.gridLayout_6.setVerticalSpacing(30)
        self.label_personalizar_letra = QLabel(self.setting_page)
        self.label_personalizar_letra.setObjectName(u"label_personalizar_letra")
        font = QFont()
        font.setPointSize(11)
        self.label_personalizar_letra.setFont(font)

        self.gridLayout_6.addWidget(self.label_personalizar_letra, 0, 0, 1, 1)

        self.fontComboBox = QFontComboBox(self.setting_page)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setMinimumSize(QSize(0, 40))
        self.fontComboBox.setStyleSheet(u"QFontComboBox {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"    background: rgb(226, 224, 239);\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QFontComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border: 1px solid #5c5c5c;\n"
"    background: rgb(226, 224, 239);\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QFontComboBox::drop-down:hover {\n"
"    background: rgb(216, 214, 229);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.fontComboBox, 1, 0, 1, 1)

        self.spin_box_aumentar_letra = QSpinBox(self.setting_page)
        self.spin_box_aumentar_letra.setObjectName(u"spin_box_aumentar_letra")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spin_box_aumentar_letra.sizePolicy().hasHeightForWidth())
        self.spin_box_aumentar_letra.setSizePolicy(sizePolicy1)
        self.spin_box_aumentar_letra.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"    background: rgb(226, 224, 239);\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 16px;\n"
"    background: rgb(226, 224, 239);\n"
"    border: 1px solid #5c5c5c;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"    background: rgb(216, 214, 229);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 16px;\n"
"    background: rgb(226, 224, 239);\n"
"    border: 1px solid #5c5c5c;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"    background: rgb(216, 214, 229);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    /* Deja los iconos por defecto, no es necesario especificar aqu\u00ed */\n"
"}\n"
"")
        self.spin_box_aumentar_letra.setMinimum(1)
        self.spin_box_aumentar_letra.setMaximum(5)
        self.spin_box_aumentar_letra.setValue(2)

        self.gridLayout_6.addWidget(self.spin_box_aumentar_letra, 1, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_6)

        self.widget_ejemplo = QWidget(self.setting_page)
        self.widget_ejemplo.setObjectName(u"widget_ejemplo")
        sizePolicy1.setHeightForWidth(self.widget_ejemplo.sizePolicy().hasHeightForWidth())
        self.widget_ejemplo.setSizePolicy(sizePolicy1)
        self.widget_ejemplo.setStyleSheet(u"QWidget {\n"
"background-color: rgb(226, 224, 239);\n"
"border-radius: 30px;\n"
"}\n"
"")
        self.gridLayout_9 = QGridLayout(self.widget_ejemplo)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(15)
        self.gridLayout_9.setVerticalSpacing(30)
        self.gridLayout_9.setContentsMargins(30, 20, 30, 20)
        self.verticalSpacer_6 = QSpacerItem(17, 96, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 0, 0, 1, 1)

        self.before_current_label_song_ej = QLabel(self.widget_ejemplo)
        self.before_current_label_song_ej.setObjectName(u"before_current_label_song_ej")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.before_current_label_song_ej.sizePolicy().hasHeightForWidth())
        self.before_current_label_song_ej.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.before_current_label_song_ej.setFont(font1)
        self.before_current_label_song_ej.setStyleSheet(u"color: rgb(131, 131, 131);")
        self.before_current_label_song_ej.setAlignment(Qt.AlignCenter)
        self.before_current_label_song_ej.setWordWrap(True)

        self.gridLayout_9.addWidget(self.before_current_label_song_ej, 1, 0, 1, 1)

        self.actual_current_label_song_ej = QLabel(self.widget_ejemplo)
        self.actual_current_label_song_ej.setObjectName(u"actual_current_label_song_ej")
        sizePolicy2.setHeightForWidth(self.actual_current_label_song_ej.sizePolicy().hasHeightForWidth())
        self.actual_current_label_song_ej.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setWeight(QFont.ExtraBold)
        self.actual_current_label_song_ej.setFont(font2)
        self.actual_current_label_song_ej.setAlignment(Qt.AlignCenter)
        self.actual_current_label_song_ej.setWordWrap(True)

        self.gridLayout_9.addWidget(self.actual_current_label_song_ej, 2, 0, 1, 1)

        self.after_current_label_song_ej = QLabel(self.widget_ejemplo)
        self.after_current_label_song_ej.setObjectName(u"after_current_label_song_ej")
        sizePolicy2.setHeightForWidth(self.after_current_label_song_ej.sizePolicy().hasHeightForWidth())
        self.after_current_label_song_ej.setSizePolicy(sizePolicy2)
        self.after_current_label_song_ej.setFont(font1)
        self.after_current_label_song_ej.setStyleSheet(u"color: rgb(131, 131, 131);")
        self.after_current_label_song_ej.setAlignment(Qt.AlignCenter)
        self.after_current_label_song_ej.setWordWrap(True)

        self.gridLayout_9.addWidget(self.after_current_label_song_ej, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(17, 95, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_5, 4, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.widget_ejemplo)


        self.gridLayout_25.addLayout(self.verticalLayout_8, 1, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_18, 1, 3, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.back_to_home_settings = QPushButton(self.setting_page)
        self.back_to_home_settings.setObjectName(u"back_to_home_settings")
        self.back_to_home_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_home_settings.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.back_to_home_settings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8-home-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_to_home_settings.setIcon(icon)
        self.back_to_home_settings.setIconSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.back_to_home_settings)

        self.horizontalSpacer_4 = QSpacerItem(858, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.gridLayout_25.addLayout(self.horizontalLayout_8, 0, 0, 1, 3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_13, 1, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(50)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ecualizador_button = QPushButton(self.setting_page)
        self.ecualizador_button.setObjectName(u"ecualizador_button")
        self.ecualizador_button.setMinimumSize(QSize(200, 50))
        self.ecualizador_button.setFont(font)
        self.ecualizador_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ecualizador_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.ecualizador_button)

        self.about_us_button = QPushButton(self.setting_page)
        self.about_us_button.setObjectName(u"about_us_button")
        self.about_us_button.setMinimumSize(QSize(200, 50))
        self.about_us_button.setFont(font)
        self.about_us_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_us_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.about_us_button)

        self.support_button = QPushButton(self.setting_page)
        self.support_button.setObjectName(u"support_button")
        self.support_button.setMinimumSize(QSize(200, 50))
        self.support_button.setFont(font)
        self.support_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.support_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.support_button)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_14)


        self.gridLayout_25.addLayout(self.verticalLayout_9, 1, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        self.gridLayout_25.addItem(self.verticalSpacer_17, 2, 2, 1, 1)


        self.gridLayout_26.addLayout(self.gridLayout_25, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.setting_page)
        self.support_page = QWidget()
        self.support_page.setObjectName(u"support_page")
        self.support_page.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(179, 159, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(199, 179, 255);  /* M\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(159, 139, 255);  /* M\u00e1s oscuro */\n"
"}\n"
"")
        self.gridLayout_28 = QGridLayout(self.support_page)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(50, 50, 50, 50)
        self.back_to_config_support = QPushButton(self.support_page)
        self.back_to_config_support.setObjectName(u"back_to_config_support")
        self.back_to_config_support.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_config_support.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8-back-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_to_config_support.setIcon(icon1)
        self.back_to_config_support.setIconSize(QSize(40, 40))
        self.back_to_config_support.setCheckable(True)

        self.gridLayout_27.addWidget(self.back_to_config_support, 0, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 318, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_18, 1, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(100, 100, 100, 100)
        self.list_apoyo = QListWidget(self.support_page)
        QListWidgetItem(self.list_apoyo)
        QListWidgetItem(self.list_apoyo)
        QListWidgetItem(self.list_apoyo)
        self.list_apoyo.setObjectName(u"list_apoyo")
        self.list_apoyo.setMinimumSize(QSize(0, 200))
        self.list_apoyo.setMaximumSize(QSize(16777215, 200))
        self.list_apoyo.setStyleSheet(u"background-color: rgb(226, 224, 239);\n"
"font-size: 17px;\n"
"padding: 30px;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_10.addWidget(self.list_apoyo)

        self.plainTextEdit_support = QPlainTextEdit(self.support_page)
        self.plainTextEdit_support.setObjectName(u"plainTextEdit_support")
        self.plainTextEdit_support.setStyleSheet(u"background-color: rgb(226, 224, 239);\n"
"font-size: 17px;\n"
"padding: 30px;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")

        self.verticalLayout_10.addWidget(self.plainTextEdit_support)

        self.enviar_buttton_apoyo = QPushButton(self.support_page)
        self.enviar_buttton_apoyo.setObjectName(u"enviar_buttton_apoyo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.enviar_buttton_apoyo.sizePolicy().hasHeightForWidth())
        self.enviar_buttton_apoyo.setSizePolicy(sizePolicy3)
        self.enviar_buttton_apoyo.setMinimumSize(QSize(200, 50))
        self.enviar_buttton_apoyo.setMaximumSize(QSize(110, 40))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setBold(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.enviar_buttton_apoyo.setFont(font3)
        self.enviar_buttton_apoyo.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviar_buttton_apoyo.setStyleSheet(u"")
        self.enviar_buttton_apoyo.setCheckable(True)

        self.verticalLayout_10.addWidget(self.enviar_buttton_apoyo)


        self.gridLayout_27.addLayout(self.verticalLayout_10, 1, 1, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_27, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.support_page)
        self.about_us_page = QWidget()
        self.about_us_page.setObjectName(u"about_us_page")
        self.gridLayout_7 = QGridLayout(self.about_us_page)
        self.gridLayout_7.setSpacing(15)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(30)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.back_to_config_about = QPushButton(self.about_us_page)
        self.back_to_config_about.setObjectName(u"back_to_config_about")
        self.back_to_config_about.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_config_about.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")
        self.back_to_config_about.setIcon(icon1)
        self.back_to_config_about.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.back_to_config_about)

        self.verticalSpacer = QSpacerItem(20, 278, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 0, 3, 1)

        self.textBrowser = QTextBrowser(self.about_us_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"\n"
"background-color: rgb(226, 224, 239);\n"
"padding: 20px;\n"
"border-radius: 30px;")

        self.gridLayout_5.addWidget(self.textBrowser, 0, 1, 3, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 0, 3, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_gracias = QLabel(self.about_us_page)
        self.label_gracias.setObjectName(u"label_gracias")
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(25)
        font4.setBold(True)
        self.label_gracias.setFont(font4)
        self.label_gracias.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_gracias, 0, 0, 1, 2)

        self.label_14 = QLabel(self.about_us_page)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setPixmap(QPixmap(u":/icons/icons/icons8-music-100.png"))

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_pulse = QLabel(self.about_us_page)
        self.label_pulse.setObjectName(u"label_pulse")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_pulse.sizePolicy().hasHeightForWidth())
        self.label_pulse.setSizePolicy(sizePolicy4)
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(20)
        font5.setBold(False)
        self.label_pulse.setFont(font5)

        self.gridLayout_4.addWidget(self.label_pulse, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 2, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 2, 2, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.about_us_page)
        self.equalizer_page = QWidget()
        self.equalizer_page.setObjectName(u"equalizer_page")
        self.equalizer_page.setStyleSheet(u"QDial {\n"
"    background: none;\n"
"}\n"
"\n"
"QDial::groove {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #c661ea, stop:1 rgb(179, 159, 255));\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 50%; /* Forma circular */\n"
"}\n"
"\n"
"QDial::handle {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #c661ea, stop:1 rgb(159, 139, 255));\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QDial::handle:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(199, 179, 255), stop:1 rgb(179, 159, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #bbb;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #c661ea, stop: 1 rgb(179, 159, 255)); /* Gradiente vertical invertido */\n"
"    width: 8px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1: 0,"
                        " y1: 0, x2: 0, y2: 1, stop: 0 #c661ea, stop: 1 rgb(159, 139, 255)); /* Gradiente vertical invertido */\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 8px;\n"
"    margin: 0 -5px; \n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(199, 179, 255), stop: 1 rgb(179, 159, 255)); /* Color m\u00e1s claro al hacer hover */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #c661ea, stop: 1 rgb(159, 139, 255)); /* Parte llena de la ranura con gradiente invertido */\n"
"    border: 1px solid #777;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: rgb(201, 200, 222); /* Parte vac\u00eda de la ranura */\n"
"    border: 1px solid #777;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.gridLayout_21 = QGridLayout(self.equalizer_page)
        self.gridLayout_21.setSpacing(40)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(50, 50, 100, 100)
        self.back_to_config_equalizer = QPushButton(self.equalizer_page)
        self.back_to_config_equalizer.setObjectName(u"back_to_config_equalizer")
        self.back_to_config_equalizer.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_config_equalizer.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")
        self.back_to_config_equalizer.setIcon(icon1)
        self.back_to_config_equalizer.setIconSize(QSize(40, 40))
        self.back_to_config_equalizer.setCheckable(True)

        self.gridLayout_21.addWidget(self.back_to_config_equalizer, 0, 0, 1, 1)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setSpacing(30)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.combo_box_equalizer = QComboBox(self.equalizer_page)
        self.combo_box_equalizer.addItem("")
        self.combo_box_equalizer.addItem("")
        self.combo_box_equalizer.addItem("")
        self.combo_box_equalizer.addItem("")
        self.combo_box_equalizer.addItem("")
        self.combo_box_equalizer.setObjectName(u"combo_box_equalizer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.combo_box_equalizer.sizePolicy().hasHeightForWidth())
        self.combo_box_equalizer.setSizePolicy(sizePolicy5)
        self.combo_box_equalizer.setMinimumSize(QSize(300, 30))
        self.combo_box_equalizer.setMaximumSize(QSize(300, 30))
        self.combo_box_equalizer.setSizeIncrement(QSize(300, 0))

        self.gridLayout_20.addWidget(self.combo_box_equalizer, 0, 0, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.dial = QDial(self.equalizer_page)
        self.dial.setObjectName(u"dial")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy6)
        self.dial.setMinimumSize(QSize(100, 100))
        self.dial.setAcceptDrops(False)
        self.dial.setMinimum(-10)
        self.dial.setMaximum(10)

        self.gridLayout_19.addWidget(self.dial, 0, 0, 1, 1)

        self.label_equalizer_ganancia = QLabel(self.equalizer_page)
        self.label_equalizer_ganancia.setObjectName(u"label_equalizer_ganancia")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_equalizer_ganancia.sizePolicy().hasHeightForWidth())
        self.label_equalizer_ganancia.setSizePolicy(sizePolicy7)
        self.label_equalizer_ganancia.setMinimumSize(QSize(0, 30))
        self.label_equalizer_ganancia.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_equalizer_ganancia, 1, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_19, 1, 2, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_equalizer_12dbmas = QLabel(self.equalizer_page)
        self.label_equalizer_12dbmas.setObjectName(u"label_equalizer_12dbmas")

        self.verticalLayout_5.addWidget(self.label_equalizer_12dbmas)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.label_equalizer_0db = QLabel(self.equalizer_page)
        self.label_equalizer_0db.setObjectName(u"label_equalizer_0db")
        sizePolicy3.setHeightForWidth(self.label_equalizer_0db.sizePolicy().hasHeightForWidth())
        self.label_equalizer_0db.setSizePolicy(sizePolicy3)

        self.verticalLayout_5.addWidget(self.label_equalizer_0db)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.label_equalizer_12dbmenos = QLabel(self.equalizer_page)
        self.label_equalizer_12dbmenos.setObjectName(u"label_equalizer_12dbmenos")

        self.verticalLayout_5.addWidget(self.label_equalizer_12dbmenos, 0, Qt.AlignTop)


        self.gridLayout_8.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.slider_60 = QSlider(self.equalizer_page)
        self.slider_60.setObjectName(u"slider_60")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.slider_60.sizePolicy().hasHeightForWidth())
        self.slider_60.setSizePolicy(sizePolicy8)
        self.slider_60.setMinimumSize(QSize(0, 300))
        self.slider_60.setMaximumSize(QSize(16777215, 500))
        self.slider_60.setMinimum(-12)
        self.slider_60.setMaximum(12)
        self.slider_60.setOrientation(Qt.Vertical)
        self.slider_60.setInvertedAppearance(False)

        self.gridLayout_8.addWidget(self.slider_60, 0, 1, 2, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)

        self.slider_250 = QSlider(self.equalizer_page)
        self.slider_250.setObjectName(u"slider_250")
        sizePolicy8.setHeightForWidth(self.slider_250.sizePolicy().hasHeightForWidth())
        self.slider_250.setSizePolicy(sizePolicy8)
        self.slider_250.setMinimumSize(QSize(0, 300))
        self.slider_250.setMaximumSize(QSize(16777215, 500))
        self.slider_250.setMinimum(-12)
        self.slider_250.setMaximum(12)
        self.slider_250.setOrientation(Qt.Vertical)
        self.slider_250.setInvertedAppearance(False)

        self.gridLayout_8.addWidget(self.slider_250, 0, 3, 2, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_15, 0, 4, 1, 1)

        self.slider_1k = QSlider(self.equalizer_page)
        self.slider_1k.setObjectName(u"slider_1k")
        sizePolicy8.setHeightForWidth(self.slider_1k.sizePolicy().hasHeightForWidth())
        self.slider_1k.setSizePolicy(sizePolicy8)
        self.slider_1k.setMinimumSize(QSize(0, 300))
        self.slider_1k.setMaximumSize(QSize(16777215, 500))
        self.slider_1k.setMinimum(-12)
        self.slider_1k.setMaximum(12)
        self.slider_1k.setOrientation(Qt.Vertical)
        self.slider_1k.setInvertedAppearance(False)

        self.gridLayout_8.addWidget(self.slider_1k, 0, 5, 2, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_16, 0, 6, 1, 1)

        self.slider_4k = QSlider(self.equalizer_page)
        self.slider_4k.setObjectName(u"slider_4k")
        sizePolicy8.setHeightForWidth(self.slider_4k.sizePolicy().hasHeightForWidth())
        self.slider_4k.setSizePolicy(sizePolicy8)
        self.slider_4k.setMinimumSize(QSize(0, 300))
        self.slider_4k.setMaximumSize(QSize(16777215, 500))
        self.slider_4k.setMinimum(-12)
        self.slider_4k.setMaximum(12)
        self.slider_4k.setOrientation(Qt.Vertical)
        self.slider_4k.setInvertedAppearance(False)

        self.gridLayout_8.addWidget(self.slider_4k, 0, 7, 2, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_17, 0, 8, 1, 1)

        self.slider_16k = QSlider(self.equalizer_page)
        self.slider_16k.setObjectName(u"slider_16k")
        sizePolicy8.setHeightForWidth(self.slider_16k.sizePolicy().hasHeightForWidth())
        self.slider_16k.setSizePolicy(sizePolicy8)
        self.slider_16k.setMinimumSize(QSize(0, 300))
        self.slider_16k.setMaximumSize(QSize(16777215, 500))
        self.slider_16k.setMinimum(-12)
        self.slider_16k.setMaximum(12)
        self.slider_16k.setOrientation(Qt.Vertical)
        self.slider_16k.setInvertedAppearance(False)

        self.gridLayout_8.addWidget(self.slider_16k, 0, 9, 2, 1)

        self.label_equalizer_60 = QLabel(self.equalizer_page)
        self.label_equalizer_60.setObjectName(u"label_equalizer_60")
        sizePolicy.setHeightForWidth(self.label_equalizer_60.sizePolicy().hasHeightForWidth())
        self.label_equalizer_60.setSizePolicy(sizePolicy)
        self.label_equalizer_60.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_equalizer_60, 2, 1, 1, 1, Qt.AlignTop)

        self.label_equalizer_250 = QLabel(self.equalizer_page)
        self.label_equalizer_250.setObjectName(u"label_equalizer_250")
        sizePolicy.setHeightForWidth(self.label_equalizer_250.sizePolicy().hasHeightForWidth())
        self.label_equalizer_250.setSizePolicy(sizePolicy)
        self.label_equalizer_250.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_equalizer_250, 2, 3, 1, 1, Qt.AlignTop)

        self.label_equalizer_1k = QLabel(self.equalizer_page)
        self.label_equalizer_1k.setObjectName(u"label_equalizer_1k")
        sizePolicy.setHeightForWidth(self.label_equalizer_1k.sizePolicy().hasHeightForWidth())
        self.label_equalizer_1k.setSizePolicy(sizePolicy)
        self.label_equalizer_1k.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_equalizer_1k, 2, 5, 1, 1, Qt.AlignTop)

        self.label_equalizer_4k = QLabel(self.equalizer_page)
        self.label_equalizer_4k.setObjectName(u"label_equalizer_4k")
        sizePolicy.setHeightForWidth(self.label_equalizer_4k.sizePolicy().hasHeightForWidth())
        self.label_equalizer_4k.setSizePolicy(sizePolicy)
        self.label_equalizer_4k.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_equalizer_4k, 2, 7, 1, 1, Qt.AlignTop)

        self.label_equalizer_16k = QLabel(self.equalizer_page)
        self.label_equalizer_16k.setObjectName(u"label_equalizer_16k")
        sizePolicy.setHeightForWidth(self.label_equalizer_16k.sizePolicy().hasHeightForWidth())
        self.label_equalizer_16k.setSizePolicy(sizePolicy)
        self.label_equalizer_16k.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_equalizer_16k, 2, 9, 1, 1, Qt.AlignTop)


        self.gridLayout_20.addLayout(self.gridLayout_8, 1, 0, 3, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_12, 1, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.equalizer_page)
        self.principal_page = QWidget()
        self.principal_page.setObjectName(u"principal_page")
        self.principal_page.setStyleSheet(u"/* Estilo base */\n"
"QPushButton {\n"
"	border: none;\n"
"	background: transparent;\n"
"}\n"
"\n"
"/* Estilo hover */\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"	border-radius: 5px; /* Border radius */\n"
"}\n"
"\n"
"/* Estilo seleccionado */\n"
"QPushButton:selected {\n"
"	background-color: rgba(255, 255, 255, 0.8); /* Cambia la transparencia */\n"
"	border-radius: 5px; /* Border radius */\n"
"}\n"
"")
        self.gridLayout_18 = QGridLayout(self.principal_page)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(15)
        self.frame_2 = QFrame(self.principal_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(20)
        self.gridLayout_17.setVerticalSpacing(10)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.boton_abrir_perfil_page = QPushButton(self.frame_2)
        self.boton_abrir_perfil_page.setObjectName(u"boton_abrir_perfil_page")
        self.boton_abrir_perfil_page.setMinimumSize(QSize(60, 50))
        self.boton_abrir_perfil_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_abrir_perfil_page.setStyleSheet(u"border-radius: 25px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_abrir_perfil_page.setIcon(icon2)
        self.boton_abrir_perfil_page.setIconSize(QSize(50, 50))
        self.boton_abrir_perfil_page.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.boton_abrir_perfil_page, 0, Qt.AlignLeft)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_hora = QLabel(self.frame_2)
        self.label_hora.setObjectName(u"label_hora")
        font6 = QFont()
        font6.setPointSize(14)
        self.label_hora.setFont(font6)
        self.label_hora.setAlignment(Qt.AlignCenter)
        self.label_hora.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_hora)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.settings_button = QPushButton(self.frame_2)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(40, 40))
        self.settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_button.setContextMenuPolicy(Qt.PreventContextMenu)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-configuration-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon3)
        self.settings_button.setIconSize(QSize(40, 40))
        self.settings_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.settings_button)


        self.gridLayout_17.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(5)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy9)
        self.widget_3.setStyleSheet(u"QWidget {\n"
"background-color: rgb(226, 224, 239);\n"
"border-radius: 30px;\n"
"}\n"
"/* Estilo base */\n"
"QPushButton {\n"
"	font-size: 20px;\n"
"	border: none;\n"
"	background: transparent;\n"
"}\n"
"\n"
"/* Estilo hover */\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 0.4); /* Cambia la transparencia */\n"
"	border-radius: 5px; /* Border radius */\n"
"}\n"
"\n"
"/* Estilo seleccionado */\n"
"QPushButton:selected {\n"
"	background-color: rgba(255, 255, 255, 0.6); /* Cambia la transparencia */\n"
"	border-radius: 5px; /* Border radius */\n"
"}\n"
"")
        self.gridLayout_13 = QGridLayout(self.widget_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.all_songs_button = QPushButton(self.widget_3)
        self.all_songs_button.setObjectName(u"all_songs_button")
        sizePolicy5.setHeightForWidth(self.all_songs_button.sizePolicy().hasHeightForWidth())
        self.all_songs_button.setSizePolicy(sizePolicy5)
        self.all_songs_button.setMinimumSize(QSize(70, 70))
        self.all_songs_button.setMaximumSize(QSize(16777215, 70))
        self.all_songs_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/all_songs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.all_songs_button.setIcon(icon4)
        self.all_songs_button.setIconSize(QSize(70, 70))
        self.all_songs_button.setCheckable(True)
        self.all_songs_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.all_songs_button)

        self.favorite_songs_button = QPushButton(self.widget_3)
        self.favorite_songs_button.setObjectName(u"favorite_songs_button")
        sizePolicy5.setHeightForWidth(self.favorite_songs_button.sizePolicy().hasHeightForWidth())
        self.favorite_songs_button.setSizePolicy(sizePolicy5)
        self.favorite_songs_button.setMinimumSize(QSize(70, 70))
        self.favorite_songs_button.setMaximumSize(QSize(16777215, 70))
        self.favorite_songs_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icons8-pixel-heart-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.favorite_songs_button.setIcon(icon5)
        self.favorite_songs_button.setIconSize(QSize(70, 70))
        self.favorite_songs_button.setCheckable(True)
        self.favorite_songs_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.favorite_songs_button)

        self.verticalSpacer_11 = QSpacerItem(20, 372, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)


        self.gridLayout_13.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.widget_3, 1, 0, 1, 1)

        self.letra_widget = QWidget(self.frame_2)
        self.letra_widget.setObjectName(u"letra_widget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(10)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.letra_widget.sizePolicy().hasHeightForWidth())
        self.letra_widget.setSizePolicy(sizePolicy10)
        self.letra_widget.setMinimumSize(QSize(500, 0))
        self.letra_widget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(226, 224, 239);\n"
"border-radius: 30px;\n"
"}")
        self.gridLayout = QGridLayout(self.letra_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(50)
        self.gridLayout.setContentsMargins(40, 30, 40, 30)
        self.verticalSpacer_9 = QSpacerItem(20, 126, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_9, 0, 0, 1, 1)

        self.before_current_label_song = QLabel(self.letra_widget)
        self.before_current_label_song.setObjectName(u"before_current_label_song")
        self.before_current_label_song.setFont(font1)
        self.before_current_label_song.setStyleSheet(u"color: rgb(131, 131, 131);")
        self.before_current_label_song.setAlignment(Qt.AlignCenter)
        self.before_current_label_song.setWordWrap(True)

        self.gridLayout.addWidget(self.before_current_label_song, 1, 0, 1, 1)

        self.actual_current_label_song = QLabel(self.letra_widget)
        self.actual_current_label_song.setObjectName(u"actual_current_label_song")
        self.actual_current_label_song.setFont(font2)
        self.actual_current_label_song.setAlignment(Qt.AlignCenter)
        self.actual_current_label_song.setWordWrap(True)

        self.gridLayout.addWidget(self.actual_current_label_song, 2, 0, 1, 1)

        self.after_current_label_song = QLabel(self.letra_widget)
        self.after_current_label_song.setObjectName(u"after_current_label_song")
        self.after_current_label_song.setFont(font1)
        self.after_current_label_song.setStyleSheet(u"color: rgb(131, 131, 131);")
        self.after_current_label_song.setAlignment(Qt.AlignCenter)
        self.after_current_label_song.setWordWrap(True)

        self.gridLayout.addWidget(self.after_current_label_song, 3, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 125, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_10, 4, 0, 1, 1)


        self.gridLayout_17.addWidget(self.letra_widget, 1, 1, 1, 1)

        self.stacked_songs = QStackedWidget(self.frame_2)
        self.stacked_songs.setObjectName(u"stacked_songs")
        sizePolicy9.setHeightForWidth(self.stacked_songs.sizePolicy().hasHeightForWidth())
        self.stacked_songs.setSizePolicy(sizePolicy9)
        self.stacked_songs.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(226, 224, 239);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    font-size: 14px; /* Tama\u00f1o de la letra */\n"
"    padding: 5px;  /* Espacio interior del widget */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    height: 30px;  /* Altura de los elementos */\n"
"    padding: 5px;  /* Espacio interior de los elementos */\n"
"    border: 1px solid transparent; /* Borde transparente para el padding */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #9796bd; /* Color de fondo para el elemento seleccionado */\n"
"    color: black; /* Color de la letra para el elemento seleccionado */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #7a78a0; /* Color de fondo cuando el mouse est\u00e1 sobre el elemento */\n"
"    color: black; /* Color de la letra cuando el mouse est\u00e1 sobre el elemento */\n"
"}\n"
"")
        self.all_songs_stack = QWidget()
        self.all_songs_stack.setObjectName(u"all_songs_stack")
        self.verticalLayout_11 = QVBoxLayout(self.all_songs_stack)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 20, -1, -1)
        self.all_songs_label_stack = QLabel(self.all_songs_stack)
        self.all_songs_label_stack.setObjectName(u"all_songs_label_stack")
        self.all_songs_label_stack.setFont(font1)

        self.verticalLayout_11.addWidget(self.all_songs_label_stack)

        self.all_songs_list = QListWidget(self.all_songs_stack)
        self.all_songs_list.setObjectName(u"all_songs_list")

        self.verticalLayout_11.addWidget(self.all_songs_list)

        self.cargar_canciones_button = QPushButton(self.all_songs_stack)
        self.cargar_canciones_button.setObjectName(u"cargar_canciones_button")
        self.cargar_canciones_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cargar_canciones_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icons8-plus-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cargar_canciones_button.setIcon(icon6)
        self.cargar_canciones_button.setIconSize(QSize(40, 40))

        self.verticalLayout_11.addWidget(self.cargar_canciones_button, 0, Qt.AlignRight)

        self.stacked_songs.addWidget(self.all_songs_stack)
        self.favorite_songs_stack = QWidget()
        self.favorite_songs_stack.setObjectName(u"favorite_songs_stack")
        self.gridLayout_14 = QGridLayout(self.favorite_songs_stack)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(20, 20, -1, -1)
        self.favorite_song_list = QListWidget(self.favorite_songs_stack)
        self.favorite_song_list.setObjectName(u"favorite_song_list")

        self.gridLayout_14.addWidget(self.favorite_song_list, 1, 0, 1, 1)

        self.favoritas_label_stack = QLabel(self.favorite_songs_stack)
        self.favoritas_label_stack.setObjectName(u"favoritas_label_stack")
        self.favoritas_label_stack.setFont(font1)

        self.gridLayout_14.addWidget(self.favoritas_label_stack, 0, 0, 1, 1)

        self.stacked_songs.addWidget(self.favorite_songs_stack)

        self.gridLayout_17.addWidget(self.stacked_songs, 1, 2, 1, 1)


        self.gridLayout_18.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(self.principal_page)
        self.frame.setObjectName(u"frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"QWidget {\n"
"background-color: rgb(226, 224, 239);\n"
"border-radius: 30px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(50)
        self.gridLayout_11.setVerticalSpacing(10)
        self.gridLayout_11.setContentsMargins(20, 5, 20, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_21 = QPushButton(self.frame)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(40, 40))
        font7 = QFont()
        font7.setPointSize(9)
        self.pushButton_21.setFont(font7)
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/icons8-sound-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/icons/icons8-no-audio-64.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_21.setIcon(icon7)
        self.pushButton_21.setIconSize(QSize(25, 25))
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoDefault(False)

        self.horizontalLayout_5.addWidget(self.pushButton_21)

        self.slider_volume = QSlider(self.frame)
        self.slider_volume.setObjectName(u"slider_volume")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.slider_volume.sizePolicy().hasHeightForWidth())
        self.slider_volume.setSizePolicy(sizePolicy11)
        self.slider_volume.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_volume.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #c661ea, stop: 1 rgb(179, 159, 255)); /* Gradiente horizontal */\n"
"    height: 8px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #c661ea, stop: 1 rgb(159, 139, 255)); /* Gradiente horizontal */\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 8px;\n"
"    margin: -5px 0; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgb(199, 179, 255), stop: 1 rgb(179, 159, 255)); /* Color m\u00e1s claro al hacer hover */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #c661ea, stop: 1 rgb(159, 139, 255)); /* Parte llena de la ranura con gradiente */\n"
"    border: 1px solid #777;\n"
"    height: 10px"
                        ";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(201, 200, 222); /* Parte vac\u00eda de la ranura */\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.slider_volume.setMaximum(100)
        self.slider_volume.setValue(65)
        self.slider_volume.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.slider_volume)

        self.horizontalSpacer_19 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_19)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout_11.addLayout(self.horizontalLayout_6, 0, 5, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(40)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.repeat_button = QPushButton(self.frame)
        self.repeat_button.setObjectName(u"repeat_button")
        self.repeat_button.setMinimumSize(QSize(40, 40))
        self.repeat_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/icons8-replay-100off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icons/icons/icons8-replay-100on.png", QSize(), QIcon.Normal, QIcon.On)
        self.repeat_button.setIcon(icon8)
        self.repeat_button.setIconSize(QSize(30, 30))
        self.repeat_button.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.repeat_button)

        self.previo_button = QPushButton(self.frame)
        self.previo_button.setObjectName(u"previo_button")
        self.previo_button.setMinimumSize(QSize(40, 40))
        self.previo_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/previo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previo_button.setIcon(icon9)
        self.previo_button.setIconSize(QSize(40, 40))
        self.previo_button.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.previo_button)

        self.pause_button = QPushButton(self.frame)
        self.pause_button.setObjectName(u"pause_button")
        sizePolicy5.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy5)
        self.pause_button.setMinimumSize(QSize(50, 50))
        self.pause_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/icons8-reproducir-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_button.setIcon(icon10)
        self.pause_button.setIconSize(QSize(50, 50))
        self.pause_button.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.pause_button, 0, Qt.AlignHCenter)

        self.next_button = QPushButton(self.frame)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMinimumSize(QSize(40, 40))
        self.next_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_button.setIcon(icon11)
        self.next_button.setIconSize(QSize(40, 40))
        self.next_button.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.next_button)

        self.shuffle_button = QPushButton(self.frame)
        self.shuffle_button.setObjectName(u"shuffle_button")
        self.shuffle_button.setMinimumSize(QSize(40, 40))
        self.shuffle_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/icons8-shuffle-100off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/icons/icons/icons8-shuffle-100on.png", QSize(), QIcon.Normal, QIcon.On)
        self.shuffle_button.setIcon(icon12)
        self.shuffle_button.setIconSize(QSize(30, 30))
        self.shuffle_button.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.shuffle_button)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.slider_song = QSlider(self.frame)
        self.slider_song.setObjectName(u"slider_song")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(15)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.slider_song.sizePolicy().hasHeightForWidth())
        self.slider_song.setSizePolicy(sizePolicy12)
        self.slider_song.setMinimumSize(QSize(500, 0))
        self.slider_song.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #c661ea, stop: 1 rgb(179, 159, 255)); /* Gradiente horizontal */\n"
"    height: 8px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #c661ea, stop: 1 rgb(159, 139, 255)); /* Gradiente horizontal */\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 8px;\n"
"    margin: -5px 0; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgb(199, 179, 255), stop: 1 rgb(179, 159, 255)); /* Color m\u00e1s claro al hacer hover */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #c661ea, stop: 1 rgb(159, 139, 255)); /* Parte llena de la ranura con gradiente */\n"
"    border: 1px solid #777;\n"
"    height: 10px"
                        ";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(201, 200, 222); /* Parte vac\u00eda de la ranura */\n"
"    border: 1px solid #777;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.slider_song.setMaximum(1000)
        self.slider_song.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.slider_song)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_11.addLayout(self.verticalLayout, 0, 3, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_10.setHorizontalSpacing(15)
        self.gridLayout_10.setVerticalSpacing(0)
        self.favorite_button = QPushButton(self.frame)
        self.favorite_button.setObjectName(u"favorite_button")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.favorite_button.sizePolicy().hasHeightForWidth())
        self.favorite_button.setSizePolicy(sizePolicy13)
        self.favorite_button.setMinimumSize(QSize(40, 40))
        self.favorite_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/icons8-heart-32.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/icons/icons/icons8-heart-48.png", QSize(), QIcon.Normal, QIcon.On)
        self.favorite_button.setIcon(icon13)
        self.favorite_button.setIconSize(QSize(30, 30))
        self.favorite_button.setCheckable(True)
        self.favorite_button.setAutoDefault(False)

        self.gridLayout_10.addWidget(self.favorite_button, 0, 2, 2, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_imagen_song = QLabel(self.frame)
        self.label_imagen_song.setObjectName(u"label_imagen_song")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.label_imagen_song.sizePolicy().hasHeightForWidth())
        self.label_imagen_song.setSizePolicy(sizePolicy14)
        self.label_imagen_song.setMinimumSize(QSize(60, 60))
        self.label_imagen_song.setMaximumSize(QSize(60, 60))
        self.label_imagen_song.setPixmap(QPixmap(u":/icons/icons/icons8-song-100.png"))
        self.label_imagen_song.setScaledContents(True)
        self.label_imagen_song.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_imagen_song, 0, 0, 2, 1)

        self.label_artista_song = QLabel(self.frame)
        self.label_artista_song.setObjectName(u"label_artista_song")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.label_artista_song.sizePolicy().hasHeightForWidth())
        self.label_artista_song.setSizePolicy(sizePolicy15)
        self.label_artista_song.setMinimumSize(QSize(100, 20))
        self.label_artista_song.setMaximumSize(QSize(100, 20))

        self.gridLayout_10.addWidget(self.label_artista_song, 1, 1, 1, 1, Qt.AlignBottom)

        self.label_titulo_song = QLabel(self.frame)
        self.label_titulo_song.setObjectName(u"label_titulo_song")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.label_titulo_song.sizePolicy().hasHeightForWidth())
        self.label_titulo_song.setSizePolicy(sizePolicy16)
        self.label_titulo_song.setMinimumSize(QSize(100, 50))
        self.label_titulo_song.setMaximumSize(QSize(100, 50))
        self.label_titulo_song.setFont(font6)
        self.label_titulo_song.setWordWrap(False)
        self.label_titulo_song.setMargin(0)

        self.gridLayout_10.addWidget(self.label_titulo_song, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.principal_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.profile_page.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 3px;\n"
"    background: rgb(226, 224, 239);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgb(216, 214, 229);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #5c5c5c;\n"
"    border-radius: 3px;\n"
"    background: rgb(155, 129, 255);\n"
"}\n"
"\n"
"")
        self.gridLayout_24 = QGridLayout(self.profile_page)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.widget = QWidget(self.profile_page)
        self.widget.setObjectName(u"widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(226, 224, 239);\n"
"}")
        self.gridLayout_22 = QGridLayout(self.widget)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(30, 40, 40, 40)
        self.horizontalSpacer = QSpacerItem(400, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.boton_foto_de_perfil = QPushButton(self.widget)
        self.boton_foto_de_perfil.setObjectName(u"boton_foto_de_perfil")
        self.boton_foto_de_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_foto_de_perfil.setStyleSheet(u"border-radius: 87px;")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/user 2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_foto_de_perfil.setIcon(icon14)
        self.boton_foto_de_perfil.setIconSize(QSize(170, 170))
        self.boton_foto_de_perfil.setCheckable(True)

        self.gridLayout_22.addWidget(self.boton_foto_de_perfil, 0, 1, 2, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_perfil = QLabel(self.widget)
        self.label_perfil.setObjectName(u"label_perfil")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.label_perfil.sizePolicy().hasHeightForWidth())
        self.label_perfil.setSizePolicy(sizePolicy17)
        self.label_perfil.setMinimumSize(QSize(0, 25))
        font8 = QFont()
        font8.setFamilies([u"Verdana"])
        font8.setBold(True)
        self.label_perfil.setFont(font8)

        self.verticalLayout_2.addWidget(self.label_perfil)

        self.tu_nombre_button = QPushButton(self.widget)
        self.tu_nombre_button.setObjectName(u"tu_nombre_button")
        sizePolicy18 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.tu_nombre_button.sizePolicy().hasHeightForWidth())
        self.tu_nombre_button.setSizePolicy(sizePolicy18)
        font9 = QFont()
        font9.setFamilies([u"Moran Demo"])
        font9.setPointSize(58)
        font9.setBold(False)
        self.tu_nombre_button.setFont(font9)
        self.tu_nombre_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.tu_nombre_button.setCheckable(True)

        self.verticalLayout_2.addWidget(self.tu_nombre_button)


        self.gridLayout_22.addLayout(self.verticalLayout_2, 0, 2, 2, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.back_to_home_profile = QPushButton(self.widget)
        self.back_to_home_profile.setObjectName(u"back_to_home_profile")
        self.back_to_home_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_home_profile.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")
        self.back_to_home_profile.setIcon(icon)
        self.back_to_home_profile.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.back_to_home_profile, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_2)


        self.gridLayout_22.addLayout(self.verticalLayout_7, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.widget, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(30)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(50)
        self.label_agregar_tu_nombre = QLabel(self.profile_page)
        self.label_agregar_tu_nombre.setObjectName(u"label_agregar_tu_nombre")
        sizePolicy.setHeightForWidth(self.label_agregar_tu_nombre.sizePolicy().hasHeightForWidth())
        self.label_agregar_tu_nombre.setSizePolicy(sizePolicy)
        font10 = QFont()
        font10.setFamilies([u"Verdana"])
        font10.setPointSize(11)
        self.label_agregar_tu_nombre.setFont(font10)

        self.gridLayout_2.addWidget(self.label_agregar_tu_nombre, 0, 0, 1, 1)

        self.checkbox_agrega_tu_nombre = QCheckBox(self.profile_page)
        self.checkbox_agrega_tu_nombre.setObjectName(u"checkbox_agrega_tu_nombre")
        self.checkbox_agrega_tu_nombre.setCheckable(False)

        self.gridLayout_2.addWidget(self.checkbox_agrega_tu_nombre, 0, 1, 1, 1)

        self.label_pon_una_foto = QLabel(self.profile_page)
        self.label_pon_una_foto.setObjectName(u"label_pon_una_foto")
        sizePolicy.setHeightForWidth(self.label_pon_una_foto.sizePolicy().hasHeightForWidth())
        self.label_pon_una_foto.setSizePolicy(sizePolicy)
        self.label_pon_una_foto.setFont(font10)

        self.gridLayout_2.addWidget(self.label_pon_una_foto, 1, 0, 1, 1)

        self.checkbox_pon_una_foto = QCheckBox(self.profile_page)
        self.checkbox_pon_una_foto.setObjectName(u"checkbox_pon_una_foto")
        self.checkbox_pon_una_foto.setCheckable(False)

        self.gridLayout_2.addWidget(self.checkbox_pon_una_foto, 1, 1, 1, 1)

        self.label_agrega_canciones = QLabel(self.profile_page)
        self.label_agrega_canciones.setObjectName(u"label_agrega_canciones")
        sizePolicy.setHeightForWidth(self.label_agrega_canciones.sizePolicy().hasHeightForWidth())
        self.label_agrega_canciones.setSizePolicy(sizePolicy)
        self.label_agrega_canciones.setFont(font10)

        self.gridLayout_2.addWidget(self.label_agrega_canciones, 2, 0, 1, 1)

        self.checkbox_agrega_canciones = QCheckBox(self.profile_page)
        self.checkbox_agrega_canciones.setObjectName(u"checkbox_agrega_canciones")
        self.checkbox_agrega_canciones.setCheckable(False)

        self.gridLayout_2.addWidget(self.checkbox_agrega_canciones, 2, 1, 1, 1)

        self.label_agrega_favoritas = QLabel(self.profile_page)
        self.label_agrega_favoritas.setObjectName(u"label_agrega_favoritas")
        sizePolicy.setHeightForWidth(self.label_agrega_favoritas.sizePolicy().hasHeightForWidth())
        self.label_agrega_favoritas.setSizePolicy(sizePolicy)
        self.label_agrega_favoritas.setFont(font10)

        self.gridLayout_2.addWidget(self.label_agrega_favoritas, 3, 0, 1, 1)

        self.checkbox_agrega_favoritas = QCheckBox(self.profile_page)
        self.checkbox_agrega_favoritas.setObjectName(u"checkbox_agrega_favoritas")
        self.checkbox_agrega_favoritas.setCheckable(False)

        self.gridLayout_2.addWidget(self.checkbox_agrega_favoritas, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(41, 228, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 0, 0, 2, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_12)

        self.label_progreso_en_la_app = QLabel(self.profile_page)
        self.label_progreso_en_la_app.setObjectName(u"label_progreso_en_la_app")
        sizePolicy7.setHeightForWidth(self.label_progreso_en_la_app.sizePolicy().hasHeightForWidth())
        self.label_progreso_en_la_app.setSizePolicy(sizePolicy7)
        self.label_progreso_en_la_app.setFont(font)

        self.verticalLayout_6.addWidget(self.label_progreso_en_la_app)

        self.progressBar = QProgressBar(self.profile_page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background: rgb(201, 200, 222);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #c661ea, stop: 1 rgb(179, 159, 255)\n"
"    ); /* Gradiente horizontal */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk:hover {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 rgb(199, 179, 255), stop: 1 rgb(179, 159, 255)\n"
"    ); /* Gradiente m\u00e1s claro al hacer hover */\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.verticalLayout_6.addWidget(self.progressBar)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_23, 0, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_13, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.profile_page)

        self.verticalLayout_12.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.stacked_songs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_personalizar_letra.setText(QCoreApplication.translate("MainWindow", u"Personalizar letra:", None))
        self.before_current_label_song_ej.setText(QCoreApplication.translate("MainWindow", u"Soy la letra de tu cancion antes", None))
        self.actual_current_label_song_ej.setText(QCoreApplication.translate("MainWindow", u"Soy la letra de tu cancion actual", None))
        self.after_current_label_song_ej.setText(QCoreApplication.translate("MainWindow", u"Soy la letra de tu cancion despues", None))
        self.back_to_home_settings.setText("")
        self.ecualizador_button.setText(QCoreApplication.translate("MainWindow", u"ecualizador", None))
        self.about_us_button.setText(QCoreApplication.translate("MainWindow", u"about us", None))
        self.support_button.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.back_to_config_support.setText("")

        __sortingEnabled = self.list_apoyo.isSortingEnabled()
        self.list_apoyo.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_apoyo.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Sugerencias", None));
        ___qlistwidgetitem1 = self.list_apoyo.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Comentarios", None));
        ___qlistwidgetitem2 = self.list_apoyo.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Otro", None));
        self.list_apoyo.setSortingEnabled(__sortingEnabled)

        self.enviar_buttton_apoyo.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.back_to_config_about.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Desarrolladores:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-"
                        "indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Andres Felipe Martinez Guerra:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Universidad de Nari\u00f1o, estudiante de ingenier\u00eda de sistemas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Sebastian David Ordo\u00f1ez Bola\u00f1oz:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:"
                        "'Roboto','sans-serif'; font-size:12pt;\">Universidad de Nari\u00f1o, estudiante de ingenier\u00eda de sistemas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Acerca de la app:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-botto"
                        "m:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">es una app dise\u00f1ada para que escuches tu musica con una interfaz agradable a la vista, con la cualidad de cambiar a modo oscuro o claro segun la preferencia del usuario, personalizable en la seleccion de la letra y el tama\u00f1o de esta, tienes la cualidad de que agregues tus canciones favoritas, cambiar de cancion en modo aleatorio o activar la repeticion continua de una</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Contactos:<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">afmartinez23a@udenar.edu.co</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">sdordonez23a@udenar.edu.co</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-s"
                        "ize:12pt;\"><br /></p></body></html>", None))
        self.label_gracias.setText(QCoreApplication.translate("MainWindow", u"Gracias por usar pu\u2669se :)", None))
        self.label_14.setText("")
        self.label_pulse.setText(QCoreApplication.translate("MainWindow", u"Pu\u2669se!", None))
        self.back_to_config_equalizer.setText("")
        self.combo_box_equalizer.setItemText(0, QCoreApplication.translate("MainWindow", u"Plane", None))
        self.combo_box_equalizer.setItemText(1, QCoreApplication.translate("MainWindow", u"Bass", None))
        self.combo_box_equalizer.setItemText(2, QCoreApplication.translate("MainWindow", u"Vocal", None))
        self.combo_box_equalizer.setItemText(3, QCoreApplication.translate("MainWindow", u"Clasical", None))
        self.combo_box_equalizer.setItemText(4, QCoreApplication.translate("MainWindow", u"User", None))

        self.label_equalizer_ganancia.setText(QCoreApplication.translate("MainWindow", u"Ganancia", None))
        self.label_equalizer_12dbmas.setText(QCoreApplication.translate("MainWindow", u"+ 12 dB", None))
        self.label_equalizer_0db.setText(QCoreApplication.translate("MainWindow", u"0 dB", None))
        self.label_equalizer_12dbmenos.setText(QCoreApplication.translate("MainWindow", u"- 12 dB", None))
        self.label_equalizer_60.setText(QCoreApplication.translate("MainWindow", u"60 Hz", None))
        self.label_equalizer_250.setText(QCoreApplication.translate("MainWindow", u"250 Hz", None))
        self.label_equalizer_1k.setText(QCoreApplication.translate("MainWindow", u"1000 Hz", None))
        self.label_equalizer_4k.setText(QCoreApplication.translate("MainWindow", u"4000 Hz", None))
        self.label_equalizer_16k.setText(QCoreApplication.translate("MainWindow", u"16000 Hz", None))
        self.boton_abrir_perfil_page.setText("")
        self.label_hora.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.settings_button.setText("")
        self.all_songs_button.setText(QCoreApplication.translate("MainWindow", u"  Todas las canciones", None))
        self.favorite_songs_button.setText(QCoreApplication.translate("MainWindow", u"  Favoritas", None))
        self.before_current_label_song.setText(QCoreApplication.translate("MainWindow", u"Soy la letra de tu cancion antes", None))
        self.actual_current_label_song.setText(QCoreApplication.translate("MainWindow", u"Soy la letra de tu cancion actual", None))
        self.after_current_label_song.setText(QCoreApplication.translate("MainWindow", u"Soy la letra de tu cancion despues", None))
        self.all_songs_label_stack.setText(QCoreApplication.translate("MainWindow", u"Todas las canciones", None))
        self.cargar_canciones_button.setText("")
        self.favoritas_label_stack.setText(QCoreApplication.translate("MainWindow", u"Favoritas", None))
        self.pushButton_21.setText("")
        self.repeat_button.setText("")
        self.previo_button.setText("")
        self.pause_button.setText("")
        self.next_button.setText("")
        self.shuffle_button.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.favorite_button.setText("")
        self.label_imagen_song.setText("")
        self.label_artista_song.setText(QCoreApplication.translate("MainWindow", u"artista", None))
        self.label_titulo_song.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.boton_foto_de_perfil.setText("")
        self.label_perfil.setText(QCoreApplication.translate("MainWindow", u"perfil", None))
        self.tu_nombre_button.setText(QCoreApplication.translate("MainWindow", u"TU NOMBRE", None))
        self.back_to_home_profile.setText("")
        self.label_agregar_tu_nombre.setText(QCoreApplication.translate("MainWindow", u"Agrega tu nonbre", None))
        self.checkbox_agrega_tu_nombre.setText("")
        self.label_pon_una_foto.setText(QCoreApplication.translate("MainWindow", u"Pon una foto", None))
        self.checkbox_pon_una_foto.setText("")
        self.label_agrega_canciones.setText(QCoreApplication.translate("MainWindow", u"Agrega canciones", None))
        self.checkbox_agrega_canciones.setText("")
        self.label_agrega_favoritas.setText(QCoreApplication.translate("MainWindow", u"A\u00f1ade 5 canciones a favoritas", None))
        self.checkbox_agrega_favoritas.setText("")
        self.label_progreso_en_la_app.setText(QCoreApplication.translate("MainWindow", u"Progreso en la app", None))
    # retranslateUi

