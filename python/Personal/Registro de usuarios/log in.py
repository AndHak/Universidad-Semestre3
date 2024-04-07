from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from estilos import *
import pickle
import sys
import os


class Main(QMainWindow):
    
    basedir = os.path.dirname(__file__)
    usuarios_file = os.path.join(basedir, 'datos', 'usuarios.pkl')

    images = ["apple.png", "facebook.png", "fondo.png", "google.png", "no pass.png", "pass.png"]
    colores = {
        'blanco': "#ffffff",
        'azul_claro': "#676fgd",
        'azul_medio': "#424769",
        'azul_oscuro': "#2d3250",
        'tomate': "#fgb17a",
    }
    usuarios = {}
    
    def __init__(self):
        super().__init__()

        # Cargar usuarios si existe el archivo
        if os.path.exists(self.usuarios_file):
            with open(self.usuarios_file, 'rb') as f:
                self.usuarios = pickle.load(f)
        else:
            self.usuarios = {}



        self.setWindowTitle("Mountain agency")
        self.setFixedSize(1280, 800)

        # Layout principal de la ventana
        self.root_layout = QGridLayout()
        self.root_layout.setContentsMargins(0, 0, 0, 0)  # Establecer márgenes a 0 píxeles

        # Layout principal de la ventana
        self.root_layout = QGridLayout()
        self.root_layout.setContentsMargins(0, 0, 0, 0)  # Establecer márgenes a 0 píxeles
        self.root_layout.setSpacing(0)  # Establecer espacio entre widgets a 0 píxeles

        # Crear y configurar el frame izquierdo
        self.frame_izquierda = QFrame()
        self.frame_izquierda.setStyleSheet(f"background: {self.colores['azul_oscuro']}") 
        self.frame_izquierda.setContentsMargins(0, 0, 0, 0)  # Establecer márgenes a 0 píxeles
        self.root_layout.addWidget(self.frame_izquierda, 0, 0, 1, 1)  # Añadir a la fila 0, columna 0

        # Crear y configurar el frame derecho
        self.frame_derecha = QFrame()
        self.frame_derecha.setStyleSheet("background: transparent")  
        self.frame_derecha.setContentsMargins(0, 0, 0, 0)  # Establecer márgenes a 0 píxeles
        self.root_layout.addWidget(self.frame_derecha, 0, 1, 1, 1)  # Añadir a la fila 0, columna 1

        # Establecer el layout principal de la ventana
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

        # Establecer la imagen de fondo en el frame derecho
        self.background = QLabel(self.frame_derecha)
        image = QPixmap(os.path.join(self.basedir, "images/fondo.jpg"))
        image = image.scaled(1520, 920)
        self.background.setPixmap(image)

        # Botones
        self.log_in_button = QPushButton("Iniciar Sesion", self.frame_izquierda)
        self.log_in_button.setStyleSheet(estilos_sections)
        self.log_in_button.setGeometry(0,0,120,40)
        self.log_in_button.setCheckable(True)
        self.log_in_button.move(70,40)

        self.registrarse_section = QPushButton("Registrarse", self.frame_izquierda)
        self.registrarse_section.setStyleSheet(estilos_sections)
        self.registrarse_section.setGeometry(0,0,120,40)
        self.registrarse_section.setCheckable(True)
        self.registrarse_section.move(200, 40)


        # Conectar el botón a la función de inicio de sesión
        self.log_in_button.clicked.connect(lambda: self.iniciar_sesion())
        self.registrarse_section.clicked.connect(lambda: self.registrarse())



        # Bienvenido y Iniciar sesion para continuar
        self.bienvenido_label = QLabel(self.frame_izquierda)
        self.bienvenido_label.setText("Bienvenido!")
        self.bienvenido_label.setStyleSheet(estilo_bienvenido)
        self.bienvenido_label.move(70, 180)

        self.iniciar_sesion_label = QLabel(self.frame_izquierda)
        self.iniciar_sesion_label.setText("Inicia sesión para continuar")
        self.iniciar_sesion_label.setStyleSheet(estilos_label2)
        self.iniciar_sesion_label.move(72, 220)
        
        # line edits email and pass
        self.email_line_edit = QLineEdit(self.frame_izquierda)
        self.email_line_edit.setPlaceholderText("Email")
        self.email_line_edit.setStyleSheet(estilos_line_edit)
        self.email_line_edit.move(70, 270)

        self.password_line_edit = QLineEdit(self.frame_izquierda)
        self.password_line_edit.setPlaceholderText("Password")
        self.password_line_edit.setStyleSheet(estilos_line_edit_hide)
        self.password_line_edit.move(70, 350)



        # boton ver contraseña
        self.icon_no_pass = QPixmap(os.path.join(self.basedir, "images/no pass.png"))
        self.icon_pass = QPixmap(os.path.join(self.basedir, "images/pass.png"))

        self.view_password = QPushButton(self.frame_izquierda)
        self.view_password.setStyleSheet(estilo_boton_pass)
        self.view_password.setIcon(QIcon(self.icon_no_pass))
        self.view_password.setIconSize(QSize(25, 25))
        self.view_password.move(400, 370)
        self.view_password.setCheckable(True)  # Hace el botón comprobable
        self.view_password.setChecked(False)  # Inicialmente no comprobado
        self.view_password.clicked.connect(self.toggle_password_visibility)

        self.toggle_password_visibility()
        self.iniciar_sesion()



        #Checkable remind me y forgot password
        self.icono_marcado = QPixmap(os.path.join(self.basedir, "images/marcado.png"))
        self.icono_no_marcado = QPixmap(os.path.join(self.basedir, "images/no marcado.png"))

        self.remind_me = QCheckBox(self.frame_izquierda) 
        self.remind_me.setText("Recordar usuario")
        self.remind_me.setStyleSheet(estilo_remind_me)
        self.remind_me.move(70, 430)
        self.remind_me.setChecked(False)
        self.remind_me.setIcon(self.icono_no_marcado)
        self.remind_me.setIconSize(QSize(20,20))


        self.remind_me.stateChanged.connect(self.actualizar_icono)





        # Boton iniciar sesión
        self.iniciar_sesion_button = QPushButton("Iniciar Sesión", self.frame_izquierda)
        self.iniciar_sesion_button.setStyleSheet(log_in_button)

        self.iniciar_sesion_button.move(70, 500)



    
    def actualizar_icono(self):
        if self.remind_me.isChecked():
            self.remind_me.setIcon(self.icono_marcado)
        else:
            self.remind_me.setIcon(self.icono_no_marcado)




    def toggle_password_visibility(self):
        # Alterna la visibilidad de la contraseña basado en el estado del botón
        if self.view_password.isChecked():
            # Muestra la contraseña
            self.password_line_edit.setEchoMode(QLineEdit.Normal)
            self.view_password.setIcon(QIcon(self.icon_pass))
        else:
            # Oculta la contraseña
            self.password_line_edit.setEchoMode(QLineEdit.Password)
            self.view_password.setIcon(QIcon(self.icon_no_pass))
            




    
       
       
       
       
       
       
       
       
       
       
       





    def guardar_usuarios(self):
    # Guardar usuarios en el archivo
        with open(self.usuarios_file, 'wb') as f:
            pickle.dump(self.usuarios, f)

    def cerrarEvent(self, event):
        # Guardar usuarios al cerrar la ventana
        self.guardar_usuarios()
        event.accept()


    def registrarse(self):
        if self.registrarse_section.isChecked():
            self.log_in_button.setCheckable(True)
            self.log_in_button.setStyleSheet(estilos_sections)
            self.registrarse_section.setStyleSheet(estilos_sections + "QPushButton {border-bottom: 5px solid #ffb17a; color: white;}")
            self.registrarse_section.setCheckable(False)
        

    def iniciar_sesion(self):
        self.log_in_button.setChecked(True)
        if self.log_in_button.isChecked():
            self.registrarse_section.setCheckable(True)
            self.registrarse_section.setStyleSheet(estilos_sections)
            self.log_in_button.setStyleSheet(estilos_sections + "QPushButton {border-bottom: 5px solid #ffb17a; color: white;}")
            self.log_in_button.setCheckable(False)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
