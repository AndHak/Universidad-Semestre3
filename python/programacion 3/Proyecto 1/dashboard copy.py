from ui_viajes_final_ui import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os
import re
import datetime

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QApplication
import sys

class TravelWidget(QWidget):
    def __init__(self, indice, titulo, destino, datos_fecha_viaje_inicio, datos_fecha_viaje_fin, presupuesto=0, personas="1", vuelos=None, alojamiento=None):
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

        # Primer cuadro: Título, Destino, Presupuesto, y Personas
        title_dest_layout = QVBoxLayout()

        title_label = QLabel(f"Título: {titulo}")
        title_label.setObjectName("label_title")
        title_label.setStyleSheet("color: rgb(27, 73, 101); font-size: 16px;")
        title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        title_label.setWordWrap(True)
        title_dest_layout.addWidget(title_label)

        destination_label = QLabel(f"Destino: {destino}")
        destination_label.setObjectName("label_destination")
        destination_label.setStyleSheet("color: #9C27B0;")
        destination_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        destination_label.setWordWrap(True)
        title_dest_layout.addWidget(destination_label)

        budget_label = QLabel(f"Presupuesto: {presupuesto}")
        budget_label.setObjectName("label_budget")
        budget_label.setStyleSheet("color: #4CAF50;")
        budget_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        budget_label.setWordWrap(True)
        title_dest_layout.addWidget(budget_label)

        people_label = QLabel(f"Personas: {personas}")
        people_label.setObjectName("label_people")
        people_label.setStyleSheet("color: #FF9800;")
        people_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        people_label.setWordWrap(True)
        title_dest_layout.addWidget(people_label)

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

        # Cuarto cuadro: Detalles de vuelos
        if vuelos:
            vuelos_layout = QVBoxLayout()
            
            vuelos_label = QLabel("Vuelos")
            vuelos_label.setObjectName("label_vuelos_title")
            vuelos_label.setStyleSheet("color: #FF5722;")
            vuelos_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            vuelos_label.setWordWrap(True)
            vuelos_layout.addWidget(vuelos_label)

            vuelos_content_layout = QHBoxLayout()

            # Ida
            ida_layout = QVBoxLayout()
            ida_label = QLabel("Ida")
            ida_label.setObjectName("label_ida_title")
            ida_label.setStyleSheet("color: #FF5722;")
            ida_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            ida_label.setWordWrap(True)
            ida_layout.addWidget(ida_label)

            fecha_ida_label = QLabel(f"Fecha: {vuelos['fecha_ida']}")
            fecha_ida_label.setObjectName("label_fecha_ida")
            fecha_ida_label.setStyleSheet("color: #FF5722;")
            fecha_ida_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            fecha_ida_label.setWordWrap(True)
            ida_layout.addWidget(fecha_ida_label)

            hora_ida_label = QLabel(f"Hora: {vuelos['hora_ida']} {vuelos['ampm_ida']}")
            hora_ida_label.setObjectName("label_hora_ida")
            hora_ida_label.setStyleSheet("color: #FF5722;")
            hora_ida_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            hora_ida_label.setWordWrap(True)
            ida_layout.addWidget(hora_ida_label)

            costo_ida_label = QLabel(f"Costo: ${vuelos['costo_ida'] if vuelos['costo_ida'] else 'N/A'}")
            costo_ida_label.setObjectName("label_costo_ida")
            costo_ida_label.setStyleSheet("color: #FF5722;")
            costo_ida_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            costo_ida_label.setWordWrap(True)
            ida_layout.addWidget(costo_ida_label)

            vuelos_content_layout.addLayout(ida_layout)

            # Regreso
            regreso_layout = QVBoxLayout()
            regreso_label = QLabel("Regreso")
            regreso_label.setObjectName("label_regreso_title")
            regreso_label.setStyleSheet("color: #FF5722;")
            regreso_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            regreso_label.setWordWrap(True)
            regreso_layout.addWidget(regreso_label)

            fecha_regreso_label = QLabel(f"Fecha: {vuelos['fecha_regreso']}")
            fecha_regreso_label.setObjectName("label_fecha_regreso")
            fecha_regreso_label.setStyleSheet("color: #FF5722;")
            fecha_regreso_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            fecha_regreso_label.setWordWrap(True)
            regreso_layout.addWidget(fecha_regreso_label)

            hora_regreso_label = QLabel(f"Hora: {vuelos['hora_regreso']} {vuelos['ampm_regreso']}")
            hora_regreso_label.setObjectName("label_hora_regreso")
            hora_regreso_label.setStyleSheet("color: #FF5722;")
            hora_regreso_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            hora_regreso_label.setWordWrap(True)
            regreso_layout.addWidget(hora_regreso_label)

            costo_regreso_label = QLabel(f"Costo: ${vuelos['costo_regreso'] if vuelos['costo_regreso'] else 'N/A'}")
            costo_regreso_label.setObjectName("label_costo_regreso")
            costo_regreso_label.setStyleSheet("color: #FF5722;")
            costo_regreso_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            costo_regreso_label.setWordWrap(True)
            regreso_layout.addWidget(costo_regreso_label)

            vuelos_content_layout.addLayout(regreso_layout)

            vuelos_layout.addLayout(vuelos_content_layout)
            layout.addLayout(vuelos_layout)

        # Quinto cuadro: Detalles de alojamiento
        if alojamiento:
            alojamiento_layout = QVBoxLayout()

            alojamiento_label = QLabel("Alojamiento")
            alojamiento_label.setObjectName("label_alojamiento_title")
            alojamiento_label.setStyleSheet("color: #9C27B0;")
            alojamiento_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            alojamiento_label.setWordWrap(True)
            alojamiento_layout.addWidget(alojamiento_label)

            alojamiento_content_layout = QHBoxLayout()

            inicio_layout = QVBoxLayout()
            inicio_label = QLabel("Inicio")
            inicio_label.setObjectName("label_inicio_title")
            inicio_label.setStyleSheet("color: #9C27B0;")
            inicio_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            inicio_label.setWordWrap(True)
            inicio_layout.addWidget(inicio_label)

            fecha_inicio_label = QLabel(f"Fecha: {alojamiento['fecha_inicio']}")
            fecha_inicio_label.setObjectName("label_fecha_inicio_alojamiento")
            fecha_inicio_label.setStyleSheet("color: #9C27B0;")
            fecha_inicio_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            fecha_inicio_label.setWordWrap(True)
            inicio_layout.addWidget(fecha_inicio_label)

            hora_inicio_label = QLabel(f"Hora: {alojamiento['hora_inicio']} {alojamiento['ampm_inicio']}")
            hora_inicio_label.setObjectName("label_hora_inicio_alojamiento")
            hora_inicio_label.setStyleSheet("color: #9C27B0;")
            hora_inicio_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            hora_inicio_label.setWordWrap(True)
            inicio_layout.addWidget(hora_inicio_label)

            alojamiento_content_layout.addLayout(inicio_layout)

            fin_layout = QVBoxLayout()
            fin_label = QLabel("Fin")
            fin_label.setObjectName("label_fin_title")
            fin_label.setStyleSheet("color: #9C27B0;")
            fin_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            fin_label.setWordWrap(True)
            fin_layout.addWidget(fin_label)

            fecha_fin_label = QLabel(f"Fecha: {alojamiento['fecha_fin']}")
            fecha_fin_label.setObjectName("label_fecha_fin_alojamiento")
            fecha_fin_label.setStyleSheet("color: #9C27B0;")
            fecha_fin_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            fecha_fin_label.setWordWrap(True)
            fin_layout.addWidget(fecha_fin_label)

            hora_fin_label = QLabel(f"Hora: {alojamiento['hora_fin']} {alojamiento['ampm_fin']}")
            hora_fin_label.setObjectName("label_hora_fin_alojamiento")
            hora_fin_label.setStyleSheet("color: #9C27B0;")
            hora_fin_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            hora_fin_label.setWordWrap(True)
            fin_layout.addWidget(hora_fin_label)

            alojamiento_content_layout.addLayout(fin_layout)

            alojamiento_layout.addLayout(alojamiento_content_layout)

            costo_alojamiento_label = QLabel(f"Costo: ${alojamiento['costo'] if alojamiento['costo'] else 0}")
            costo_alojamiento_label.setObjectName("label_costo_alojamiento")
            costo_alojamiento_label.setStyleSheet("color: #9C27B0;")
            costo_alojamiento_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            costo_alojamiento_label.setWordWrap(True)
            alojamiento_layout.addWidget(costo_alojamiento_label)

            info_adicional_label = QLabel(f"Información adicional: {alojamiento['info_adicional'] if alojamiento['info_adicional'] else 'N/A'}")
            info_adicional_label.setObjectName("label_info_adicional_alojamiento")
            info_adicional_label.setStyleSheet("color: #9C27B0;")
            info_adicional_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            info_adicional_label.setWordWrap(True)
            alojamiento_layout.addWidget(info_adicional_label)

            layout.addLayout(alojamiento_layout)




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
        self.cargar_viajes_iniciales()
        self.listar_viajes()
        

        #Botones de la pagina nuevo viaje
        self.checkbox_vuelos_nuevo_viaje.stateChanged.connect(self.activar_regreso_ida_avion)
        self.checkbox_alojaimento_nuevo_viaje.stateChanged.connect(self.activar_alojamiento)
        self.save_new_travel_button.clicked.connect(self.evaluar_viaje)
        self.eliminar_viajeguardado_button.clicked.connect(self.eliminar_viaje_guardado)
        self.boton_familia_nuevo_viaje.clicked.connect(self.activar_line_edit_familia)
        self.boton_solo_nuevo_viaje.clicked.connect(self.activar_line_edit_familia)
        self.boton_pareja_nuevo_viaje.clicked.connect(self.activar_line_edit_familia)

    
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

        lista_fechas_inicio = fecha_inicio.split("-")
        lista_fechas_fin = fecha_fin.split("-")

        if len(lista_fechas_inicio) != 3 or not lista_fechas_inicio[0].isdigit() or not lista_fechas_inicio[1].isalnum() or not lista_fechas_inicio[2].isdigit():
            self.mostrar_warning("El formato de la fecha de inicio no es válido")
            return

        if len(lista_fechas_fin) != 3 or not lista_fechas_fin[0].isdigit() or not lista_fechas_fin[1].isalnum() or not lista_fechas_fin[2].isdigit():
            self.mostrar_warning("El formato de la fecha de fin no es válido")
            return

        indicador_de_mes_inicio = None
        indicador_de_mes_fin = None

        for i, mes in self.meses.items():
            if lista_fechas_inicio[1].capitalize() == mes:
                indicador_de_mes_inicio = i
            if lista_fechas_fin[1].capitalize() == mes:
                indicador_de_mes_fin = i

        if not indicador_de_mes_inicio:
            self.mostrar_warning("El mes de inicio es incorrecto, escriba el mes correctamente")
            return

        if not indicador_de_mes_fin:
            self.mostrar_warning("El mes de fin es incorrecto, escriba el mes correctamente")
            return

        dia_inicio_viaje, mes_inicio_viaje, año_inicio_viaje = int(lista_fechas_inicio[0]), indicador_de_mes_inicio, int(lista_fechas_inicio[2])
        dia_fin_viaje, mes_fin_viaje, año_fin_viaje = int(lista_fechas_fin[0]), indicador_de_mes_fin, int(lista_fechas_fin[2])

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
            "alojamiento": alojamiento
        }

        self.listar_viajes()
        self.mytravels_small_button1.click()


        self.mostrar_exito("El viaje se ha agregado correctamente")


    def listar_viajes(self):
        if self.viajes_usuario:
            viajes_ordenados = sorted(self.viajes_usuario.items(), key=lambda x: x[0], reverse=True)
            self.list_widget_viajes_guardados.clear()
            for i, viaje in viajes_ordenados:
                indice = i
                texto_titulo = viaje["titulo"]
                texto_destino = viaje["destino"]
                lista_fechas_inicio = viaje["fecha_inicio"]
                lista_fechas_fin = viaje["fecha_fin"]
                presupuesto = viaje["presupuesto"]
                personas_de_viaje = viaje["personas"]
                vuelos = viaje.get("vuelos", {})
                alojamiento = viaje.get("alojamiento", {})

                travel_widget = TravelWidget(indice, texto_titulo, texto_destino, lista_fechas_inicio, lista_fechas_fin, presupuesto, personas_de_viaje, vuelos, alojamiento)
                item = QListWidgetItem(self.list_widget_viajes_guardados)
                item.setSizeHint(travel_widget.sizeHint())
                self.list_widget_viajes_guardados.addItem(item)
                self.list_widget_viajes_guardados.setItemWidget(item, travel_widget)
            self.list_widget_viajes_guardados.scrollToTop()
        

    def cargar_viajes_iniciales(self):
        self.viajes_usuario = {
            0: {
                "titulo": "Viaje a Paris",
                "destino": "Paris, Francia",
                "fecha_inicio": ["01", "Ene", 2024],
                "fecha_fin": ["10", "Ene", 2024],
                "presupuesto": 1500,
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
                    "fecha_inicio": "01-Ene-2024",
                    "hora_inicio": "12:00",
                    "ampm_inicio": "PM",
                    "fecha_fin": "10-Ene-2024",
                    "hora_fin": "10:00",
                    "ampm_fin": "AM",
                    "costo": 500,
                    "info_adicional": "Hotel de 4 estrellas"
                }
            },
            1: {
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
                    "fecha_inicio": "15-Feb-2024",
                    "hora_inicio": "02:00",
                    "ampm_inicio": "PM",
                    "fecha_fin": "25-Feb-2024",
                    "hora_fin": "10:00",
                    "ampm_fin": "AM",
                    "costo": 1000,
                    "info_adicional": "Airbnb en el centro de la ciudad"
                }
            }
        }
        self.indice_viajes_guardados = max(self.viajes_usuario.keys())



    def validar_fecha_hora(self, fecha, hora, ampm, tipo):
        # Validar formato de fecha
        try:
            datetime.datetime.strptime(fecha, '%d-%m-%Y')
        except ValueError:
            self.mostrar_warning(f"El formato de la fecha de {tipo} no es válido. Use DD-MM-YYYY")
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


    def comparar_fechas(self, dia_inicio, mes_inicio, año_inicio, dia_fin, mes_fin, año_fin):
        fecha_inicio = datetime.date(año_inicio, mes_inicio, dia_inicio)
        fecha_fin = datetime.date(año_fin, mes_fin, dia_fin)
        return fecha_fin >= fecha_inicio

    def comparar_fechas_vuelo(self, fecha_ida, fecha_regreso):
        fecha_ida_dt = datetime.datetime.strptime(fecha_ida, '%d-%m-%Y')
        fecha_regreso_dt = datetime.datetime.strptime(fecha_regreso, '%d-%m-%Y')
        return fecha_regreso_dt >= fecha_ida_dt


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
    window = MainApp()
    window.show()
    sys.exit(app.exec())

