from ui_viajes_final_ui import Ui_MainWindow
from login_ui import Ui_MainWindow_login
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from hacerpdf import crear_pdf
from clase_widgets import *
import sys
import os
import re
import datetime

from login_ui import Ui_MainWindow_login
from PySide6 import QtWidgets, QtGui

#Primer diccionario de recordatorios y segundo diccionario de viajes(contine en su interior itinerario del viaje y gastos) y el ultimo de datos del perfil
datos_usuario = {
    ""
}
dic_usuarios = {'andresfg13789@gmail.com': ['Andres', 'Guerra', '2567AndresG', [{'texto': 'a'}], {}, {}]}
class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow_login):
    basedir = os.path.dirname(__file__)
    def __init__(self):
        self.basedir = os.path.dirname(__file__)
        super().__init__()
        self.setupUi(self)
        
        #botones login
        self.button_registrate_stacked.clicked.connect(self.cambiar_a_registro)
        self.button_ver_password.pressed.connect(lambda: self.mirar_password(self.line_password_login, self.button_ver_password, "ojo-abierto-morado.png"))
        self.button_ver_password.released.connect(lambda: self.ocultar_password(self.line_password_login, self.button_ver_password, "ojo-cerrado-morado.png"))
        self.button_inicia_sesion.clicked.connect(self.validar_login)

        #botones registro
        self.button_inicia_sesion_stacked.clicked.connect(self.cambiar_a_login)
        self.button_ver_password_registro.pressed.connect(lambda: self.mirar_password(self.line_password_registro, self.button_ver_password_registro, "ojo-abierto-morado.png"))
        self.button_ver_password_registro.released.connect(lambda: self.ocultar_password(self.line_password_registro, self.button_ver_password_registro, "ojo-cerrado-morado.png"))
        self.pushButton_7.pressed.connect(lambda: self.mirar_password(self.line_password_validacion_registro, self.pushButton_7, "ojo-abierto-morado.png"))
        self.pushButton_7.released.connect(lambda: self.ocultar_password(self.line_password_validacion_registro, self.pushButton_7, "ojo-cerrado-morado.png"))
        self.button_registrarse.clicked.connect(self.validar_registro) 
        
        self.line_usuario_login.setText("andresfg13789@gmail.com")
        self.line_password_login.setText("2567AndresG")
        

        


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

    
    def mirar_password(self, line_edit, button, icon_name):
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.basedir, "img_trabajos", icon_name)))
        button.setIcon(icon)
    
    def ocultar_password(self, line_edit, button, icon_name):
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.basedir, "img_trabajos", icon_name)))
        button.setIcon(icon)
    
    def validar_login(self):
        usuario = self.line_usuario_login.text().strip()
        contraseña = self.line_password_login.text().strip()

        if usuario and contraseña:
            if usuario in dic_usuarios:
                password = dic_usuarios[usuario][2]  # Obtener la contraseña almacenada
                if contraseña == password:
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



