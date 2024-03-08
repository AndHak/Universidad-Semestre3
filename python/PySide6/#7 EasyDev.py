from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property

import sys

class MyFirstWindow(QMainWindow):
    colores = {
        "gris_suave": (213,211,221),
        "beige": (239,208,199),
        "negro": (0,0,0)
    }
    def setup_ui(self):
        self.set_fixed_size(800, 800)

        #Contenedor del titulo
        self.fr_titulo = QFrame(self)
        self.fr_titulo.geometry = QRect(20, 20, 760, 100)
        self.fr_titulo.style_sheet = f"background-color: rgb{self.colores['gris_suave']};"

        #Texto de titulo
        self.titulo = QLabel(self.fr_titulo)
        self.titulo.text = "Aestethically"
        self.titulo.geometry = QRect(0, 0, 760, 100)
        self.titulo.alignment = Qt.AlignCenter
        self.titulo.style_sheet = f"""
            color: {self.colores['negro']};
            font-size: 50px;
            font-weight: bold;
            """

        self.cuadro_principal = QFrame(self)
        self.cuadro_principal.geometry = QRect(20, 140, 500, 640)
        self.cuadro_principal.style_sheet = f"background-color: rgb{self.colores['beige']};"

        #Cuadro principal con inicio de sesion
        self.iniciar_sesion_texto = QLabel(self.cuadro_principal)
        self.iniciar_sesion_texto.text = "Iniciar sesión"
        self.iniciar_sesion_texto.geometry = QRect(20, 30, 500, 50)
        self.iniciar_sesion_texto.alignment = Qt.AlignCenter
        self.iniciar_sesion_texto.style_sheet = f"""
            color: {self.colores['negro']};
            font-size: 25px;
            font-weight: bold;
            """


        self.cuadro_info = QFrame(self)
        self.cuadro_info.geometry = QRect(540, 140, 240, 640)
        self.cuadro_info.style_sheet= f"background-color: rgb{self.colores['gris_suave']};"

#Ejecutar la app
app = QApplication(sys.argv)

window = MyFirstWindow()
window.setup_ui()
window.show()

sys.exit(app.exec_())