from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap

from __feature__ import snake_case, true_property

import sys

class MyFirstWindow(QMainWindow):
    colores = {
        "gris_suave": (213,211,221),
        "beige": (239,208,199),
        "negro": (0,0,0),
        "blanco": (240, 240, 240),
        "azul_aes": (74,123,166)
    }

    imagen_bienvenida = r"C:\Programacion Universidad\Semestre 3\python\PySide6\hamster.jpg"

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
            color: {self.colores['blanco']};
            font-size: 50px;
            font-weight: bold;
            """

        self.cuadro_principal = QFrame(self)
        self.cuadro_principal.geometry = QRect(20, 140, 500, 640)
        self.cuadro_principal.style_sheet = f"background-color: rgb{self.colores['beige']};"

        #Cuadro principal con inicio de sesion
        self.iniciar_sesion_texto = QLabel(self.cuadro_principal)
        self.iniciar_sesion_texto.text = "Iniciar sesión"
        self.iniciar_sesion_texto.geometry = QRect(0, 30, 500, 50)
        self.iniciar_sesion_texto.alignment = Qt.AlignCenter
        self.iniciar_sesion_texto.style_sheet = f"""
            color: {self.colores['negro']};
            font-size: 25px;
            font-weight: bold;
            """
        
        #Input
        self.input_user = QLineEdit(self.cuadro_principal)
        self.input_user.geometry = QRect(150, 120, 200, 40)
        self.input_user.style_sheet = f"""
            background-color: rgb{self.colores['blanco']};
            color: {self.colores['negro']};
            """
        
        #Input
        self.input_password = QLineEdit(self.cuadro_principal)
        self.input_password.geometry = QRect(150, 200, 200, 40)
        self.input_password.style_sheet = f"""
            background-color: rgb{self.colores['blanco']};
            color: {self.colores['negro']};
            """
        
        #Boton
        self.boton_inciar_sesion = QPushButton(self.cuadro_principal)
        self.boton_inciar_sesion.text = "iniciar sesión"
        self.boton_inciar_sesion.geometry = QRect(150, 260, 200, 30)
        self.boton_inciar_sesion.style_sheet = f"""
            color: {self.colores['negro']};
            font-size: 15px;
            background-color: rgb{self.colores['blanco']}
            """
        self.boton_inciar_sesion.clicked.connect(self.obtiene_user)

        #Boton password
        self.boton_password = QPushButton(self.cuadro_principal)
        self.boton_password.text = "Crear una cuenta"
        self.boton_password.geometry = QRect(150, 300, 200, 30)
        self.boton_password.style_sheet = f"""
            color: {self.colores['negro']};
            font-size: 15px;
            background-color: rgb{self.colores['blanco']}
            """


        self.cuadro_info = QFrame(self)
        self.cuadro_info.geometry = QRect(540, 140, 240, 640)
        self.cuadro_info.style_sheet= f"background-color: rgb{self.colores['gris_suave']};"


        self.dialogo = QDialog(self)
        self.dialogo.set_fixed_size(500, 500)

        #Titulo dialogo
        self.titulo_bienvenida = QFrame(self.dialogo)
        self.titulo_bienvenida.geometry = QRect(0, 0, 500, 80)
        self.titulo_bienvenida.style_sheet = f"""
        background-color: rgb{self.colores['azul_aes']};   
        """
        
        #Texto bienvenidos
        self.texto_bienvenida = QLabel(self.titulo_bienvenida)
        self.texto_bienvenida.geometry = QRect(0, 0, 500, 80)
        self.texto_bienvenida.alignment = Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        self.texto_bienvenida.style_sheet = f"""
            color: rgb{self.colores['blanco']};
            font-size: 35px;
            font-weight: bold;
            """
        

    def obtiene_user(self):
        self.texto_bienvenida.text = f"Bienvenido {self.input_user.text}"
        print(f"Usuario: {self.input_user.text}")
        print(f"Clave: {self.input_password.text}")
        self.dialogo.show()

    

        

#Ejecutar la app
app = QApplication(sys.argv)

window = MyFirstWindow()
window.setup_ui()
window.show()

sys.exit(app.exec_())