class MainApp(QMainWindow, Ui_MainWindow):
    basedir = os.path.dirname(__file__)
    #Validaciones del perfil
    paso_foto_de_perfil = False
    paso_escoger_sexualidad = False
    paso_nombre_validado = False
    paso_apellido_validado = False
    paso_edad_validada = False
    ti_o_cc_validado = False
    direccion_validada = False
    telefono_validado = False
    edad_validada = False
    pasaporte_validado = False
    nacionalidad_validada = False
    biografia_validada = False

    viajes_usuario = {}
    indice_viajes_guardados = 0

    pasos_totales = 9
    pasos_completados = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My travel app")

        self.menub.setHidden(True)

        self.home_small_button1.setChecked(True)
        self.mostrar_pagina_home()

        self.open_pic_to_profile_pic_2.setHidden(True)
        self.delete_profile_pic_2.setHidden(True)

        self.home_small_button1.clicked.connect(self.mostrar_pagina_home)
        self.home_small_button2.clicked.connect(self.mostrar_pagina_home)
        self.mytravels_small_button1.clicked.connect(self.mostrar_pagina_mis_viajes)
        self.mytravels_small_button2.clicked.connect(self.mostrar_pagina_mis_viajes)
        self.newtravel_small_button1.clicked.connect(self.mostrar_pagina_nuevo_viaje)
        self.newtravel_small_button2.clicked.connect(self.mostrar_pagina_nuevo_viaje)
        self.itinerary_small_button1.clicked.connect(self.mostrar_pagina_itinerario)
        self.itinerary_small_button2.clicked.connect(self.mostrar_pagina_itinerario)
        self.bills_small_button1.clicked.connect(self.mostrar_pagina_gastos)
        self.bills_small_button2.clicked.connect(self.mostrar_pagina_gastos)
        self.notify_small_button1.clicked.connect(self.mostrar_pagina_notificaciones)
        self.notify_small_button2.clicked.connect(self.mostrar_pagina_notificaciones)
        self.settings_small_button1.clicked.connect(self.mostrar_configuraciones_page)
        self.settings_small_button2.clicked.connect(self.mostrar_configuraciones_page)

        self.myprofile_button.clicked.connect(self.mostrar_pagina_perfil)
        

        #Botones de recordatorio
        self.agregar_recordatorio_nuevo.clicked.connect(self.mostrar_agregar_nuevo_recordatorio)
        self.volver_recordatorios_agregar_recordatorio_page.clicked.connect(self.mostrar_pagina_recordatorios)

        #Botones de settings
        self.suppor_button_settings.clicked.connect(self.mostrar_pagina_de_soporte)
        self.back_button_support.clicked.connect(self.mostrar_pagina_botones_configuraciones)
        self.about_us_button_settings.clicked.connect(self.mostrar_pagina_about_us)
        self.back_button_about_us.clicked.connect(self.mostrar_pagina_botones_configuraciones)

        #Botones del editar perfil
        self.open_pic_to_profile_pic_2.clicked.connect(self.cargar_foto_de_perfil)
        self.delete_profile_pic_2.clicked.connect(self.borrar_foto_de_perfil)
        self.edit_profile_2.clicked.connect(self.activar_edicion_de_perfil)

        #Grupo de botones para sexo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.hombre_radio_profile_2)
        self.button_group.addButton(self.otro_radio_profile_2)
        self.button_group.addButton(self.mujer_radio_profile_2)
        self.button_group.addButton(self.none_radio_profile_2)
        self.button_group.buttonClicked.connect(self.validar_sexo)

        #Reloj
        self.Horas.setDigitCount(2)
        self.Horas.setSegmentStyle(QLCDNumber.Filled)
        self.minutos.setDigitCount(2)
        self.minutos.setSegmentStyle(QLCDNumber.Filled)

        self.timer_reloj = QTimer(self)
        self.timer_reloj.timeout.connect(self.update_time)
        self.timer_reloj.start(1000)

        self.cargar_viajes_iniciales()
        self.listar_viajes()
        self.actualizar_gastos_del_viaje()
        self.actualizar_planes_del_itinerario()
        self.actualizar_progreso()
        

        #Botones de la pagina nuevo viaje
        self.checkbox_vuelos_nuevo_viaje.stateChanged.connect(self.activar_regreso_ida_avion)
        self.checkbox_alojaimento_nuevo_viaje.stateChanged.connect(self.activar_alojamiento)
        self.save_new_travel_button.clicked.connect(self.evaluar_viaje)
        self.boton_familia_nuevo_viaje.clicked.connect(self.activar_line_edit_familia)
        self.boton_solo_nuevo_viaje.clicked.connect(self.activar_line_edit_familia)
        self.boton_pareja_nuevo_viaje.clicked.connect(self.activar_line_edit_familia)

        #Botones de la pagina mis viajes
        self.eliminar_viajeguardado_button.clicked.connect(self.eliminar_viaje_guardado)
        self.ver_viaje_guardado_button.clicked.connect(self.pasar_datos_to_pdf)



        #Botones de los gastos del viaje
        self.seleccionar_viaje_gasto.currentIndexChanged.connect(self.actualizar_gastos_del_viaje)
        self.boton_guardar_gasto.clicked.connect(self.añadir_gasto)
        self.eliminar_gasto_button.clicked.connect(self.eliminar_gasto)


        #Botones de agregar itinerario
        self.seleccionar_viaje_itinerario.currentIndexChanged.connect(self.actualizar_planes_del_itinerario)
        self.boton_guardar_plan.clicked.connect(self.añadir_plan)
        self.eliminar_plan_button.clicked.connect(self.eliminar_plan)

        #señales recordatorio
        self.check_box_hora_recordatorio.stateChanged.connect(self.activar_fecha_hora)
        self.agregar_recordatorio_button.clicked.connect(self.agregar_recordatorio)
        self.checkbox_lugar_recordatorio.stateChanged.connect(self.activar_line_lugar_recordatorio)
        self.eliminar_recordatorio_button.clicked.connect(self.borrar_recordatorio)

    
    def agregar_recordatorio(self):
        texto = self.text_edit_recordatorio.toPlainText()
        fecha = self.lineedit_fecha_recordatorio.text().strip()
        hora = self.lineedit_hora_recordatorio.text().strip()
        formato = self.am_pm_hora_recordatorio.currentText()
        lugar = self.lineedit_lugar_recordatorio.text()

        if texto:
            # Crear el recordatorio
            if self.check_box_hora_recordatorio.isChecked():
                if self.validar_fecha_hora(fecha, hora, formato, "Recordatorio"):
                    if self.checkbox_lugar_recordatorio.isChecked():
                        if lugar:
                            recordatorio_info = {
                                "texto": texto,
                                "fecha": fecha,
                                "hora": hora,
                                "lugar": lugar
                            }
                        else:
                            self.mostrar_warning("Si activaste el lugar no debe quedar vacío")
                            return  # Salir de la función si no se cumple la condición
                    else:
                        recordatorio_info = {
                            "texto": texto,
                            "fecha": fecha,
                            "hora": hora
                        }
            elif self.checkbox_lugar_recordatorio.isChecked():
                if lugar:
                    recordatorio_info = {
                        "texto": texto,
                        "lugar": lugar
                    }
                else:
                    self.mostrar_warning("Si activaste el lugar no debe quedar vacío")
                    return  # Salir de la función si no se cumple la condición
            else:
                recordatorio_info = {"texto": texto}

            # Agregar el recordatorio al diccionario de usuarios
            email_usuario = self.email_edit_profile_2.text()
            if email_usuario in dic_usuarios:
                dic_recordatorios = dic_usuarios[email_usuario][3]
                dic_recordatorios.append(recordatorio_info)
            else:
                self.mostrar_warning("Usuario no encontrado en el diccionario de usuarios")
                return  # Salir de la función si el usuario no está en el diccionario

            # Actualizar la lista de recordatorios en la interfaz
            self.cargar_recordatorios()

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Recordatorio creado con exito")
            msg_box.setWindowTitle("Recordatorio")

            # Cambiar el tamaño del QMessageBox
            msg_box.resize(300, 200)

            # Cambiar el estilo del botón
            msg_box.setStyleSheet("""
                QPushButton {
                    min-width: 30px;
                    min-height: 15px;
                }
            """)
            ok = msg_box.exec()
            if ok:
                self.mostrar_pagina_recordatorios()
        else:
            self.mostrar_warning("El recordatorio no debe quedar vacío")

    def cargar_recordatorios(self):
        # Limpiar la lista de recordatorios antes de cargar nuevos
        self.lista_agregar_recordatorios.clear()

        # Obtener el correo electrónico del usuario actual
        email_usuario = self.email_edit_profile_2.text()

        # Verificar si el usuario está en el diccionario de usuarios
        if email_usuario in dic_usuarios:
            # Obtener la lista de recordatorios del usuario
            recordatorios_usuario = dic_usuarios[email_usuario][3]
            print(recordatorios_usuario)

            # Iterar sobre los recordatorios del usuario y crear widgets para cada uno
            for recordatorio_info in recordatorios_usuario:
                texto = recordatorio_info.get("texto", "")
                fecha = recordatorio_info.get("fecha", "")
                hora = recordatorio_info.get("hora", "")
                lugar = recordatorio_info.get("lugar", "")

                # Crear un widget RecordatorioWidget para el recordatorio actual
                recordatorio_widget = RecordatorioWidget(texto, fecha, hora, lugar)

                # Agregar el widget a la lista en la interfaz
                item = QListWidgetItem()  # Crear un ítem de lista
                item.setSizeHint(recordatorio_widget.sizeHint())  # Establecer el tamaño del ítem
                self.lista_agregar_recordatorios.addItem(item)  # Agregar el ítem a la lista
                self.lista_agregar_recordatorios.setItemWidget(item, recordatorio_widget)  # Asociar el widget con el ítem
        else:
            # Mostrar un mensaje si el usuario no está en el diccionario de usuarios
            self.mostrar_warning("Usuario no encontrado en el diccionario de usuarios")

    def borrar_recordatorio(self):
        recordatorio_a_borrar = self.lista_agregar_recordatorios.currentItem()
        if recordatorio_a_borrar:
            confirmacion = QMessageBox.question(self, "Confirmar eliminación", "¿Seguro que quiere eliminar este recordatorio?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirmacion == QMessageBox.StandardButton.Yes:
                # Obtener el índice del recordatorio en la lista
                indice_recordatorio = self.lista_agregar_recordatorios.row(recordatorio_a_borrar)

                # Obtener el correo electrónico del usuario actual
                email_usuario = self.email_edit_profile_2.text()

                # Verificar si el usuario está en el diccionario de usuarios
                if email_usuario in dic_usuarios:
                    # Obtener la lista de recordatorios del usuario
                    recordatorios_usuario = dic_usuarios[email_usuario][3]

                    # Eliminar el recordatorio correspondiente de la lista
                    if indice_recordatorio < len(recordatorios_usuario):
                        del recordatorios_usuario[indice_recordatorio]

                    # Eliminar el recordatorio de la lista en la interfaz
                    self.lista_agregar_recordatorios.takeItem(indice_recordatorio)

                else:
                    # Mostrar un mensaje si el usuario no está en el diccionario de usuarios
                    self.mostrar_warning("Usuario no encontrado en el diccionario de usuarios")
        else:
            self.mostrar_warning("Para borrar un recordatorio primero lo debe seleccionar")
        
    def activar_fecha_hora(self):
        if self.check_box_hora_recordatorio.isChecked():
            self.lineedit_hora_recordatorio.setEnabled(True)
            self.lineedit_fecha_recordatorio.setEnabled(True)
            self.am_pm_hora_recordatorio.setEnabled(True)
        else:
            self.lineedit_hora_recordatorio.setEnabled(False)
            self.lineedit_fecha_recordatorio.setEnabled(False)
            self.am_pm_hora_recordatorio.setEnabled(False)
            self.lineedit_hora_recordatorio.clear()
            self.lineedit_fecha_recordatorio.clear()
            self.checkbox_lugar_recordatorio.setChecked(False)
            self.check_box_hora_recordatorio.setChecked(False)

    def activar_line_lugar_recordatorio(self):
        if self.checkbox_lugar_recordatorio.isChecked():
            self.lineedit_lugar_recordatorio.setEnabled(True)
        else:
            self.lineedit_lugar_recordatorio.setEnabled(False)
            self.lineedit_lugar_recordatorio.clear()

    def pasar_datos_to_pdf(self):
        current_item = self.list_widget_viajes_guardados.currentItem()
        if current_item is None:
            self.mostrar_warning("Por favor, selecciona un viaje primero.")
            return
        
        item_widget = self.list_widget_viajes_guardados.itemWidget(current_item)
        if item_widget is None:
            self.mostrar_warning("El elemento seleccionado no tiene datos asociados.")
            return
        
        indice = item_widget.indice
        datos = self.viajes_usuario.get(indice)
        if datos is None:
            self.mostrar_warning("No se encontraron datos para el viaje seleccionado.")
            return
    

        crear_pdf(datos)

    def activar_line_edit_familia(self):
        if self.boton_familia_nuevo_viaje.isChecked():
            self.line_edit_familia_nuevo_viaje.setEnabled(True)
        else:
            self.line_edit_familia_nuevo_viaje.setEnabled(False)

    def evaluar_viaje(self):
        texto_titulo = self.lineedit_titulo_nuevo_viaje.text()
        texto_destino = self.lineedit_destino_nuevo_viaje.text()

        if not texto_titulo.strip():
            self.mostrar_warning("El título del viaje es obligatorio")
            return

        if not texto_destino.strip():
            self.mostrar_warning("El destino del viaje es obligatorio")
            return

        fecha_inicio = self.lineedit_fechainicio_nuevo_viaje.text()
        fecha_fin = self.lineedit_fechafin_nuevo_viaje.text()

        if not fecha_inicio.strip():
            self.mostrar_warning("La fecha de inicio es obligatoria")
            return

        if not fecha_fin.strip():
            self.mostrar_warning("La fecha de fin es obligatoria")
            return

        if not self.validar_solo_fecha(fecha_inicio, "Inicio del viaje") or not self.validar_solo_fecha(fecha_fin, "Fin del viaje"):
            return

        lista_fechas_inicio = fecha_inicio.split("-")
        lista_fechas_fin = fecha_fin.split("-")
        dia_inicio_viaje, mes_inicio_viaje, año_inicio_viaje = lista_fechas_inicio[0], lista_fechas_inicio[1], lista_fechas_inicio[2]
        dia_fin_viaje, mes_fin_viaje, año_fin_viaje = lista_fechas_fin[0], lista_fechas_fin[1], lista_fechas_fin[2]


        if not self.comparar_fechas(dia_inicio_viaje, mes_inicio_viaje, año_inicio_viaje, dia_fin_viaje, mes_fin_viaje, año_fin_viaje):
            self.mostrar_warning("La fecha de fin no puede ser antes de la fecha de inicio")
            return

        presupuesto = self.lineedit_presupuesto_nuevo_viaje.text().strip()

        if presupuesto.isdigit() or presupuesto == "":
            if presupuesto == "":
                presupuesto = 0
            else:
                presupuesto = int(presupuesto)
        else:
            self.mostrar_warning("El presupuesto del viaje debe ser un número")
            return

        personas_de_viaje = None
        if self.boton_solo_nuevo_viaje.isChecked():
            personas_de_viaje = "1"
        elif self.boton_pareja_nuevo_viaje.isChecked():
            personas_de_viaje = "2"
        else:
            if self.boton_familia_nuevo_viaje.isChecked():
                personas_de_viaje = self.line_edit_familia_nuevo_viaje.text().strip()
                if personas_de_viaje == "" or not personas_de_viaje.isdigit():
                    self.mostrar_warning("Debe colocar el número de integrantes de la familia")
                    return

        vuelos = None
        if self.checkbox_vuelos_nuevo_viaje.isChecked():
            fecha_ida = self.lineedit_fecha_ida_nuevo_viaje.text()
            hora_ida = self.lineedit_hora_ida_nuevo_viaje.text()
            ampm_ida = self.combobox_ampm_hora_ida_nuevo_viaje.currentText()
            fecha_regreso = self.lineedit_fecha_regreso_nuevo_viaje.text()
            hora_regreso = self.lineedit_hora_regreso_nuevo_viaje.text()
            ampm_regreso = self.combobox_ampm_hora_regreso_nuevo_viaje.currentText()

            if not self.validar_fecha_hora(fecha_ida, hora_ida, ampm_ida, "ida") or not self.validar_fecha_hora(fecha_regreso, hora_regreso, ampm_regreso, "regreso"):
                return

            if not self.comparar_fechas_vuelo(fecha_ida, fecha_regreso):
                self.mostrar_warning("La fecha de regreso no puede ser antes de la fecha de ida")
                return

            vuelos = {
                "fecha_ida": fecha_ida,
                "hora_ida": hora_ida,
                "ampm_ida": ampm_ida,
                "fecha_regreso": fecha_regreso,
                "hora_regreso": hora_regreso,
                "ampm_regreso": ampm_regreso,
                "costo_ida": self.lineedit_costo_ida_nuevo_viaje.text(),
                "costo_regreso": self.lineedit_costo_regreso_nuevo_viaje.text()
            }

        alojamiento = None
        if self.checkbox_alojaimento_nuevo_viaje.isChecked():
            alojamiento_tipo = self.combobox_hote_o_airbnb_nuevo_viaje.currentText()
            direccion = self.lineedit_direccion_nuevo_viaje.text()
            fecha_inicio_aloja = self.lineedit_fecha_inicio_alojamiento_nuevo_viaje.text()
            hora_inicio_aloja = self.lineedit_hora_inicio_nuevo_viaje_alojamiento.text()
            ampm_inicio_aloja = self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.currentText()
            fecha_fin_aloja = self.lineedit_fecha_fin_alojamiento_nuevo_viaje.text()
            hora_fin_aloja = self.lineedit_hora_fin_nuevo_viaje_alojamiento.text()
            ampm_fin_aloja = self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.currentText()
            costo_aloja = self.line_edit_costo_alojamiento_nuevo_viaje.text().strip() or "0"
            info_adicional = self.plaintextedit_info_adicional_nuevo_viaje.toPlainText()

            if not direccion.strip():
                self.mostrar_warning("La dirección del alojamiento es obligatoria")
                return

            if not self.validar_fecha_hora(fecha_inicio_aloja, hora_inicio_aloja, ampm_inicio_aloja, "inicio de alojamiento") or not self.validar_fecha_hora(fecha_fin_aloja, hora_fin_aloja, ampm_fin_aloja, "fin de alojamiento"):
                return

            if not self.comparar_fechas_vuelo(fecha_inicio_aloja, fecha_fin_aloja):
                self.mostrar_warning("La fecha de fin del alojamiento no puede ser antes de la fecha de inicio")
                return

            alojamiento = {
                "tipo": alojamiento_tipo,
                "direccion": direccion,
                "fecha_inicio": fecha_inicio_aloja,
                "hora_inicio": hora_inicio_aloja,
                "ampm_inicio": ampm_inicio_aloja,
                "fecha_fin": fecha_fin_aloja,
                "hora_fin": hora_fin_aloja,
                "ampm_fin": ampm_fin_aloja,
                "costo": costo_aloja,
                "info_adicional": info_adicional
            }

        self.indice_viajes_guardados += 1
        self.viajes_usuario[self.indice_viajes_guardados] = {
            "titulo": texto_titulo,
            "destino": texto_destino,
            "fecha_inicio": lista_fechas_inicio,
            "fecha_fin": lista_fechas_fin,
            "presupuesto": presupuesto,
            "personas": personas_de_viaje,
            "vuelos": vuelos,
            "alojamiento": alojamiento,
            "Itinerario": [],
            "Gastos": []
        }

        self.listar_viajes()
        self.mytravels_small_button1.click()
        self.reset_formulario_nuevo_viaje()

        self.mostrar_exito("El viaje se ha agregado correctamente")

    def añadir_plan(self):
        plan = self.descripcion_del_plan.text()
        if not plan:
            self.mostrar_warning("Debe agregar un plan")
            return

        fecha = self.fecha_del_plan.text()
        if not fecha:
            self.mostrar_warning("Agregue la fecha de cuando se realizará el plan")
            return

        hora = self.hora_del_plan.text()
        if not hora:
            self.mostrar_warning("Agregue la hora")
            return
        
        am_pm = self.am_pm_del_plan.currentText()
        if not self.validar_fecha_hora(fecha, hora, self.am_pm_del_plan.currentText(), "Itinerario"):
            return

        else:
            clave_seleccionada = self.seleccionar_viaje_itinerario.currentData()
            if clave_seleccionada is not None:
                viaje_encontrado = self.viajes_usuario.get(clave_seleccionada)
                if viaje_encontrado:
                    itinerario = viaje_encontrado.get("Itinerario", [])
                    info_plan = [plan, hora, am_pm, fecha]
                    itinerario.append(info_plan)
                    viaje_encontrado["Itinerario"] = itinerario
                    self.viajes_usuario[clave_seleccionada] = viaje_encontrado

                    self.mostrar_exito("El plan se ha agregado correctamente.")
                    self.actualizar_planes_del_itinerario()
                else:
                    self.mostrar_warning("Viaje no encontrado")

    def actualizar_planes_del_itinerario(self):
        clave_seleccionada = self.seleccionar_viaje_itinerario.currentData()
        if clave_seleccionada is not None:
            viaje_encontrado = self.viajes_usuario.get(clave_seleccionada)
            if viaje_encontrado:
                planes = viaje_encontrado.get("Itinerario", [])

                self.list_widget_de_planes.clear()
                for plan in planes:
                    descripcion_del_plan, hora, am_pm, fecha = plan
                    plan_widget = PlanWidget(descripcion_del_plan, hora, am_pm, fecha)
                    item=QListWidgetItem(self.list_widget_de_planes)
                    item.setSizeHint(plan_widget.sizeHint())
                    self.list_widget_de_planes.addItem(item)
                    self.list_widget_de_planes.setItemWidget(item, plan_widget)
    
    def eliminar_plan(self):
        clave_seleccionada = self.seleccionar_viaje_itinerario.currentData()
        if clave_seleccionada is not None:
            viaje_encontrado = self.viajes_usuario.get(clave_seleccionada)
            if viaje_encontrado:
                planes = viaje_encontrado.get("Itinerario", [])
                plan_seleccionado = self.list_widget_de_planes.currentItem()
                if plan_seleccionado:
                    item_index = self.list_widget_de_planes.row(plan_seleccionado)
                    confirmacion = QMessageBox.question(self, "Confirmar eliminación", "¿Está seguro de que desea eliminar este plan?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if confirmacion == QMessageBox.Yes:
                        self.list_widget_de_planes.takeItem(item_index)
                        if 0 <= item_index < len(planes):
                            del planes[item_index]
                        viaje_encontrado["Itinerario"] = planes
                        self.viajes_usuario[clave_seleccionada] = viaje_encontrado
                        self.mostrar_exito("El plan se ha eliminado correctamente")
                        self.actualizar_planes_del_itinerario()
                else:
                    self.mostrar_warning("Seleccione un plan para eliminar")
            else:
                self.mostrar_warning("Viaje no encontrado")
        
    def eliminar_viaje_guardado(self):
        viaje_seleccionado = self.list_widget_viajes_guardados.currentItem()
        if viaje_seleccionado:
            item_index = self.list_widget_viajes_guardados.row(viaje_seleccionado)
            clave_seleccionada = self.list_widget_viajes_guardados.item(item_index).data(Qt.UserRole)

            confirmacion = QMessageBox.question(self, "Confirmar eliminación", "¿Está seguro de que desea eliminar este viaje?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirmacion == QMessageBox.Yes:
                # Eliminar el viaje de la listas
                self.list_widget_viajes_guardados.takeItem(item_index)

                # Eliminar el viaje del diccionario
                if clave_seleccionada in self.viajes_usuario:
                    del self.viajes_usuario[clave_seleccionada]

                self.mostrar_exito("El viaje se ha eliminado correctamente")
                self.actualizar_planes_del_itinerario()
                self.actualizar_gastos_del_viaje()
        else:
            self.mostrar_warning("Seleccione un viaje para eliminar")

    def actualizar_gastos_del_viaje(self):
        clave_seleccionada = self.seleccionar_viaje_gasto.currentData()
        if clave_seleccionada is not None:
            viaje_encontrado = self.viajes_usuario.get(clave_seleccionada)
            if viaje_encontrado:
                presupuesto = viaje_encontrado["presupuesto"]
                vuelos = viaje_encontrado.get("vuelos", {})
                alojamiento = viaje_encontrado.get("alojamiento", {})
                gastos = viaje_encontrado.get("Gastos", [])

                total_vuelos = float(vuelos['costo_ida']) + float(vuelos['costo_regreso'])
                total_gastos_varios = 0

                self.label_presupuesto_del_viaje.setText(f"${presupuesto:.2f}")
                self.label_costo_de_los_vuelos.setText(f"${total_vuelos:.2f}")
                self.label_costo_del_alojamiento.setText(f"${float(alojamiento['costo']):.2f}")

                # Actualizar la lista de gastos en la interfaz
                self.list_widget_gastos.clear()
                for gasto in gastos:
                    descripcion, valor, fecha = gasto
                            # Añadir el gasto a la interfaz
                    gasto_widget = GastoWidget(descripcion, valor, fecha)
                    item = QListWidgetItem(self.list_widget_gastos)
                    item.setSizeHint(gasto_widget.sizeHint())
                    self.list_widget_gastos.addItem(item)
                    self.list_widget_gastos.setItemWidget(item, gasto_widget)


                    total_gastos_varios += valor

                self.label_total_de_los_gastos_varios.setText(f"${total_gastos_varios:.2f}")

                total_de_gastos = float(presupuesto) - total_vuelos - float(alojamiento['costo']) - total_gastos_varios
                self.label_total_total_gastos.setText(f"${total_de_gastos:.2f}")
            
    def añadir_gasto(self):
        descripcion = self.descripcion_del_gasto.text().strip()
        if not descripcion:
            self.mostrar_warning("Debe agregar una descripción del gasto")
            return

        valor = self.costo_del_gasto.text().strip()
        if not valor:
            self.mostrar_warning("Agregue el costo del gasto")
            return
        if valor.isdigit():
            gasto = float(valor)
        else:
            self.mostrar_warning("Escriba un valor númerico")
            return

        fecha = self.fecha_del_gasto.text()
        if fecha.strip() == "":
            self.mostrar_warning("Escriba una fecha")
            return
        if not self.validar_solo_fecha(fecha, "Fecha gasto"):
            return

        clave_seleccionada = self.seleccionar_viaje_gasto.currentData()
        if clave_seleccionada is not None:
            viaje_encontrado = self.viajes_usuario.get(clave_seleccionada)
            if viaje_encontrado:
                gastos = viaje_encontrado.get("Gastos", [])
                info_gasto = [descripcion, gasto, fecha]
                gastos.append(info_gasto)
                viaje_encontrado["Gastos"] = gastos
                self.viajes_usuario[clave_seleccionada] = viaje_encontrado


                self.mostrar_exito("El gasto se ha agregado correctamente")
                self.actualizar_gastos_del_viaje()
            else:
                self.mostrar_warning("Viaje no encontrado")

    def eliminar_gasto(self):
        clave_seleccionada = self.seleccionar_viaje_gasto.currentData()
        if clave_seleccionada is not None:
            viaje_encontrado = self.viajes_usuario.get(clave_seleccionada)
            if viaje_encontrado:
                gastos = viaje_encontrado.get("Gastos", [])
                gasto_seleccionado = self.list_widget_gastos.currentItem()
                if gasto_seleccionado:
                    item_index = self.list_widget_gastos.row(gasto_seleccionado)
                    confirmacion = QMessageBox.question(self, "Confirmar eliminación", "¿Está seguro de que desea eliminar este gasto?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if confirmacion == QMessageBox.Yes:
                        self.list_widget_gastos.takeItem(item_index)
                        if 0 <= item_index < len(gastos):
                            del gastos[item_index]
                        viaje_encontrado["Gastos"] = gastos
                        self.viajes_usuario[clave_seleccionada] = viaje_encontrado
                        self.mostrar_exito("El gasto se ha eliminado correctamente")
                        self.actualizar_gastos_del_viaje()
                else:
                    self.mostrar_warning("Seleccione un gasto para eliminar")
            else:
                self.mostrar_warning("Viaje no encontrado")
            
    def listar_viajes(self):
        if self.viajes_usuario:
            viajes_ordenados = sorted(self.viajes_usuario.items(), key=lambda x: x[0], reverse=True)
            self.list_widget_viajes_guardados.clear()
            self.seleccionar_viaje_gasto.clear()
            self.seleccionar_viaje_itinerario.clear()
            for i, viaje in viajes_ordenados:
                texto_titulo = viaje["titulo"]
                texto_destino = viaje["destino"]
                lista_fechas_inicio = viaje["fecha_inicio"]
                lista_fechas_fin = viaje["fecha_fin"]
                presupuesto = viaje["presupuesto"]
                personas_de_viaje = viaje["personas"]
                vuelos = viaje.get("vuelos", {})
                alojamiento = viaje.get("alojamiento", {})
                itinerario = viaje.get("Itinerario", [])
                gastos = viaje.get("Gastos", [])

                texto_combo = f"Título: {texto_titulo} - Destino: {texto_destino} - Numero de personas: {personas_de_viaje}"

                travel_widget = TravelWidget(i, texto_titulo, texto_destino, lista_fechas_inicio, lista_fechas_fin, presupuesto, personas_de_viaje, vuelos, alojamiento, itinerario, gastos)
                item = QListWidgetItem(self.list_widget_viajes_guardados)
                item.setSizeHint(travel_widget.sizeHint())
                self.list_widget_viajes_guardados.addItem(item)
                self.list_widget_viajes_guardados.setItemWidget(item, travel_widget)
                self.seleccionar_viaje_gasto.addItem(texto_combo, userData=i)  
                self.seleccionar_viaje_itinerario.addItem(texto_combo, userData=i)
            self.list_widget_viajes_guardados.scrollToTop()

    def cargar_viajes_iniciales(self):
        self.viajes_usuario = {
            1: {
                "titulo": "Viaje a Paris",
                "destino": "Paris, Francia",
                "fecha_inicio": ["01", "Ene", 2024],
                "fecha_fin": ["10", "Ene", 2024],
                "presupuesto": 5000,
                "personas": 2,
                "vuelos": {
                    "fecha_ida": "01-Ene-2024",
                    "hora_ida": "10:00",
                    "ampm_ida": "AM",
                    "fecha_regreso": "10-Ene-2024",
                    "hora_regreso": "08:00",
                    "ampm_regreso": "PM",
                    "costo_ida": 500,
                    "costo_regreso": 500,
                    "info_adicional": "Vuelos directos"
                },
                "alojamiento": {
                    "Tipo": "Hotel",
                    "fecha_inicio": "01-Ene-2024",
                    "hora_inicio": "12:00",
                    "ampm_inicio": "PM",
                    "fecha_fin": "10-Ene-2024",
                    "hora_fin": "10:00",
                    "ampm_fin": "AM",
                    "costo": 500,
                    "info_adicional": "Hotel de 4 estrellas"
                }, 
                "Itinerario": [["Ir de compras", "12:00", "AM", "11-11-2024"],
                               ["Ir al monte fuji", "5:00", "AM", "12-11-2024"],
                               ["Salir a cenar", "7:00", "PM", "13-11-2024"]], 
                "Gastos": [["Pan con queso", 2000, "18-11-2024"]],
            },
            2: {
                "titulo": "Viaje a Tokio",
                "destino": "Tokio, Japón",
                "fecha_inicio": ["15", "Feb", 2024],
                "fecha_fin": ["25", "Feb", 2024],
                "presupuesto": 3000,
                "personas": 1,
                "vuelos": {
                    "fecha_ida": "15-Feb-2024",
                    "hora_ida": "05:00",
                    "ampm_ida": "AM",
                    "fecha_regreso": "25-Feb-2024",
                    "hora_regreso": "11:00",
                    "ampm_regreso": "AM",
                    "costo_ida": 1000,
                    "costo_regreso": 1000,
                    "info_adicional": "Escala en Los Ángeles"
                },
                "alojamiento": {
                    "Tipo": "Airbnb",
                    "fecha_inicio": "15-Feb-2024",
                    "hora_inicio": "02:00",
                    "ampm_inicio": "PM",
                    "fecha_fin": "25-Feb-2024",
                    "hora_fin": "10:00",
                    "ampm_fin": "AM",
                    "costo": 12000,
                    "info_adicional": "Airbnb en el centro de la ciudad"
                },
                "Itinerario": [], 
                "Gastos": [["Cena elegante", 20000, "23-11-2024"],
                           ["Pan con queso", 22000, "18-11-2024"],
                           ["Almojabanas", 12000, "18-11-2024"]]
            }
        }
        self.indice_viajes_guardados = max(self.viajes_usuario.keys())

    def validar_fecha_hora(self, fecha, hora, ampm, tipo):
        # Validar formato de fecha
        try:
            datetime.datetime.strptime(fecha, '%d-%m-%Y')
        except ValueError:
            self.mostrar_warning(f"El formato de la fecha de {tipo} no es válido.")
            return False

        # Validar formato de hora
        if not re.match(r'^[0-1]?[0-9]:[0-5][0-9]$', hora):
            self.mostrar_warning(f"El formato de la hora de {tipo} no es válido. Use HH:MM")
            return False

        # Validar rango de hora y AM/PM
        horas, minutos = map(int, hora.split(':'))
        if (horas < 1 or horas > 12) or (horas == 12 and minutos == 0 and ampm == "PM"):
            self.mostrar_warning(f"Hora de {tipo} no válida. Las horas deben estar entre 01 y 12.")
            return False

        return True
    
    def validar_solo_fecha(self, fecha, tipo):
        try:
            datetime.datetime.strptime(fecha, '%d-%m-%Y')
        except ValueError:
            self.mostrar_warning(f"El formato de la fecha de {tipo} no es válido.")
            return False
        return True

    def comparar_fechas(self, dia_inicio, mes_inicio, año_inicio, dia_fin, mes_fin, año_fin):
        dia_inicio, mes_inicio, año_inicio, dia_fin, mes_fin, año_fin = map(int, [dia_inicio, mes_inicio, año_inicio, dia_fin, mes_fin, año_fin])
        fecha_inicio = datetime.date(año_inicio, mes_inicio, dia_inicio)
        fecha_fin = datetime.date(año_fin, mes_fin, dia_fin)
        return fecha_fin >= fecha_inicio

    def comparar_fechas_vuelo(self, fecha_ida, fecha_regreso):
        fecha_ida_dt = datetime.datetime.strptime(fecha_ida, '%d-%m-%Y')
        fecha_regreso_dt = datetime.datetime.strptime(fecha_regreso, '%d-%m-%Y')
        return fecha_regreso_dt >= fecha_ida_dt

    def activar_alojamiento(self):
        if self.checkbox_alojaimento_nuevo_viaje.isChecked():
            self.groupbox_alojamiento_viaje.setEnabled(True)
        else:
            self.groupbox_alojamiento_viaje.setEnabled(False)

    def activar_regreso_ida_avion(self):
        if self.checkbox_vuelos_nuevo_viaje.isChecked():
            self.grupo_regreso_viaje.setEnabled(True)
            self.grupo_ida_viaje.setEnabled(True)
        else:
            self.grupo_regreso_viaje.setEnabled(False)
            self.grupo_ida_viaje.setEnabled(False)

    def reset_formulario_nuevo_viaje(self):
        self.lineedit_titulo_nuevo_viaje.clear()
        self.lineedit_destino_nuevo_viaje.clear()
        self.lineedit_fechainicio_nuevo_viaje.clear()
        self.lineedit_fechafin_nuevo_viaje.clear()
        self.lineedit_presupuesto_nuevo_viaje.clear()
        self.boton_solo_nuevo_viaje.setChecked(True)
        self.boton_pareja_nuevo_viaje.setChecked(False)
        self.boton_familia_nuevo_viaje.setChecked(False)
        self.line_edit_familia_nuevo_viaje.clear()
        self.line_edit_familia_nuevo_viaje.setEnabled(False)
        self.checkbox_vuelos_nuevo_viaje.setChecked(False)
        self.lineedit_fecha_ida_nuevo_viaje.clear()
        self.lineedit_hora_ida_nuevo_viaje.clear()
        self.combobox_ampm_hora_ida_nuevo_viaje.setCurrentIndex(0)
        self.lineedit_fecha_regreso_nuevo_viaje.clear()
        self.lineedit_hora_regreso_nuevo_viaje.clear()
        self.combobox_ampm_hora_regreso_nuevo_viaje.setCurrentIndex(0)
        self.lineedit_costo_ida_nuevo_viaje.clear()
        self.lineedit_costo_regreso_nuevo_viaje.clear()
        self.checkbox_alojaimento_nuevo_viaje.setChecked(False)
        self.combobox_hote_o_airbnb_nuevo_viaje.setCurrentIndex(0)
        self.lineedit_direccion_nuevo_viaje.clear()
        self.lineedit_fecha_inicio_alojamiento_nuevo_viaje.clear()
        self.combobox_ampm_hora_inicio_nuevo_viaje_alojamiento.setCurrentIndex(0)
        self.lineedit_hora_inicio_nuevo_viaje_alojamiento.clear()
        self.lineedit_hora_fin_nuevo_viaje_alojamiento.clear()
        self.lineedit_fecha_fin_alojamiento_nuevo_viaje.clear()
        self.combobox_ampm_hora_fin_nuevo_viaje_alojamiento.setCurrentIndex(0)
        self.line_edit_costo_alojamiento_nuevo_viaje.clear()
        self.plaintextedit_info_adicional_nuevo_viaje.clear()



    def activar_edicion_de_perfil(self):
        if self.edit_profile_2.text() == "Editar perfil":
            self.cargar_telefono()
            self.open_pic_to_profile_pic_2.setHidden(False)
            self.delete_profile_pic_2.setHidden(False)
            self.edit_profile_2.setText("Guardar")
            self.open_pic_to_profile_pic_2.setCheckable(True)
            self.open_pic_to_profile_pic_2.setEnabled(True)
            self.delete_profile_pic_2.setEnabled(True)
            self.delete_profile_pic_2.setCheckable(True)
            self.sexo_groupbox_profile_2.setEnabled(True)
            self.name_edit_profile_2.setEnabled(True)
            self.lastname_edit_profile_2.setEnabled(True)
            self.age_spinbox_profile_2.setEnabled(True)
            self.email_edit_profile_2.setEnabled(True)
            self.pass_edit_profile_2.setEnabled(True)
            self.id_edit_profile_2.setEnabled(True)
            self.country_edit_profile_2.setEnabled(True)
            self.passport_edit_profile_2.setEnabled(True)
            self.adress_edit_profile_2.setEnabled(True)
            self.telefono_edit_profile_3.setEnabled(True)
            self.biography_paintext_profile_2.setEnabled(True)
        else:
            if all(self.validar_formulario()):
                self.open_pic_to_profile_pic_2.setHidden(True)
                self.delete_profile_pic_2.setHidden(True)
                self.edit_profile_2.setText("Editar perfil")
                self.open_pic_to_profile_pic_2.setCheckable(False)
                self.open_pic_to_profile_pic_2.setEnabled(False)
                self.delete_profile_pic_2.setEnabled(False)
                self.delete_profile_pic_2.setCheckable(False)
                self.sexo_groupbox_profile_2.setEnabled(False)
                self.name_edit_profile_2.setEnabled(False)
                self.lastname_edit_profile_2.setEnabled(False)
                self.age_spinbox_profile_2.setEnabled(False)
                self.email_edit_profile_2.setEnabled(False)
                self.pass_edit_profile_2.setEnabled(False)
                self.id_edit_profile_2.setEnabled(False)
                self.country_edit_profile_2.setEnabled(False)
                self.passport_edit_profile_2.setEnabled(False)
                self.adress_edit_profile_2.setEnabled(False)
                self.telefono_edit_profile_3.setEnabled(False)
                self.biography_paintext_profile_2.setEnabled(False)
                self.actualizar_progreso()
            
    #Validar que todo este correcto en el perfil
    def validar_formulario(self):
        return [
            self.validar_nombre(),
            self.validar_sexo(),
            self.validar_apellido(),
            self.validar_id(),
            self.validar_email(),
            self.validar_password(),
            self.validar_biografia(),
            self.validar_direccion(),
            self.validar_telefono(),
            self.validar_pasaporte(),
            self.validar_nacionalidad(),
            self.validar_edad()
            ]

    #Funcion de mostrar alerta
    def mostrar_warning(self, message):
        QMessageBox.warning(self, "Advertencia", message)
    
    def mostrar_exito(self, message):
        QMessageBox.information(self, "Información", message)

    #Validaciones del perfil desde la linea 158 hasta 394
    def validar_nombre(self):
        nombre = self.name_edit_profile_2.text().strip()
        if not nombre:
            self.mostrar_warning("El nombre no puede estar vacío.")
            return False
        elif not re.match(r'^[a-zA-Z\s]+$', nombre):
            self.mostrar_warning("El nombre no puede contener caracteres especiales ni dígitos.")
            return False
        elif len(nombre.split()) > 3:
            self.mostrar_warning("No puede haber más de tres nombres.")
            return False
        else:
            nombre = ' '.join(nombre.split()).title()
            self.name_edit_profile_2.setText(nombre)
            if not self.paso_nombre_validado:
                self.paso_nombre_validado = True
            return True

    def validar_apellido(self):
        apellido = self.lastname_edit_profile_2.text().strip()
        if not apellido:
            self.mostrar_warning("El apellido no puede estar vacío.")
            return False
        elif not re.match(r'^[a-zA-Z\s]+$', apellido):
            self.mostrar_warning("El apellido no puede contener caracteres especiales ni dígitos.")
            return False
        elif len(apellido.split()) > 3:
            self.mostrar_warning("No puede haber más de tres apellidos.")
            return False
        else:
            apellido = ' '.join(apellido.split()).title()
            self.lastname_edit_profile_2.setText(apellido)
            if not self.paso_apellido_validado:
                self.paso_apellido_validado = True
            return True

    def validar_email(self):
        email = self.email_edit_profile_2.text()
        if email.strip() == "":
            self.mostrar_warning("El email no puede estar vacio.")
            return False
            
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email.strip()):
            self.mostrar_warning("Debe colocar un email válido.")
            return False
        return True
    
    def validar_password(self):
        password = self.pass_edit_profile_2.text()
        if password.strip() == "":
            self.mostrar_warning("La contraseña no puede estar vacía.")
            return False

        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(password_regex, password.strip()):
            self.mostrar_warning("La contraseña debe contener al menos 8 caracteres, incluyendo una letra mayúscula, una letra minúscula y un número. No se permiten caracteres especiales.")
            return False
        return True
    
    def validar_id(self):
        ti_o_cc = self.id_edit_profile_2.text()
        if ti_o_cc.strip() == "":
            self.id_edit_profile_2.setText("")
            if self.ti_o_cc_validado:
                self.pasos_completados -= 1
                self.ti_o_cc_validado = False
            return True
        elif all(i.isdigit() or i.isspace() for i in ti_o_cc.strip()):
            identificacion_sin_espacios = ''.join(ti_o_cc.split())
            self.id_edit_profile_2.setText(identificacion_sin_espacios)
            if not self.ti_o_cc_validado:
                self.ti_o_cc_validado = True
                self.pasos_completados += 1
            return True
        else:
            self.mostrar_warning("El número de identificación no puede tener letras o caracteres especiales")
            return False
            
    def validar_sexo(self):
        if self.none_radio_profile_2.isChecked():
            if self.paso_escoger_sexualidad:
                self.paso_escoger_sexualidad = False
                self.pasos_completados -= 1
                self.actualizar_progreso()
        else:
            if not self.paso_escoger_sexualidad:
                self.paso_escoger_sexualidad = True
                self.pasos_completados += 1
                self.actualizar_progreso()
        return True
    
    def validar_nacionalidad(self):
        nacionalidad = self.country_edit_profile_2.currentText().strip()
        if nacionalidad == "" or nacionalidad == "No Especificar":
            if self.nacionalidad_validada:
                self.nacionalidad_validada = False
                self.pasos_completados -= 1
            return True
        elif not re.match(r'^[a-zA-Z\s]+$', nacionalidad):
            if self.nacionalidad_validada:
                self.nacionalidad_validada = False
                self.pasos_completados -= 1
            self.mostrar_warning("La nacionalidad solo puede contener letras.")
            return False
        else:
            nacionalidad = ' '.join(nacionalidad.split()).title()
            self.country_edit_profile_2.setCurrentText(nacionalidad)
            if not self.nacionalidad_validada:
                self.nacionalidad_validada = True
                self.pasos_completados += 1
            return True

    def validar_edad(self):
        edad = self.age_spinbox_profile_2.value()
        if edad < 16:
            if self.edad_validada:
                self.edad_validada = False
                self.pasos_completados -= 1
            self.mostrar_warning("Debe tener al menos 16 años.")
            return False
        else:
            if not self.edad_validada:
                self.edad_validada = True
                self.pasos_completados += 1
            return True
        
    def validar_biografia(self):
        biografia = self.biography_paintext_profile_2.toPlainText().strip()
        if biografia == "":
            if self.biografia_validada:
                self.biografia_validada = False
                self.pasos_completados -= 1
            return True
        else:
            if not self.biografia_validada:
                self.biografia_validada = True
                self.pasos_completados += 1
            return True

    def validar_direccion(self):
        direccion = self.adress_edit_profile_2.text().strip()
        if direccion == "":
            if self.direccion_validada:
                self.direccion_validada = False
                self.pasos_completados -= 1
            return True
        else:
            if not self.direccion_validada:
                self.direccion_validada = True
                self.pasos_completados += 1
            return True
        
    def cargar_telefono(self):
        telefono = self.telefono_edit_profile_3.text()
        if telefono.startswith("+"):
            if telefono:
                prefijo_numero = self.telefono_edit_profile_3.text().split(" ")
                self.telefono_edit_profile_3.setText(f"{prefijo_numero[1]}")
        
    def validar_telefono(self):
        telefono = self.telefono_edit_profile_3.text().strip()
        nacionalidad = self.country_edit_profile_2.currentText().strip()
        
        if telefono == "":
            if self.telefono_validado:
                self.telefono_validado = False
                self.pasos_completados -= 1
            return True
        elif nacionalidad == "Colombia" and not re.match(r'^\d+$', telefono):
            self.mostrar_warning("El número de teléfono solo puede contener números para la nacionalidad Colombia.")
            return False
        else:
            if nacionalidad == "Colombia":
                telefono = f"+57 {telefono}"
            self.telefono_edit_profile_3.setText(telefono)
            if not self.telefono_validado:
                self.telefono_validado = True
                self.pasos_completados += 1
            return True

    def validar_pasaporte(self):
        pasaporte = self.passport_edit_profile_2.text().strip()
        if pasaporte == "":
            if self.pasaporte_validado:
                self.pasaporte_validado = False
                self.pasos_completados -= 1
            return True
        elif not re.match(r'^[A-Za-z0-9]+$', pasaporte):
            self.mostrar_warning("El pasaporte solo puede contener letras y números.")
            return False
        else:
            self.passport_edit_profile_2.setText(pasaporte)
            if not self.pasaporte_validado:
                self.pasaporte_validado = True
                self.pasos_completados += 1
            return True

    def cargar_foto_de_perfil(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            nueva_foto = QPixmap(file_name).scaled(QSize(self.label_myprofile_page_photo_2.width(), self.label_myprofile_page_photo_2.height()), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.poner_foto_de_perfil(nueva_foto)

    def borrar_foto_de_perfil(self):
        if self.paso_foto_de_perfil:
            foto_por_defecto = QPixmap(os.path.join(self.basedir, "icons/sinfoto.png")).scaled(QSize(self.label_myprofile_page_photo_2.width(), self.label_myprofile_page_photo_2.height()), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.pasos_completados -= 1
            self.label_myprofile_page_photo_2.setPixmap(foto_por_defecto)
            self.label_pic_small1.setPixmap(foto_por_defecto)
            self.label_pic_small2.setPixmap(foto_por_defecto)
            self.paso_foto_de_perfil = False
            self.actualizar_progreso()

    def poner_foto_de_perfil(self, pixmap):
        if not self.paso_foto_de_perfil:
            self.pasos_completados += 1
            self.label_myprofile_page_photo_2.setPixmap(pixmap)
            self.label_pic_small1.setPixmap(pixmap)
            self.label_pic_small2.setPixmap(pixmap)
            self.paso_foto_de_perfil = True
            self.actualizar_progreso()
        else:
            self.label_myprofile_page_photo_2.setPixmap(pixmap)
            self.label_pic_small1.setPixmap(pixmap)
            self.label_pic_small2.setPixmap(pixmap)

    def actualizar_progreso(self):
        self.progressbar_profile_2.setMaximum(self.pasos_totales)
        self.progressbar_profile_2.setValue(self.pasos_completados)

        if self.pasos_completados == self.pasos_totales:
            self.label_progressbar_profile_2.setText("Perfil Completo")
        else:
            self.label_progressbar_profile_2.setText(f"Completa tu perfil       {self.pasos_completados}/{self.pasos_totales}")

    #Funcion de actualizar reloj
    def update_time(self):
        #Actualiza el reloj
        current_time = QTime.currentTime()
        hours = current_time.hour()
        minutes = current_time.minute()

        self.Horas.display(hours)
        self.minutos.display(minutes)

    #Mostrar paginas del dashboard y sub stacketwidgets
    def mostrar_pagina_de_soporte(self):
        self.configuraciones_stacked.setCurrentIndex(1)

    def mostrar_pagina_about_us(self):
        self.configuraciones_stacked.setCurrentIndex(2)

    def mostrar_pagina_botones_configuraciones(self):
        self.configuraciones_stacked.setCurrentIndex(0)

    def mostrar_agregar_nuevo_recordatorio(self):
        self.notifications_stacked.setCurrentIndex(1)

    def mostrar_pagina_recordatorios(self):
        self.notifications_stacked.setCurrentIndex(0)
        self.lineedit_hora_recordatorio.clear()
        self.lineedit_fecha_recordatorio.clear()
        self.text_edit_recordatorio.clear()
        self.checkbox_lugar_recordatorio.setChecked(False)
        self.check_box_hora_recordatorio.setChecked(False)


    def mostrar_pagina_notificaciones(self):
        self.stackedWidget.setCurrentWidget(self.notifications_page)
        self.cargar_recordatorios()


    def mostrar_pagina_perfil(self):
        self.stackedWidget.setCurrentWidget(self.profile_page)

    def mostrar_pagina_home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)

    def mostrar_pagina_mis_viajes(self):
        self.stackedWidget.setCurrentWidget(self.mis_viajes_page)

    def mostrar_pagina_nuevo_viaje(self):
        self.stackedWidget.setCurrentWidget(self.nuevo_viaje_page)

    def mostrar_pagina_itinerario(self):
        self.stackedWidget.setCurrentWidget(self.Iinerario_page)

    def mostrar_pagina_gastos(self):
        self.stackedWidget.setCurrentWidget(self.gastos_page)


    def mostrar_configuraciones_page(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
