from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from estilos import *
import pickle
import sys
import os
import re


class Main(QMainWindow):
    
    basedir = os.path.dirname(__file__)
    usuarios_file = os.path.join(basedir, 'datos', 'usuarios.pkl')

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

        self.setWindowTitle("Mountain agency")
        self.setFixedSize(1280, 800)

        self.basedir = os.path.dirname(__file__)
        self.icon = QPixmap(os.path.join(self.basedir, "images/icon.png"))
        self.setWindowIcon(self.icon)

        self.setup_ui()

        #Carga de imagenes
        #Checkable remind me y forgot password
        self.icono_marcado = QPixmap(os.path.join(self.basedir, "images/marcado.png")).scaled(20,20)
        self.icono_no_marcado = QPixmap(os.path.join(self.basedir, "images/no_marcado.png")).scaled(20,20)

    def setup_ui(self):
        self.root_layout = QGridLayout()
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.root_layout.setSpacing(0)

        self.frame_izquierda = QFrame()
        self.frame_izquierda.setStyleSheet("background: #2d3250;")
        self.frame_izquierda.setContentsMargins(0, 0, 0, 0)
        self.root_layout.addWidget(self.frame_izquierda, 0, 0, 1, 1)

        self.frame_derecha = QFrame()
        self.frame_derecha.setStyleSheet("background: transparent;")
        self.frame_derecha.setContentsMargins(0, 0, 0, 0)
        self.root_layout.addWidget(self.frame_derecha, 0, 1, 1, 1)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

        self.background = QLabel(self.frame_derecha)
        image = QPixmap(os.path.join(self.basedir, "images/fondo.jpg"))
        image = image.scaled(1520, 920)
        self.background.setPixmap(image)

        self.log_in_button = QPushButton("Iniciar Sesión", self.frame_izquierda)
        self.log_in_button.setStyleSheet(estilos_sections)
        self.log_in_button.setGeometry(0, 0, 120, 40)
        self.log_in_button.setCheckable(True)
        self.log_in_button.move(70, 40)
        self.log_in_button.setChecked(True)

        self.registrarse_section = QPushButton("Registrarse", self.frame_izquierda)
        self.registrarse_section.setStyleSheet(estilos_sections)
        self.registrarse_section.setGeometry(0, 0, 120, 40)
        self.registrarse_section.setCheckable(True)
        self.registrarse_section.move(200, 40)
    

        self.log_in_button.clicked.connect(lambda: self.show_login_ui())
        self.registrarse_section.clicked.connect(lambda: self.show_register_ui())

        self.ui_iniciar_sesion = QWidget(self.frame_izquierda)
        self.ui_iniciar_sesion.setGeometry(0, 100, 640, 700)  
        self.ui_iniciar_sesion.hide()

        self.ui_registrarse = QWidget(self.frame_izquierda)  
        self.ui_registrarse.setGeometry(0, 100, 640, 700)  
        self.ui_registrarse.hide()

        self.setup_ui_register()
        self.setup_login_ui()

        self.show_login_ui()


    def setup_login_ui(self):
        # Bienvenido y Iniciar sesion para continuar
        self.bienvenido_label = QLabel(self.ui_iniciar_sesion)
        self.bienvenido_label.setText("Bienvenido!")
        self.bienvenido_label.setStyleSheet(estilo_bienvenido)
        self.bienvenido_label.move(70, 80) 

        self.iniciar_sesion_label = QLabel(self.ui_iniciar_sesion)
        self.iniciar_sesion_label.setText("Inicia sesión para continuar")
        self.iniciar_sesion_label.setStyleSheet(estilos_label2)
        self.iniciar_sesion_label.move(72, 120) 
            
        # line edits email and pass
        self.email_line_edit = QLineEdit(self.ui_iniciar_sesion)
        self.email_line_edit.setPlaceholderText("Email")
        self.email_line_edit.setStyleSheet(estilos_line_edit)
        self.email_line_edit.move(70, 170) 

        self.password_line_edit = QLineEdit(self.ui_iniciar_sesion)
        self.password_line_edit.setPlaceholderText("Password")
        self.password_line_edit.setStyleSheet(estilos_line_edit_hide)
        self.password_line_edit.move(70, 250) 

        # boton ver contraseña
        self.icon_no_pass = QPixmap(os.path.join(self.basedir, "images/no pass.png"))
        self.icon_pass = QPixmap(os.path.join(self.basedir, "images/pass.png"))

        self.view_password = QPushButton(self.ui_iniciar_sesion)
        self.view_password.setStyleSheet(estilo_boton_pass)
        self.view_password.setIcon(QIcon(self.icon_no_pass))
        self.view_password.setIconSize(QSize(25, 25))
        self.view_password.move(400, 270)
        self.view_password.setCheckable(True)  # Hace el botón comprobable
        self.view_password.setChecked(False)  # Inicialmente no comprobado
        self.view_password.clicked.connect(self.toggle_password_visibility)

        self.toggle_password_visibility()

        #Checkable remind me y forgot password
        self.icono_marcado = QPixmap(os.path.join(self.basedir, "images/marcado.png")).scaled(20,20)
        self.icono_no_marcado = QPixmap(os.path.join(self.basedir, "images/no_marcado.png")).scaled(20,20)

        self.remind_me = QCheckBox(self.ui_iniciar_sesion) 
        self.remind_me.setText(" Recordar usuario")
        self.remind_me.setStyleSheet(estilo_remind_me)
        self.remind_me.move(50, 330) 
        self.remind_me.setChecked(False)
        self.remind_me.setIcon(self.icono_no_marcado)
        self.remind_me.setIconSize(QSize(20,20))

        self.remind_me.stateChanged.connect(self.actualizar_icono)

        #Forgot_password
        self.forgot_password = QPushButton(self.ui_iniciar_sesion)
        self.forgot_password.setText("Olvide mi contraseña")
        self.forgot_password.setStyleSheet(estilos_forgot_password)
        self.forgot_password.move(312, 330) 

        # Boton iniciar sesión
        self.iniciar_sesion_button = QPushButton("Iniciar Sesión", self.ui_iniciar_sesion)
        self.iniciar_sesion_button.setStyleSheet(log_in_button)
        self.iniciar_sesion_button.move(70, 400) 

        # Iniciar sesion con redes sociales
        self.iniciar_sesion_con_label = QLabel(self.ui_iniciar_sesion)
        self.iniciar_sesion_con_label.setText("Iniciar sesion con:")
        self.iniciar_sesion_con_label.setStyleSheet(iniciar_sesion_con)
        self.iniciar_sesion_con_label.move(70, 540)  

        self.facebook_icon = QPixmap(os.path.join(self.basedir, "images/facebook.png"))
        self.google_icon = QPixmap(os.path.join(self.basedir, "images/google.png"))
        self.apple_icon = QPixmap(os.path.join(self.basedir, "images/apple.png"))

        self.facebook_button = QPushButton(self.ui_iniciar_sesion)
        self.google_button = QPushButton(self.ui_iniciar_sesion)
        self.apple_button = QPushButton(self.ui_iniciar_sesion)

        self.facebook_button.setIcon(self.facebook_icon)
        self.google_button.setIcon(self.google_icon)
        self.apple_button.setIcon(self.apple_icon)

        self.facebook_button.setIconSize(QSize(35,35))
        self.google_button.setIconSize(QSize(35,35))
        self.apple_button.setIconSize(QSize(35,35))

        self.facebook_button.move(200, 520)  
        self.google_button.move(250, 520)  
        self.apple_button.move(300, 520)  

        self.facebook_button.setStyleSheet(estilos_redes_sociales)
        self.google_button.setStyleSheet(estilos_redes_sociales)
        self.apple_button.setStyleSheet(estilos_redes_sociales)


    def setup_ui_register(self):

        # Bienvenido y Iniciar sesion para continuar
        self.unetenos_label = QLabel(self.ui_registrarse)
        self.unetenos_label.setText("Unetenos!")
        self.unetenos_label.setStyleSheet(estilo_bienvenido)
        self.unetenos_label.move(70, 30)

        self.llena_datos_label = QLabel(self.ui_registrarse)
        self.llena_datos_label.setText("Llena los siguientes datos")
        self.llena_datos_label.setStyleSheet(estilos_label2)
        self.llena_datos_label.move(72, 70)



        # line edits email and pass
        self.name_line_edit = QLineEdit(self.ui_registrarse)
        self.name_line_edit.setPlaceholderText("Nombre")
        self.name_line_edit.setStyleSheet(registrarse_name)
        self.name_line_edit.move(70, 110)         

        self.last_name_line_edit = QLineEdit(self.ui_registrarse)
        self.last_name_line_edit.setPlaceholderText("Apellido")
        self.last_name_line_edit.setStyleSheet(registrarse_name)
        self.last_name_line_edit.move(265, 110) 

        self.email_register_line_edit = QLineEdit(self.ui_registrarse)
        self.email_register_line_edit.setPlaceholderText("Email")
        self.email_register_line_edit.setStyleSheet(registrarse_line_edit)
        self.email_register_line_edit.move(70, 180) 

        self.password_register_line_edit = QLineEdit(self.ui_registrarse)
        self.password_register_line_edit.setPlaceholderText("Password")
        self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide)
        self.password_register_line_edit.move(70, 250)

        self.password_confirm_line_edit = QLineEdit(self.ui_registrarse)
        self.password_confirm_line_edit.setPlaceholderText("Verify password")
        self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide)
        self.password_confirm_line_edit.move(70, 320)


        self.name_line_edit.textChanged.connect(self.reset_name_style)
        self.last_name_line_edit.textChanged.connect(self.reset_lastname_style)
        self.email_register_line_edit.textChanged.connect(self.reset_mail_style)
        self.password_register_line_edit.textChanged.connect(self.reset_password_styles)
        self.password_confirm_line_edit.textChanged.connect(self.reset_password_styles)



        # Ver contraseña false
        self.toggle_password_register_visibility()



        # Boton registrarse
        self.registrarse_button_form = QPushButton("Registrarse", self.ui_registrarse)
        self.registrarse_button_form.setStyleSheet(log_in_button)
        self.registrarse_button_form.move(70, 400)
        self.registrarse_button_form.clicked.connect(self.verificar_registracion)

        # Iniciar sesion con redes sociales
        self.iniciar_sesion_con_label = QLabel(self.ui_registrarse)
        self.iniciar_sesion_con_label.setText("Iniciar sesion con:")
        self.iniciar_sesion_con_label.setStyleSheet(iniciar_sesion_con)
        self.iniciar_sesion_con_label.move(70, 540)

        self.facebook_icon = QPixmap(os.path.join(self.basedir, "images/facebook.png"))
        self.google_icon = QPixmap(os.path.join(self.basedir, "images/google.png"))
        self.apple_icon = QPixmap(os.path.join(self.basedir, "images/apple.png"))

        self.facebook_button = QPushButton(self.ui_registrarse)
        self.google_button = QPushButton(self.ui_registrarse)
        self.apple_button = QPushButton(self.ui_registrarse)

        self.facebook_button.setIcon(self.facebook_icon)
        self.google_button.setIcon(self.google_icon)
        self.apple_button.setIcon(self.apple_icon)

        self.facebook_button.setIconSize(QSize(35,35))
        self.google_button.setIconSize(QSize(35,35))
        self.apple_button.setIconSize(QSize(35,35))

        self.facebook_button.move(200, 520)
        self.google_button.move(250, 520)
        self.apple_button.move(300, 520)

        self.facebook_button.setStyleSheet(estilos_redes_sociales)
        self.google_button.setStyleSheet(estilos_redes_sociales)
        self.apple_button.setStyleSheet(estilos_redes_sociales)
        

    def show_login_ui(self):
        self.ui_iniciar_sesion.show()
        self.ui_registrarse.hide()
        self.log_in_button.setChecked(True)
        self.registrarse_section.setChecked(False)
        if self.log_in_button.isChecked():
            self.registrarse_section.setCheckable(True)
            self.registrarse_section.setStyleSheet(estilos_sections)
            self.log_in_button.setStyleSheet(estilos_sections + "QPushButton {border-bottom: 5px solid #ffb17a; color: white;}")
            self.log_in_button.setCheckable(False)

    def show_register_ui(self):
        self.ui_iniciar_sesion.hide()
        self.ui_registrarse.show()
        self.log_in_button.setChecked(False)
        self.registrarse_section.setChecked(True)
        if self.registrarse_section.isChecked():
            self.log_in_button.setCheckable(True)
            self.log_in_button.setStyleSheet(estilos_sections)
            self.registrarse_section.setStyleSheet(estilos_sections + "QPushButton {border-bottom: 5px solid #ffb17a; color: white;}")
            self.registrarse_section.setCheckable(False)



