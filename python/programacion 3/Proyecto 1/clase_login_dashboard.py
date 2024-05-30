from login_ui import Ui_MainWindow_login
from PySide6 import QtWidgets, QtGui



class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow_login):
    basedir = os.path.dirname(__file__)
    dic_usuarios = {}
    def __init__(self):
        self.basedir = os.path.dirname(__file__)
        super().__init__()
        self.setupUi(self)
        #botones login
        self.button_registrate_stacked.clicked.connect(self.cambiar_a_registro)
        self.button_ver_password.pressed.connect(lambda: self.mirar_password(self.line_password_login, self.button_ver_password))
        self.button_ver_password.released.connect(lambda: self.ocultar_password(self.line_password_login, self.button_ver_password))
        self.button_inicia_sesion.clicked.connect(self.validar_login)

        #botones registro
        self.button_inicia_sesion_stacked.clicked.connect(self.cambiar_a_login)
        self.button_ver_password_registro.pressed.connect(lambda: self.mirar_password(self.line_password_registro, self.button_ver_password))
        self.button_ver_password_registro.released.connect(lambda: self.ocultar_password(self.line_password_registro, self.button_ver_password))
        self.pushButton_7.pressed.connect(lambda: self.mirar_password(self.line_password_validacion_registro, self.pushButton_7))
        self.pushButton_7.released.connect(lambda: self.ocultar_password(self.line_password_validacion_registro, self.pushButton_7))
        self.button_registrarse.clicked.connect(self.validar_registro)

        


    def cambiar_a_login(self):
        self.stackedWidget.setCurrentWidget(self.login_widget)  # Cambia a la página de inicio
        self.line_usuario_login.clear()
        self.line_password_login.clear()
        self.line_usuario_login.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_password_login.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        

    def cambiar_a_registro(self):
        self.stackedWidget.setCurrentWidget(self.singup_widget)
        self.line_nombre_registro.clear()
        self.line_apellido_registro.clear()
        self.line_email.clear()
        self.line_password_registro.clear()
        self.line_password_validacion_registro.clear()
        self.line_nombre_registro.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_apellido_registro.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_email.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_password_registro.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_password_validacion_registro.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")

    
    def mirar_password(self, line_edit, button):
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.basedir, "icons_login/ojo-abierto-morado.png")))
        button.setIcon(icon)
    
    def ocultar_password(self, line_edit, button):
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.basedir, "icons_login/ojo-cerrado-morado.png")))
        button.setIcon(icon)
    
    def validar_login(self):
        usuario = self.line_usuario_login.text().strip()
        contraseña = self.line_password_login.text().strip()

        if usuario and contraseña:
            if usuario in dic_usuarios:
                password = dic_usuarios[usuario][2]  # Obtener la contraseña almacenada
                if contraseña == password:
                    QtWidgets.QMessageBox.information(self,"Login Exitoso", "Has iniciado sesión correctamente.")
                    self.line_usuario_login.clear()
                    self.line_password_login.clear()
                    # self.line_usuario_login.setStyleSheet("border-color: black;")
                    # self.line_password_login.setStyleSheet("border-color: black;")
                    # implementacion para la pagina principal
                    self.main_window = MainApp()
                    self.main_window.name_edit_profile_2.setText(f"{dic_usuarios[usuario][0]}")
                    self.main_window.lastname_edit_profile_2.setText(f"{dic_usuarios[usuario][1]}")
                    self.main_window.email_edit_profile_2.setText(usuario)
                    self.main_window.pass_edit_profile_2.setText(contraseña)
                    self.main_window.show()
                    self.close()
                else:
                    self.mostrar_warning("Contraseña incorrecta.")
                    # self.line_password_login.setStyleSheet("border-color: red;")
                    return
            else:
                self.mostrar_warning("El usuario no existe.")
                # self.line_usuario_login.setStyleSheet("border-color: red;")
                return

        else:
            if not usuario:
                # self.line_usuario_login.setStyleSheet("border-color: red;")
                self.mostrar_warning("El campo de usuario no puede estar vacío.")
                return
            if not contraseña:
                # self.line_password_login.setStyleSheet("border-color: red;")
                self.mostrar_warning("El campo de contraseña no puede estar vacío.")
                return

    def validar_registro(self):
        nombre = self.line_nombre_registro.text().strip()
        apellido = self.line_apellido_registro.text().strip()
        email = self.line_email.text().strip()
        password = self.line_password_registro.text().strip()
        validacion_password = self.line_password_validacion_registro.text().strip()

        mensajes_alerta = []  # Lista para almacenar mensajes de alerta

        if not nombre:
            mensajes_alerta.append("El nombre no puede estar vacío.")

        if not apellido:
            mensajes_alerta.append("El apellido no puede estar vacío.")

        if not email:
            mensajes_alerta.append("El email no puede estar vacío.")

        if not password:
            mensajes_alerta.append("La contraseña no puede estar vacía.")

        if not validacion_password:
            mensajes_alerta.append("La verificación de contraseña no puede estar vacía.")

        if mensajes_alerta:
            self.mostrar_warning("\n".join(mensajes_alerta))
            return

        if password != validacion_password:
            self.mostrar_warning("Verifica que tus contraseñas sean iguales")
            return
        else:
            
            if self.validar_nombre_registro(self.line_nombre_registro): 
                if self.validar_apellido_registro(self.line_apellido_registro):
                    if self.validar_email_registro(self.line_email): 
                        if self.validar_password_registro(self.line_password_registro):
                            nombre = self.line_nombre_registro.text()
                            apellido = self.line_apellido_registro.text()
                            email = self.line_email.text()
                            contraseña = self.line_password_registro.text()
                            msg_box = QMessageBox()
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
                            dic_usuarios[email] = [nombre, apellido, contraseña]
                        

                            print(dic_usuarios)
                            ok = msg_box.exec()
                            if ok:
                                self.stackedWidget.setCurrentWidget(self.login_widget)
                            self.line_nombre_registro.clear()
                            self.line_apellido_registro.clear()
                            self.line_email.clear()
                            self.line_password_registro.clear()
                            self.line_password_validacion_registro.clear()
                            # self.line_nombre_registro.setStyleSheet("border-color: black;")
                            # self.line_apellido_registro.setStyleSheet("border-color: black;")
                            # self.line_email.setStyleSheet("border-color: black;")
                            # self.line_password_registro.setStyleSheet("border-color: black;")
                            # self.line_password_validacion_registro.setStyleSheet("border-color: black;")


    def validar_nombre_registro(self, nombre_line_edit):
        nombre = nombre_line_edit.text().strip()
        if not re.match(r'^[a-zA-Z\s]+$', nombre):
            self.mostrar_warning("El nombre no puede contener caracteres especiales ni dígitos.")
            # nombre_line_edit.setStyleSheet("border-color: red;")
            return False
        elif len(nombre.split()) > 3:
            self.mostrar_warning("No puede haber más de tres nombres.")
            # nombre_line_edit.setStyleSheet("border-color: red;")
            return False
        else:
            nombre = ' '.join(nombre.split()).title()
            nombre_line_edit.setText(nombre)
            # nombre_line_edit.setStyleSheet("border-color: green;")

            return nombre

    def validar_apellido_registro(self, apellido_line_edit):
        apellido = apellido_line_edit.text().strip()
        if not re.match(r'^[a-zA-Z\s]+$', apellido):
            self.mostrar_warning("El apellido no puede contener caracteres especiales ni dígitos.")
            # apellido_line_edit.setStyleSheet("border-color: red;")
            return False
        elif len(apellido.split()) > 3:
            self.mostrar_warning("No puede haber más de tres apellidos.")
            # apellido_line_edit.setStyleSheet("border-color: red;")
            return False
        else:
            apellido = ' '.join(apellido.split()).title()
            apellido_line_edit.setText(apellido)
            # apellido_line_edit.setStyleSheet("border-color: green;")
            return apellido

    def validar_email_registro(self, email_line_edit):
        email = email_line_edit.text()
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email.strip()):
            self.mostrar_warning("Debe colocar un email válido.")
            # email_line_edit.setStyleSheet("border-color: red;")
            return False
        # email_line_edit.setStyleSheet("border-color: green;")
        email_line_edit.setText(email)
        return email

    def validar_password_registro(self, password_line_edit):
        password = password_line_edit.text()
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(password_regex, password.strip()):
            self.mostrar_warning("La contraseña debe contener al menos 8 caracteres, incluyendo una letra mayúscula, una letra minúscula y un número. No se permiten caracteres especiales.")
            # password_line_edit.setStyleSheet("border-color: red;")
            return False
        # password_line_edit.setStyleSheet("border-color: green;")
        password_line_edit.setText(password)
        return password

    def mostrar_warning(self, mensaje):
        QtWidgets.QMessageBox.warning(self, "Validaciónes", mensaje)
