from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, 
                               QLabel, QLineEdit, QCheckBox, QFrame)
from PySide6.QtGui import QFont, QPixmap
import sys


class Login(QWidget):

    colores = {
        "gris_suave": (213,211,221),
        "beige": (239,208,199),
        "negro": (0,0,0)
    }
    
    def __init__(self):
        super().__init__()
        self.start_iu()
        self.generar_formulario()
    
    def start_iu(self):
        self.setFixedSize(800, 800)

        # Contenedor del titulo
        self.fr_titulo = QFrame(self)
        self.fr_titulo.setGeometry(20, 20, 760, 100)
        self.fr_titulo.setStyleSheet(f"background-color: rgb{self.colores['gris_suave']};")

        # Texto de titulo
        self.titulo = QLabel(self.fr_titulo)
        self.titulo.setText("Aestethically")
        self.titulo.setGeometry(0, 0, 760, 100)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet(f"""
            color: {self.colores['negro']};
            font-size: 50px;
            font-weight: bold;
            """)

        self.cuadro_principal = QFrame(self)
        self.cuadro_principal.setGeometry(20, 140, 500, 640)
        self.cuadro_principal.setStyleSheet(f"background-color: rgb{self.colores['beige']};")

        # Cuadro principal con inicio de sesion
        self.iniciar_sesion_texto = QLabel(self.cuadro_principal)
        self.iniciar_sesion_texto.setText("Iniciar sesión")
        self.iniciar_sesion_texto.setGeometry(20, 30, 500, 50)
        self.iniciar_sesion_texto.setAlignment(Qt.AlignCenter)
        self.iniciar_sesion_texto.setStyleSheet(f"""
            color: {self.colores['negro']};
            font-size: 25px;
            font-weight: bold;
            """)


        self.cuadro_info = QFrame(self)
        self.cuadro_info.setGeometry(540, 140, 240, 640)
        self.cuadro_info.setStyleSheet(f"background-color: rgb{self.colores['gris_suave']};")

    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self.cuadro_principal)
        user_label.setText("User")
        user_label.setFont(QFont("Arial", 10))
        user_label.move(20, 100)
        
        self.user_input = QLineEdit(self.cuadro_principal)
        self.user_input.resize(250, 130)  # ancho, alto
        self.user_input.move(90, 100)

        password_label = QLabel(self.cuadro_principal)
        password_label.setText("Password")
        password_label.setFont(QFont("Arial", 10))
        password_label.move(20, 130)

        self.password_input = QLineEdit(self.cuadro_principal)
        self.password_input.resize(250, 24)  # width, height
        self.password_input.move(90, 130)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.check_view_password = QCheckBox(self.cuadro_principal)
        self.check_view_password.setText("View Password")
        self.check_view_password.move(90, 140)
        
        login_button = QPushButton(self.cuadro_principal)
        login_button.setText("Login")
        login_button.resize(320, 34)
        login_button.move(20, 160)

        register_button = QPushButton(self.cuadro_principal)
        register_button.setText("Registrate")
        register_button.resize(320, 34)
        register_button.move(20, 190)
        


if __name__=="__main__":
    App = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(App.exec())