#################
#Register methods
    def verificar_registracion(self):

        self.verify_name()
        self.verify_last_name()
        self.verify_email()
        self.verify_password()

    def verify_password(self):

        password = self.password_register_line_edit.text()
        confirm_password = self.password_confirm_line_edit.text()

        if password != confirm_password or (not password and not confirm_password) :
            self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
            self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
        else:
            if len(password) < 6 or len(password) > 12:
                self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
            elif not any([letra.isdigit() for letra in password]):
                self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
            elif not any([letra.islower() for letra in password]):
                self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
            elif not any([letra.isupper() for letra in password]):
                self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)



    def verify_email(self):
        email = self.email_register_line_edit.text()

        # Patrón de expresión regular para validar el formato de un email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Utilizar re.match para verificar el formato del email
        if not re.match(patron, email):
            self.email_register_line_edit.setStyleSheet(email_register_fail)


 

    def reset_password_styles(self):
        self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide)
        self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide)

    def reset_name_style(self):
        self.name_line_edit.setStyleSheet(registrarse_name)

    def reset_lastname_style(self):
        self.last_name_line_edit.setStyleSheet(registrarse_name)

    def reset_mail_style(self):
        self.email_register_line_edit.setStyleSheet(registrarse_line_edit)
        

    def toggle_password_register_visibility(self):
        # Oculta la contraseña
        self.password_confirm_line_edit.setEchoMode(QLineEdit.Password)
        self.password_register_line_edit.setEchoMode(QLineEdit.Password)

    def verify_name(self):
        name = self.name_line_edit.text()
        if not name or len(name) <= 2:
            self.name_line_edit.setStyleSheet(names_registration_fail)

    def verify_last_name(self):
        lastname = self.last_name_line_edit.text()
        if not lastname or len(lastname) <= 2:
            self.last_name_line_edit.setStyleSheet(names_registration_fail)
    

###############
#Log in methods
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


###########
#UI methods
    def guardar_usuarios(self):
    # Guardar usuarios en el archivo
        with open(self.usuarios_file, 'wb') as f:
            pickle.dump(self.usuarios, f)

    def cerrarEvent(self, event):
        # Guardar usuarios al cerrar la ventana
        self.guardar_usuarios()
        event.accept()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
