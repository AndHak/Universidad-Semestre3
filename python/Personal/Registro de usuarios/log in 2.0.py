from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
from estilos import *
from usuario import *
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
    
    def __init__(self):
        super().__init__()
        QCoreApplication.instance().aboutToQuit.connect(self.guardar_datos_al_cerrar)
        # Definir la ruta del archivo de usuarios
        self.usuarios_file = os.path.join(self.basedir, 'datos', 'usuarios_base_data.pkl')

        # Cargar los datos al iniciar la aplicación si el archivo existe
        if os.path.exists(self.usuarios_file):
            with open(self.usuarios_file, 'rb') as archivo:
                self.usuarios_base_data = pickle.load(archivo)
        else:
            self.usuarios_base_data = {}


        self.user = Usuario("","","","")

        self.setWindowTitle("Mountain agency")
        self.setFixedSize(1280, 800)

        self.basedir = os.path.dirname(__file__)
        self.icon = QPixmap(os.path.join(self.basedir, "images/icon.png"))
        self.setWindowIcon(self.icon)

        self.setup_ui()

        self.notify_sound = QSoundEffect()
        self.notify_sound.setSource(QUrl.fromLocalFile(os.path.join(self.basedir, "sounds/notify.wav")))




        

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
        self.email_line_edit.textChanged.connect(self.reset_email_log_in_style)

        self.password_line_edit = QLineEdit(self.ui_iniciar_sesion)
        self.password_line_edit.setPlaceholderText("Password")
        self.password_line_edit.setStyleSheet(estilos_line_edit_hide)
        self.password_line_edit.move(70, 250) 
        self.password_line_edit.textChanged.connect(self.reset_pass_log_in_style)

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
        self.iniciar_sesion_button.clicked.connect(self.log_in_user)

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



