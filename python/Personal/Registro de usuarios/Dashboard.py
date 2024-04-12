from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
from estilos_dashboard import *
from usuario import *
import pickle
import sys
import os
import re





class Dashboard(QMainWindow):

    basedir = os.path.dirname(__file__)
    colores = {
        'blanco': "#ffffff",
        'azul_claro_claro': "#858CB6",
        'azul_claro': "#676f9d",
        'azul_medio': "#424769",
        'azul_oscuro': "#2d3250",
        'tomate': "#ffb17a",
    }

    def __init__(self, usuario_logueado):
        super().__init__()

        #Imports no tocar
        self.user = usuario_logueado

        self.setWindowTitle("Mountain agency")
        self.resize(QSize(1600, 900))

        # Definir la ruta del archivo de usuarios
        self.usuarios_file = os.path.join(self.basedir, 'datos', 'usuarios_base_data.pkl')

        # Cargar los datos al iniciar la aplicación si el archivo existe
        if os.path.exists(self.usuarios_file):
            with open(self.usuarios_file, 'rb') as archivo:
                self.usuarios_base_data = pickle.load(archivo)

        self.icon = QPixmap(os.path.join(self.basedir, "images/icon.png"))
        self.setWindowIcon(self.icon)

        self.notify_sound = QSoundEffect()
        self.notify_sound.setSource(QUrl.fromLocalFile(os.path.join(self.basedir, "sounds/notify.wav")))
        #Fin imports


        self.background_images = [
            os.path.join(self.basedir, 'images_dashboard', 'rio_de_janeiro.jpg'),
            os.path.join(self.basedir, 'images_dashboard', 'paris.jpg'),
        ]

        self.current_image_index = 0

        self.root_layout = QVBoxLayout()

        self.frame_principal = QFrame()

        self.root_layout.addWidget(self.frame_principal, 100)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

        #Bar widget
        self.bar_widget = QWidget()
        self.barw



    def barra_de_navegacion(self):
        horizontal_layout = QHBoxLayout()

        self.bar_design = QWidget()
        horizontal_layout.addWidget(self.bar_design)

        self.home_button = QPushButton()
        self.home_button.setText("HOME")
        self.home_button.setStyleSheet(estilos_bar_buttons)


        self.main_widget.setLayout(horizontal_layout)

        



if __name__ == "__main__":
    app2 = QApplication(sys.argv)
    usuario_logueado = Usuario("","","","")
    window2 = Dashboard(usuario_logueado)
    window2.show()
    sys.exit(app2.exec())
