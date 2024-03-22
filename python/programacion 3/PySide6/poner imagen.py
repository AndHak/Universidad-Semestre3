from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap

import sys
import os

class MainWindow(QWidget):

    imagen = r"C:\Users\andre\Downloads\Personalizacion escritorio\icons\logo_telegram_airplane_air_plane_paper_airplane_icon_143170.png"
    icono = r"C:\Users\andre\Downloads\Personalizacion escritorio\icons\kali2.png"

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicativo 2")
        self.setFixedSize(1280, 720)

        label = QLabel(self)
        imagen = QPixmap(self.imagen)
        label.setPixmap(imagen.scaled(100,100))

        app_icon = QPixmap(self.icono)  # Ruta a tu imagen de icono
        app.setWindowIcon(app_icon)



if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
