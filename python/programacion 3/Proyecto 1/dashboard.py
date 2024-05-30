from ui_viajes_final_ui import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os
import re

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QApplication
import sys

class TravelWidget(QWidget):
    def __init__(self, indice, titulo, destino, datos_fecha_viaje_inicio, datos_fecha_viaje_fin, presupuesto=None):
        super().__init__()

        # Estilos para el widget
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                border-radius: 10px;
                padding: 10px;
            }
            QLabel {
                font-family: "Arial", sans-serif;
            }
            QLabel[objectName^="label_"] {
                font-weight: bold;
            }
        """)

        # Diseño horizontal
        layout = QHBoxLayout(self)

        # Primer cuadro: Título y Destino
        title_dest_layout = QVBoxLayout()

        title_label = QLabel(titulo)
        title_label.setObjectName("label_title")
        title_label.setStyleSheet("color: #4CAF50;")
        title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        title_label.setWordWrap(True)
        title_dest_layout.addWidget(title_label)

        destination_label = QLabel(destino)
        destination_label.setObjectName("label_destination")
        destination_label.setStyleSheet("color: #9C27B0;")
        destination_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        destination_label.setWordWrap(True)
        title_dest_layout.addWidget(destination_label)

        layout.addLayout(title_dest_layout)

        # Segundo cuadro: Fecha de inicio
        start_date_layout = QVBoxLayout()

        start_date_label = QLabel("Fecha de inicio")
        start_date_label.setObjectName("label_start_date_title")
        start_date_label.setStyleSheet("color: #2196F3;")
        start_date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        start_date_label.setWordWrap(True)
        start_date_layout.addWidget(start_date_label)

        start_day_value_label = QLabel(f"Día: {datos_fecha_viaje_inicio[0]}")
        start_day_value_label.setObjectName("label_start_day_value")
        start_day_value_label.setStyleSheet("color: #2196F3;")
        start_day_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        start_day_value_label.setWordWrap(True)
        start_date_layout.addWidget(start_day_value_label)

        start_month_value_label = QLabel(f"Mes: {datos_fecha_viaje_inicio[1]}")
        start_month_value_label.setObjectName("label_start_month_value")
        start_month_value_label.setStyleSheet("color: #2196F3;")
        start_month_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        start_month_value_label.setWordWrap(True)
        start_date_layout.addWidget(start_month_value_label)

        start_year_value_label = QLabel(f"Año: {datos_fecha_viaje_inicio[2]}")
        start_year_value_label.setObjectName("label_start_year_value")
        start_year_value_label.setStyleSheet("color: #2196F3;")
        start_year_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        start_year_value_label.setWordWrap(True)
        start_date_layout.addWidget(start_year_value_label)

        layout.addLayout(start_date_layout)

        # Tercer cuadro: Fecha de fin
        end_date_layout = QVBoxLayout()

        end_date_label = QLabel("Fecha de fin")
        end_date_label.setObjectName("label_end_date_title")
        end_date_label.setStyleSheet("color: #2196F3;")
        end_date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        end_date_label.setWordWrap(True)
        end_date_layout.addWidget(end_date_label)

        end_day_value_label = QLabel(f"Día: {datos_fecha_viaje_fin[0]}")
        end_day_value_label.setObjectName("label_end_day_value")
        end_day_value_label.setStyleSheet("color: #2196F3;")
        end_day_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        end_day_value_label.setWordWrap(True)
        end_date_layout.addWidget(end_day_value_label)

        end_month_value_label = QLabel(f"Mes: {datos_fecha_viaje_fin[1]}")
        end_month_value_label.setObjectName("label_end_month_value")
        end_month_value_label.setStyleSheet("color: #2196F3;")
        end_month_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        end_month_value_label.setWordWrap(True)
        end_date_layout.addWidget(end_month_value_label)

        end_year_value_label = QLabel(f"Año: {datos_fecha_viaje_fin[2]}")
        end_year_value_label.setObjectName("label_end_year_value")
        end_year_value_label.setStyleSheet("color: #2196F3;")
        end_year_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        end_year_value_label.setWordWrap(True)
        end_date_layout.addWidget(end_year_value_label)

        layout.addLayout(end_date_layout)

        self.setLayout(layout)

        # Ajustar políticas de tamaño
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        title_dest_layout.setSizeConstraint(QLayout.SetMinimumSize)
        start_date_layout.setSizeConstraint(QLayout.SetMinimumSize)
        end_date_layout.setSizeConstraint(QLayout.SetMinimumSize)


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

    meses = {1: "Enero",
             2: "Febrero",
             3: "Marzo",
             4: "Abril",
             5: "Mayo",
             6: "Junio",
             7: "Julio",
             8: "Agosto",
             9: "Septiembre",
             10: "Octubre",
             11: "Noviembre",
             12: "Diciembre"}

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

        self.actualizar_progreso()
        

        #Botones de la pagina nuevo viaje
        self.checkbox_vuelos_nuevo_viaje.stateChanged.connect(self.activar_regreso_ida_avion)
        self.checkbox_alojaimento_nuevo_viaje.stateChanged.connect(self.activar_alojamiento)
        self.save_new_travel_button.clicked.connect(self.evaluar_viaje)
        self.eliminar_viajeguardado_button.clicked.connect(self.eliminar_viaje_guardado)
        self.boton_familia_nuevo_viaje.clicked.connect(self.activar_line_edit_familia)
        self.boton_solo_nuevo_viaje.clicked.connect(self.activar_line_edit_familia)
        
    
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
            self.mostrar_warning("El Destino del viaje es obligatorio")
            return
        
        fecha_inicio = self.lineedit_fechainicio_nuevo_viaje.text()
        fecha_fin = self.lineedit_fechafin_nuevo_viaje.text()

        if fecha_inicio.strip() == "" or fecha_fin.strip() == "":
            if fecha_inicio.strip() == "":
                formato_fecha_inicio = "N/A"
            if fecha_fin.strip() == "":
                formato_fecha_fin = "N/A"
        else:
            lista_fechas_inicio = fecha_inicio.split("-")
            lista_fechas_fin = fecha_fin.split("-")
            indicador_de_mes_fin = None
            indicador_de_mes_inicio = None
            if len(lista_fechas_inicio) == 3 and lista_fechas_inicio[0].isdigit() and lista_fechas_inicio[1].isalnum() and lista_fechas_inicio[2].isdigit():
                for i, mes in self.meses.items():
                    if lista_fechas_inicio[1].capitalize() == mes:
                        indicador_de_mes_inicio = i
                        break
                if not indicador_de_mes_inicio:
                    self.mostrar_warning("El mes es incorrecto, escriba el mes correctamente")
                    return
            
            if len(lista_fechas_fin) == 3 and lista_fechas_fin[0].isdigit() and lista_fechas_fin[1].isalnum() and lista_fechas_fin[2].isdigit():
                for i, mes in self.meses.items():
                    if lista_fechas_fin[1].capitalize() == mes:
                        indicador_de_mes_fin = i
                        break
                if not indicador_de_mes_fin:
                    self.mostrar_warning("El mes es incorrecto, escriba el mes correctamente")
                    return
            else:
                self.mostrar_warning("El formato de fecha no es valido")
                return
            
            if indicador_de_mes_inicio and indicador_de_mes_fin:
                dia_inicio_viaje, mes_inicio_viaje, año_inicio_viaje = int(lista_fechas_inicio[0]), indicador_de_mes_inicio, int(lista_fechas_inicio[2])
                dia_fin_viaje, mes_fin_viaje, año_fin_viaje = int(lista_fechas_fin[0]), indicador_de_mes_fin, int(lista_fechas_fin[2])
                fechas_validadas = self.comparar_fechas(dia_inicio_viaje, mes_inicio_viaje, año_inicio_viaje, dia_fin_viaje, mes_fin_viaje, año_fin_viaje)
                if not fechas_validadas:
                    self.mostrar_warning("La fecha de fin no puede ser antes de la fecha de inicio")
                    return
                
        presupuesto = self.lineedit_presupuesto_nuevo_viaje.text().strip()

        if presupuesto.isdigit() or presupuesto == "":
            if presupuesto == "":
                presupuesto = 0
            elif presupuesto.isdigit():
                presupuesto = int(presupuesto)
        else:
            self.mostrar_warning("El presupuesto del viaje debe ser un número")
            return
        
        personas_de_viaje = None
        if self.boton_solo_nuevo_viaje.isChecked():
            personas_de_viaje = 1
        elif self.boton_pareja_nuevo_viaje.isChecked():
            personas_de_viaje = 2
        else:
            if self.boton_familia_nuevo_viaje.isChecked():
                personas_de_viaje = self.line_edit_familia_nuevo_viaje.text().strip()
                if personas_de_viaje == "" or personas_de_viaje.isalpha():
                    self.mostrar_warning("Debe colocar el numero de integrantes de la familia")
                    return
                elif personas_de_viaje.isdigit():
                    personas_de_viaje = int(personas_de_viaje)


        vuelos_completados = True
        alojamiento_completado = True

        if self.checkbox_vuelos_nuevo_viaje.isChecked():
            vuelos_completados = False

        if self.checkbox_alojaimento_nuevo_viaje.isChecked():
            alojamiento_completado = False
        
        if vuelos_completados and alojamiento_completado:
            indice = self.list_widget_viajes_guardados.count() + 1
            travel_widget = TravelWidget(indice, texto_titulo, texto_destino, lista_fechas_inicio, lista_fechas_fin, presupuesto)
            item = QListWidgetItem(self.list_widget_viajes_guardados)
            item.setSizeHint(travel_widget.sizeHint())
            self.list_widget_viajes_guardados.addItem(item)
            self.list_widget_viajes_guardados.setItemWidget(item, travel_widget)

            self.mostrar_exito("El viaje se ha agregado correctamente")
        else:
            self.mostrar_warning("Por favor, complete la información de los vuelos.")


    def comparar_fechas(self, dia_inicio, mes_inicio, año_inicio, dia_fin, mes_fin, año_fin):
        if año_fin < año_inicio:
            return False
        if año_fin == año_inicio:
            if mes_fin < mes_inicio:
                return False
            if mes_fin == mes_inicio:
                if dia_fin < dia_inicio:
                    return False
        return True

    def eliminar_viaje_guardado(self):
        viaje_seleccionado = self.list_widget_viajes_guardados.currentItem()
        if viaje_seleccionado:
            item = self.list_widget_viajes_guardados.row(viaje_seleccionado)
            self.list_widget_viajes_guardados.takeItem(item)  
    
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

    def mostrar_pagina_notificaciones(self):
        self.stackedWidget.setCurrentWidget(self.notifications_page)

    def mostrar_configuraciones_page(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test_widget = TravelWidget(1, "Vacaciones", "Paris", [15, 6, 2024], [22, 6, 2024])
    window = MainApp()
    window.show()
    sys.exit(app.exec())

