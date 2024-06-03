from reproductor_de_musica_ui_ui import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDial, QDoubleSpinBox, QFontComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import sys
import os


class MainMusicApp(QMainWindow, Ui_MainWindow):
    basedir = os.path.dirname(__file__)
    modo_oscuro_activado = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pu♩se Music")
        self.setWindowIcon(QIcon(os.path.join(self.basedir, "icons/icons8-music-100.png")))

        #Conectar botones stacked
        self.settings_button.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_home_settings.clicked.connect(self.mostrar_pagina_principal)
        self.boton_abrir_perfil_page.clicked.connect(self.mostrar_pagina_perfil)
        self.back_to_home_profile.clicked.connect(self.mostrar_pagina_principal)
        self.ecualizador_button.clicked.connect(self.mostrar_pagina_ecualizador)
        self.about_us_button.clicked.connect(self.mostrar_pagina_about_us)
        self.support_button.clicked.connect(self.mostrar_pagina_soporte)
        self.back_to_config_about.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_config_equalizer.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_config_support.clicked.connect(self.mostrar_pagina_settings)
        self.all_songs_button.clicked.connect(self.mostrar_all_songs)
        self.favorite_songs_button.clicked.connect(self.mostrar_favoritas)

        self.mostrar_pagina_principal()
        
        

    def mostrar_pagina_settings(self):
        self.stackedWidget.setCurrentWidget(self.setting_page)

    def mostrar_pagina_principal(self):
        self.stackedWidget.setCurrentWidget(self.principal_page)

    def mostrar_pagina_perfil(self):
        self.stackedWidget.setCurrentWidget(self.profile_page)

    def mostrar_pagina_about_us(self):
        self.stackedWidget.setCurrentWidget(self.about_us_page)

    def mostrar_pagina_ecualizador(self):
        self.stackedWidget.setCurrentWidget(self.equalizer_page)
    
    def mostrar_pagina_soporte(self):
        self.stackedWidget.setCurrentWidget(self.support_page)

    def mostrar_all_songs(self):
        self.stacked_songs.setCurrentWidget(self.all_songs_stack)
    
    def mostrar_favoritas(self):
        self.stacked_songs.setCurrentWidget(self.favorite_songs_stack)

   



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMusicApp()
    window.show()
    sys.exit(app.exec())



    