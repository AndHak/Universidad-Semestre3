from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import re
import os
import sys


class MainWindow(QWidget):
    dic_usuarios = {}
    def __init__(self):
        super().__init__()


        self.basedir = os.path.dirname(__file__)
        
        # Configuración de la ventana principal
        self.setWindowTitle("My travel app login")
        self.setMinimumSize(400,600)

        self.layout_principal = QHBoxLayout()
        self.layout_principal.setContentsMargins(10,0,0,0)
       
        #self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)  # Fondo transparente

        
        
        self.setLayout(self.layout_principal) 

        self.login_singup()
        self.imagen()

        

    def login_singup(self):
        self.layout_widgets = QStackedLayout()
        self.login_widget = QWidget()
        self.singup_widget = QWidget()

        #intrefaz login
        login = QVBoxLayout()

        label_inicio = QLabel("Inicia Sesion!")
        label_inicio.setFont(QFont("Unispace", 30))
        
        qform_login = QFormLayout()
        self.button_registro_interfaz = QPushButton("Registrate")
        self.button_registro_interfaz.setFixedSize(100,30)
        qform_login.addRow("¿No tienes una cuenta?", self.button_registro_interfaz)
        self.button_registro_interfaz.clicked.connect(lambda : self.layout_widgets.setCurrentWidget(self.singup_widget))
        qform_login.setContentsMargins(0,0,0,0)

        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuario")
        self.usuario.setFixedSize(300,30)

        qhbox = QHBoxLayout()

        self.contraseña = QLineEdit()
        self.contraseña.setPlaceholderText("Contraseña")

        self.ver_contraseña = QPushButton()
        icon = QIcon(os.path.join(self.basedir, "img_trabajos", "ojo-cerrado-morado.png"))
        self.ver_contraseña.setIcon(icon)
        self.contraseña.setEchoMode(QLineEdit.EchoMode.Password)
        self.ver_contraseña.pressed.connect(lambda: self.mirar_password(self.contraseña, self.ver_contraseña))
        self.ver_contraseña.released.connect(lambda: self.ocultar_password(self.contraseña, self.ver_contraseña))
        # self.ver_contraseña.setStyleSheet("background-color: #85C1E9;")


        qhbox.addWidget(self.contraseña)
        qhbox.addWidget(self.ver_contraseña)

        self.button_iniciar_sesion = QPushButton("Iniciar Sesion")
        self.button_iniciar_sesion.clicked.connect(self.validar_login)
        
        login.addWidget(label_inicio)
        login.addLayout(qform_login)
        login.addWidget(self.usuario)
        login.addSpacing(4)
        login.addLayout(qhbox)
        login.addSpacing(10)
        login.addWidget(self.button_iniciar_sesion)
        login.setContentsMargins(0,140,0,160)

        self.login_widget.setLayout(login)

        #interfaz registro
        singup = QVBoxLayout()

        label_registro = QLabel("Registrate!")
        label_registro.setFont(QFont("Unispace", 30))

        qform_registro = QFormLayout()
        self.button_iniciar_sesion_interfaz = QPushButton("Inicia Sesion")
        self.button_iniciar_sesion_interfaz.setFixedSize(100,30)
        qform_registro.addRow("¿Ya tienes una cuenta?", self.button_iniciar_sesion_interfaz)
        self.button_iniciar_sesion_interfaz.clicked.connect(lambda: self.layout_widgets.setCurrentWidget(self.login_widget))
        qform_registro.setContentsMargins(0,0,0,0)

        qhbox_registro = QHBoxLayout()

        self.nombre_registro = QLineEdit()
        self.nombre_registro.setPlaceholderText("Nombre")

        self.apellido_registro = QLineEdit()
        self.apellido_registro.setPlaceholderText("Apellido")

        qhbox_registro.addWidget(self.nombre_registro)
        qhbox_registro.addWidget(self.apellido_registro)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email (recuerda este sera tu usuario)")

        qhbox_contra = QHBoxLayout()
        self.contraseña_registro = QLineEdit()
        self.contraseña_registro.setPlaceholderText("Contraseña")
        self.contraseña_registro.setEchoMode(QLineEdit.EchoMode.Password)

        self.ver_contraseña_contra = QPushButton()
        icon_contra = QIcon(os.path.join(self.basedir, "img_trabajos", "ojo-cerrado-morado.png"))
        self.ver_contraseña_contra.setIcon(icon_contra)
        self.ver_contraseña_contra.pressed.connect(lambda: self.mirar_password(self.contraseña_registro, self.ver_contraseña_contra))
        self.ver_contraseña_contra.released.connect(lambda: self.ocultar_password(self.contraseña_registro, self.ver_contraseña_contra))

        qhbox_contra.addWidget(self.contraseña_registro)
        qhbox_contra.addWidget(self.ver_contraseña_contra)

        qhbox_contra_veri = QHBoxLayout()
        self.contraseña_registro_verificacion = QLineEdit()
        self.contraseña_registro_verificacion.setPlaceholderText("Repite tu Contraseña")
        self.contraseña_registro_verificacion.setEchoMode(QLineEdit.EchoMode.Password)
        self.ver_contraseña_contra_veri = QPushButton()
        icon_veri = QIcon(os.path.join(self.basedir, "img_trabajos", "ojo-cerrado-morado.png"))
        self.ver_contraseña_contra_veri.setIcon(icon_veri)
        self.ver_contraseña_contra_veri.pressed.connect(lambda: self.mirar_password(self.contraseña_registro_verificacion, self.ver_contraseña_contra_veri))
        self.ver_contraseña_contra_veri.released.connect(lambda: self.ocultar_password(self.contraseña_registro_verificacion, self.ver_contraseña_contra_veri))

        qhbox_contra_veri.addWidget(self.contraseña_registro_verificacion)
        qhbox_contra_veri.addWidget(self.ver_contraseña_contra_veri)


        self.button_registrarse = QPushButton("Registrarse")
        self.button_registrarse.clicked.connect(self.validar_registro)

        singup.addWidget(label_registro)
        singup.addLayout(qform_registro)
        singup.addLayout(qhbox_registro)
        singup.addSpacing(5)
        singup.addWidget(self.email)
        singup.addSpacing(5)
        singup.addLayout(qhbox_contra)
        singup.addSpacing(5)
        singup.addLayout(qhbox_contra_veri)
        singup.addSpacing(15)
        singup.addWidget(self.button_registrarse)
        singup.setContentsMargins(0,100,0,130)

        self.singup_widget.setLayout(singup)

        self.layout_widgets.addWidget(self.login_widget)
        self.layout_widgets.addWidget(self.singup_widget)

        self.layout_principal.addLayout(self.layout_widgets)

    def imagen(self):
        label = QLabel()
        
        imagen = QPixmap(os.path.join(self.basedir, "img_trabajos", "avion.jpg"))
        label.setPixmap(imagen.scaled(imagen.size()*0.5))
        label.setStyleSheet("border: none;")

        self.layout_principal.addWidget(label)
    
    def mirar_password(self, line_edit, button):
        line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        icon = QIcon(os.path.join(self.basedir, "img_trabajos", "ojo-abierto-morado.png"))
        button.setIcon(icon)
    
    def ocultar_password(self, line_edit, button):
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        icon = QIcon(os.path.join(self.basedir, "img_trabajos", "ojo-cerrado-morado.png"))
        button.setIcon(icon)

    def validar_login(self):
        usuario = self.usuario.text().strip()
        contraseña = self.contraseña.text().strip()

        if usuario and contraseña:
            if usuario in self.dic_usuarios:
                password = self.dic_usuarios[usuario][2]  # Obtener la contraseña almacenada
                if contraseña == password:
                    QMessageBox.information(self, "Login Exitoso", "Has iniciado sesión correctamente.")
                    self.usuario.clear()
                    self.contraseña.clear()
                    self.usuario.setStyleSheet("border-color: gray;")
                    self.contraseña.setStyleSheet("border-color: gray;")
                    #implementacion para la pagina principal

                else:
                    self.mostrar_warning("Contraseña incorrecta.")
                    self.contraseña.setStyleSheet("border-color: red;")
            else:
                self.mostrar_warning("El usuario no existe.")
                self.usuario.setStyleSheet("border-color: red;")
        else:
            if not usuario:
                self.usuario.setStyleSheet("border-color: red;")
                self.mostrar_warning("El campo de usuario no puede estar vacío.")
            if not contraseña:
                self.contraseña.setStyleSheet("border-color: red;")
                self.mostrar_warning("El campo de contraseña no puede estar vacío.")

    def validar_registro(self):
        nombre = self.validar_nombre_registro(self.nombre_registro)
        apellido = self.validar_apellido_registro(self.apellido_registro)
        email = self.validar_email_registro(self.email)
        password = self.validar_password_registro(self.contraseña_registro)
        validacion_password = self.validar_password_registro(self.contraseña_registro_verificacion)

        if nombre and apellido and email:
            if password == validacion_password:
                msg_box = QMessageBox(self)
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Cuenta creada con éxito.")
                msg_box.setWindowTitle("Cuenta Creada")

                # Cambiar el tamaño del QMessageBox
                msg_box.resize(300, 200)

                # Cambiar el estilo del botón
                msg_box.setStyleSheet("""
                    QPushButton {
                        min-width: 30px;
                        min-height: 15px;
                    }
                """)
                self.dic_usuarios[email] = [nombre, apellido, password]
                print(self.dic_usuarios)
                ok = msg_box.exec()
                if ok:
                    self.layout_widgets.setCurrentWidget(self.login_widget)
                self.nombre_registro.clear()
                self.apellido_registro.clear()
                self.email.clear()
                self.contraseña_registro.clear()
                self.contraseña_registro_verificacion.clear()
                self.nombre_registro.setStyleSheet("border-color: gray;")
                self.apellido_registro.setStyleSheet("border-color: gray;")
                self.email.setStyleSheet("border-color: gray;")
                self.contraseña_registro.setStyleSheet("border-color: gray;")
                self.contraseña_registro_verificacion.setStyleSheet("border-color: gray;")
            else:
                self.mostrar_warning("Verifica que tus contraseñas sean iguales")
                self.contraseña_registro.setStyleSheet("border-color: red;")
                self.contraseña_registro_verificacion.setStyleSheet("border-color: red;")
            
    
    def validar_nombre_registro(self, nombre_line_edit):
        nombre = nombre_line_edit.text().strip()
        if not nombre:
            self.mostrar_warning("El nombre no puede estar vacío.")
            nombre_line_edit.setStyleSheet("border-color: red;")
            return False
        elif not re.match(r'^[a-zA-Z\s]+$', nombre):
            self.mostrar_warning("El nombre no puede contener caracteres especiales ni dígitos.")
            nombre_line_edit.setStyleSheet("border-color: red;")
            return False
        elif len(nombre.split()) > 3:
            self.mostrar_warning("No puede haber más de tres nombres.")
            nombre_line_edit.setStyleSheet("border-color: red;")
            return False
        else:
            nombre = ' '.join(nombre.split()).title()
            nombre_line_edit.setText(nombre)
            nombre_line_edit.setStyleSheet("border-color: green;")

            return nombre
    
    def validar_apellido_registro(self, apellido_line_edit):
        apellido = apellido_line_edit.text().strip()
        if not apellido:
            self.mostrar_warning("El apellido no puede estar vacío.")
            apellido_line_edit.setStyleSheet("border-color: red;")
            return False
        elif not re.match(r'^[a-zA-Z\s]+$', apellido):
            self.mostrar_warning("El apellido no puede contener caracteres especiales ni dígitos.")
            apellido_line_edit.setStyleSheet("border-color: red;")
            return False
        elif len(apellido.split()) > 3:
            self.mostrar_warning("No puede haber más de tres apellidos.")
            apellido_line_edit.setStyleSheet("border-color: red;")
            return False
        else:
            apellido = ' '.join(apellido.split()).title()
            apellido_line_edit.setText(apellido)
            apellido_line_edit.setStyleSheet("border-color: green;")
            return apellido

    def validar_email_registro(self, email_line_edit):
        email = email_line_edit.text()
        if email.strip() == "":
            self.mostrar_warning("El email no puede estar vacio.")
            email_line_edit.setStyleSheet("border-color: red;")
            return False
        
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email.strip()):
            self.mostrar_warning("Debe colocar un email válido.")
            email_line_edit.setStyleSheet("border-color: red;")
            return False
        email_line_edit.setStyleSheet("border-color: green;")
        return email
            
    def validar_password_registro(self, password_line_edit):
        password = password_line_edit.text()
        if password.strip() == "":
            self.mostrar_warning("La contraseña no puede estar vacía.")
            password_line_edit.setStyleSheet("border-color: red;")
            return False

        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(password_regex, password.strip()):
            self.mostrar_warning("La contraseña debe contener al menos 8 caracteres, incluyendo una letra mayúscula, una letra minúscula y un número. No se permiten caracteres especiales.")
            password_line_edit.setStyleSheet("border-color: red;")
            return False
        
        password_line_edit.setStyleSheet("border-color: green;")
        return password

    def mostrar_warning(self, mensaje):
        QMessageBox.warning(self, "Validación de Formulario", mensaje)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    style ="""
    /* Estilo para la aplicación */
    QWidget {
        background-color: white; /* Fondo blanco */
        color: black; /* Letras negras */
        border-radius: 15px; /* Bordes redondeados */
        
    }
    Qlabel {
        font-size: 15px;
    }
    QWidget { 
        border: none; 
        }
    /* Estilo para los QLineEdit */
    QLineEdit {
        background-color: rgba(255, 255, 255, 50%); /* Fondo transparente */
        border-bottom: 1px solid black; /* Borde inferior */
        border-radius: 5px; /* Bordes redondeados */
        color: black; /* Letras negras */
        height: 30px; /* Altura personalizada */
        font-size: 13px;
    }

    /* Estilo para los botones */
    QPushButton {
        background-color: #1B4965; /* Color #1B4965 */
        color: white; /* Letras blancas */
        border: none; /* Sin borde */
        padding: 5px 8px; /* Espaciado interno */
        border-radius: 10px; /* Bordes redondeados */
        height: 27px; /* Altura personalizada */
        font-size: 15px;

    }

    /* Estilo para cuando se presiona un botón */
    QPushButton:pressed {
        background-color: #123547; /* Color oscuro cuando se presiona */
    }

    /* Estilo para cuando se pasa el cursor sobre un botón */
    QPushButton:hover {
        background-color: #336699; /* Color más claro cuando se pasa el cursor */
    }
    

    """
    window.setStyleSheet(style)
    window.show()
    sys.exit(app.exec())