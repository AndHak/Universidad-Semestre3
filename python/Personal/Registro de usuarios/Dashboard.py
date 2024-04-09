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
        self.user = Usuario("","","","")

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
            # Agregar más rutas de imágenes según sea necesario
        ]
        self.current_image_index = 0

        self.setup_ui()

    def setup_ui(self):
        # Fondo de la ventana
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.update_background()

        # Botones para cambiar la imagen
        btn_prev = QPushButton('Anterior', self)
        btn_prev.setGeometry(20, self.height() // 2, 100, 30)
        btn_prev.clicked.connect(self.prev_image)

        btn_next = QPushButton('Siguiente', self)
        btn_next.setGeometry(self.width() - 120, self.height() // 2, 100, 30)
        btn_next.clicked.connect(self.next_image)

        # Barra de navegación
        nav_bar = QToolBar(self)
        nav_bar.setStyleSheet("""
            QToolBar {
                background-color: transparent;
                font-size: 20px;
                font-family: Verdana;
                color: wwhite;
            }
        """)
        nav_bar.setMovable(False)
        self.addToolBar(nav_bar)

        btn_home = QAction(QIcon(os.path.join(self.basedir, 'images', 'home.png')), 'Home', self)
        btn_profile = QAction(QIcon(os.path.join(self.basedir, 'images', 'profile.png')), 'My Profile', self)
        btn_categories = QAction(QIcon(os.path.join(self.basedir, 'images', 'categories.png')), 'Categories', self)

        nav_bar.addAction(btn_home)
        nav_bar.addAction(btn_profile)
        nav_bar.addAction(btn_categories)

    def update_background(self):
        image_path = self.background_images[self.current_image_index]
        pixmap = QPixmap(image_path)
        self.background_label.setPixmap(pixmap.scaled(self.size()))

    def prev_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.background_images)
        self.update_background()

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.background_images)
        self.update_background()



if __name__ == "__main__":
    app2 = QApplication(sys.argv)
    usuario_logueado = Usuario("","","","")
    window2 = Dashboard(usuario_logueado)
    window2.show()
    sys.exit(app2.exec())