#################
#Register methods
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


    def verificar_registracion(self):
        if not self.name_line_edit.text() and not self.email_register_line_edit.text() and not self.last_name_line_edit.text() \
            and not self.password_register_line_edit.text() and not self.password_confirm_line_edit.text():
            message = "Llene los campos vacios"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            self.email_register_line_edit.setStyleSheet(email_register_fail)
            self.last_name_line_edit.setStyleSheet(names_registration_fail)
            self.name_line_edit.setStyleSheet(names_registration_fail)
            self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
            self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
            return

        self.verify_name()
        if self.verify_name:
            self.verify_last_name()
            if self.verify_last_name:
                self.verify_email()
                if self.verify_email:
                    self.verify_password()
                    if self.verify_password:
                        if all([self.verify_password(), self.verify_email(), self.verify_name(), self.verify_last_name()]):
                            self.registrar_usuario()

    def verify_password(self):
        password = self.password_register_line_edit.text()
        confirm_password = self.password_confirm_line_edit.text()

        if password != confirm_password or (not password and not confirm_password) :
            self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
            self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
            
            message = "Las contraseñas no coinciden"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False
            
        else:
            if len(password) < 6 or len(password) > 16:
                self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                message = "Escriba una contraseña entre 6 y 16 caracteres"
                self.mostrar_notificacion(message, estilo_notificacion_fail)
                return False
            
            elif not any([letra.isdigit() for letra in password]):
                self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                message = "La contraseña debe tener por lo menos un numero"
                self.mostrar_notificacion(message, estilo_notificacion_fail)
                return False
            
            elif not any([letra.islower() for letra in password]):
                self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                message = "La contraseña debe tener al menos una letra minúscula"
                self.mostrar_notificacion(message, estilo_notificacion_fail)
                return False
            
            elif not any([letra.isupper() for letra in password]):
                self.password_register_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                self.password_confirm_line_edit.setStyleSheet(registrarse_line_edit_hide_fail)
                message = "La contraseña debe tener al menos una letra mayúscula"
                self.mostrar_notificacion(message, estilo_notificacion_fail)
                return False
    
            return True     

    def verify_email(self):
        email = self.email_register_line_edit.text()

        # Patrón de expresión regular para validar el formato de un email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Utilizar re.match para verificar el formato del email
        if not re.match(patron, email):
            self.email_register_line_edit.setStyleSheet(email_register_fail)
            message = "El email no es válido"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False
        
        return True

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

        # Verificar si el nombre es demasiado corto
        if not name or len(name) <= 2:
            self.name_line_edit.setStyleSheet(names_registration_fail)
            message = "Nombre demasiado corto"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        # Verificar si el nombre es demasiado largo
        if len(name) > 30:
            self.name_line_edit.setStyleSheet(names_registration_fail)
            message = "Nombre demasiado largo"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        # Verificar si el nombre tiene más de dos palabras
        name_parts = name.split()
        if len(name_parts) > 2:
            self.name_line_edit.setStyleSheet(names_registration_fail)
            message = "Máximo dos nombres"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        # Verificar si el nombre contiene caracteres no permitidos
        if not re.match("^[a-zA-Z\\s]+$", name):
            self.name_line_edit.setStyleSheet(names_registration_fail)
            message = "El nombre no puede incluir números o caracteres especiales"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        return True
            
            

    def verify_last_name(self):
        lastname = self.last_name_line_edit.text()

        # Verificar si el apellido es demasiado corto
        if not lastname or len(lastname) <= 2:
            self.last_name_line_edit.setStyleSheet(names_registration_fail)
            message = "Apellido demasiado corto"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        # Verificar si el apellido es demasiado largo
        if len(lastname) > 30:
            self.last_name_line_edit.setStyleSheet(names_registration_fail)
            message = "Apellido demasiado largo"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        # Verificar si el apellido tiene más de una palabra
        lastname_parts = lastname.split()
        if len(lastname_parts) > 2:
            self.last_name_line_edit.setStyleSheet(names_registration_fail)
            message = "El apellido debe ser una sola palabra"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        # Verificar si el apellido contiene números o caracteres especiales
        if not re.match("^[a-zA-ZÀ-ÿ\\s]+$", lastname):
            self.last_name_line_edit.setStyleSheet(names_registration_fail)
            message = "El apellido no puede incluir números o caracteres especiales"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        return True

    def registrar_usuario(self):
        email = self.email_register_line_edit.text().lower()
        password = self.password_register_line_edit.text()
        name = self.name_line_edit.text().title()
        lastname = self.last_name_line_edit.text().title()


        self.usuarios_base_data[email] = Usuario(name, lastname, email, password)

        message = "Usuario registrado con éxito"
        self.mostrar_notificacion(message, estilo_notificacion_succes)

        
    

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

    def reset_email_log_in_style(self):
        self.email_line_edit.setStyleSheet(estilos_line_edit)

    def reset_pass_log_in_style(self):
        self.password_line_edit.setStyleSheet(estilos_line_edit_hide)

    def log_in_user(self):
        # Inicializar la variable usuario_encontrado fuera del método
        self.usuario_encontrado = None

        password = self.password_line_edit.text()
        email = self.email_line_edit.text()

        if not password or not email:
            # Mostrar notificación si faltan campos
            self.password_line_edit.setStyleSheet(login_fail_pass)
            self.email_line_edit.setStyleSheet(login_fail_mail)
            message = "Llene los campos vacíos"
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        # Llamar a las funciones de verificación
        if self.verify_log_in_mail(email) and self.verify_log_in_pass(password):
            self.iniciar_sesion_succes()

    def verify_log_in_mail(self, email):
        if self.usuarios_base_data:
            for id_email, objeto in self.usuarios_base_data.items():
                if id_email == email:
                    self.usuario_encontrado = objeto
                    return True
            # Mostrar notificación si el usuario no existe
            message = "El usuario no existe"
            self.email_line_edit.setStyleSheet(login_fail_mail)
            self.mostrar_notificacion(message, estilo_notificacion_fail)
            return False

        # Mostrar notificación si no hay usuarios registrados
        message = "No hay usuarios registrados"
        self.mostrar_notificacion(message, estilo_notificacion_fail)
        return False

    def verify_log_in_pass(self, password):
        if self.usuario_encontrado:
            if self.email_line_edit.text() == self.usuario_encontrado.email:
                if password == self.usuario_encontrado.password:
                    return True
                # Mostrar notificación si la contraseña es incorrecta
                message = "Contraseña incorrecta"
                self.mostrar_notificacion(message, estilo_notificacion_fail)
                return False

        # Mostrar notificación si el usuario no existe
        message = "El usuario no existe"
        self.mostrar_notificacion(message, estilo_notificacion_fail)
        return False

    def iniciar_sesion_succes(self):
        message = "Inicio de sesión exitoso"
        self.mostrar_notificacion(message, estilo_notificacion_succes)









###########
#UI methods
    def guardar_datos_al_cerrar(self):
        # Guardar el diccionario de usuarios al cerrar la aplicación
        with open(self.usuarios_file, 'wb') as archivo:
            pickle.dump(self.usuarios_base_data, archivo)



    def mostrar_notificacion(self, message, estilo):

        # Verificar si hay una notificación anterior y borrarla si es necesario
        if hasattr(self, 'notify_fail') and self.notify_fail.isVisible():
            self.notify_fail.close()

        # Resto del código para mostrar la notificación
        self.notify_fail = QWidget(self.frame_derecha)
        effect = QGraphicsOpacityEffect(self.notify_fail)
        self.notify_fail.setGraphicsEffect(effect)
        self.notify_fail.setStyleSheet(estilo)
        self.notify_fail.resize(160, 110)

        label = QLabel(message, self.notify_fail)
        label.setStyleSheet(message_notify)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(QRect(0, 0, self.notify_fail.width(), self.notify_fail.height()))
        label.setWordWrap(True)  # Ajuste automático del texto

        self.animation = QPropertyAnimation(self.notify_fail, b"pos")
        self.animation.setStartValue(QPoint(440, 700))
        self.animation.setEndValue(QPoint(440, 650))
        self.animation.setDuration(500)

        self.animation2 = QPropertyAnimation(effect, b"opacity")
        self.animation2.setStartValue(0)
        self.animation2.setEndValue(0.8)
        self.animation2.setDuration(1000)

        self.animation_group = QParallelAnimationGroup()
        self.animation_group.addAnimation(self.animation)
        self.animation_group.addAnimation(self.animation2)

        # Crear un temporizador para ocultar la notificación después de 3 segundos
        self.timer_hide = QTimer()
        self.timer_hide.setSingleShot(True)  # El temporizador se detendrá después de ejecutarse una vez
        self.timer_hide.timeout.connect(self.ocultar_notificacion)  # Conectar la señal timeout al método ocultar_notificacion

        # Iniciar temporizador para ocultar la notificación después de 3 segundos
        self.timer_hide = QTimer()
        self.timer_hide.setSingleShot(True)  # El temporizador se detendrá después de ejecutarse una vez
        self.timer_hide.timeout.connect(self.ocultar_notificacion)  # Conectar la señal timeout al método ocultar_notificacion
        self.timer_hide.start(4000)  # 3000 ms = 3 segundos

        self.animation_group.start()
        self.notify_fail.show()
        self.notify_sound.play()

    def ocultar_notificacion(self):

        self.animation2_reverse = QPropertyAnimation(self.notify_fail.graphicsEffect(), b"opacity")
        self.animation2_reverse.setStartValue(0.8)
        self.animation2_reverse.setEndValue(0)
        self.animation2_reverse.setDuration(2000)

        self.animation_group_reverse = QParallelAnimationGroup()
        self.animation_group_reverse.addAnimation(self.animation2_reverse)
        self.animation_group_reverse.finished.connect(self.notify_fail.hide)

        self.animation_group_reverse.start()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
