from PySide6.QtWidgets import *

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy

class TravelWidget(QWidget):
    def __init__(self, indice, titulo, destino, datos_fecha_viaje_inicio, datos_fecha_viaje_fin, presupuesto=0.0, personas="1", vuelos=None, alojamiento=None, itinerario=None, gastos=None):
        super().__init__()
        self.indice = indice

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

        budget_label = QLabel(f"Presupuesto: ${float(presupuesto):.2f}")
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

            costo_ida_label = QLabel(f"Costo: ${float(vuelos['costo_ida']) if vuelos['costo_ida'] else 0.00:.2f}")
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

            costo_regreso_label = QLabel(f"Costo: ${float(vuelos['costo_regreso']) if vuelos['costo_regreso'] else 0.00:.2f}")
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

            alojamiento_label = QLabel(f"Alojamiento: {alojamiento['Tipo']}")
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

            costo_alojamiento_label = QLabel(f"Costo: ${float(alojamiento['costo']) if alojamiento['costo'] else 0.00:.2f}")
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




class GastoWidget(QWidget):
    def __init__(self, descripcion, gasto, fecha):
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

        # Primer cuadro: Descripción
        descripcion_layout = QVBoxLayout()

        descripcion_label = QLabel(f"Descripción: {descripcion}")
        descripcion_label.setObjectName("label_descripcion_title")
        descripcion_label.setStyleSheet("color: #2196F3;")
        descripcion_label.setWordWrap(True)
        descripcion_layout.addWidget(descripcion_label)

        layout.addLayout(descripcion_layout)

        # Segundo cuadro: Gasto
        gasto_layout = QVBoxLayout()

        gasto_label = QLabel(f"Valor: ${float(gasto):.2f}" if gasto else "Valor: N/A")
        gasto_label.setObjectName("label_gasto_title")
        gasto_label.setStyleSheet("color: #4CAF50;")
        gasto_label.setWordWrap(True)
        gasto_layout.addWidget(gasto_label)

        layout.addLayout(gasto_layout)

        # Tercer cuadro: Fecha
        fecha_layout = QVBoxLayout()

        fecha_label = QLabel(f"Fecha: {fecha}")
        fecha_label.setObjectName("label_fecha_title")
        fecha_label.setStyleSheet("color: #FF9800;")
        fecha_label.setWordWrap(True)
        fecha_layout.addWidget(fecha_label)

        layout.addLayout(fecha_layout)


class PlanWidget(QWidget):
    def __init__(self, plan, hora, am_pm, fecha):
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

        # Primer cuadro: Plan
        plan_layout = QVBoxLayout()

        plan_label = QLabel(f"Plan: {plan}")
        plan_label.setObjectName("label_plan_title")
        plan_label.setStyleSheet("color: #2196F3;")
        plan_label.setWordWrap(True)
        plan_layout.addWidget(plan_label)

        layout.addLayout(plan_layout)

        # Segundo cuadro: Hora
        hora_layout = QVBoxLayout()

        hora_label = QLabel(f"Hora: {hora} {am_pm}")
        hora_label.setObjectName("label_hora_title")
        hora_label.setStyleSheet("color: #4CAF50;")
        hora_label.setWordWrap(True)
        hora_layout.addWidget(hora_label)

        layout.addLayout(hora_layout)

        # Tercer cuadro: Fecha
        fecha_layout = QVBoxLayout()

        fecha_label = QLabel(f"Fecha: {fecha}")
        fecha_label.setObjectName("label_fecha_title")
        fecha_label.setStyleSheet("color: #FF9800;")
        fecha_label.setWordWrap(True)
        fecha_layout.addWidget(fecha_label)

        layout.addLayout(fecha_layout)


class RecordatorioWidget(QWidget):
    def __init__(self, asunto, fecha=None, hora=None, lugar=None):
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

        # Primer cuadro: Asunto
        asunto_layout = QVBoxLayout()

        asunto_label = QLabel("Asunto")
        asunto_label.setObjectName("label_asunto_title")
        asunto_label.setStyleSheet("color: #2196F3;")
        asunto_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        asunto_label.setWordWrap(True)
        asunto_layout.addWidget(asunto_label)

        asunto_value_label = QLabel(f"{asunto}")
        asunto_value_label.setObjectName("label_asunto_value")
        asunto_value_label.setStyleSheet("color: #2196F3;")
        asunto_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        asunto_value_label.setWordWrap(True)
        asunto_layout.addWidget(asunto_value_label)

        layout.addLayout(asunto_layout)

        # Segundo cuadro: Fecha
        if fecha:
            fecha_layout = QVBoxLayout()

            fecha_label = QLabel("Fecha")
            fecha_label.setObjectName("label_fecha_title")
            fecha_label.setStyleSheet("color: #FF9800;")
            fecha_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            fecha_label.setWordWrap(True)
            fecha_layout.addWidget(fecha_label)

            fecha_value_label = QLabel(f"{fecha}")
            fecha_value_label.setObjectName("label_fecha_value")
            fecha_value_label.setStyleSheet("color: #FF9800;")
            fecha_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            fecha_value_label.setWordWrap(True)
            fecha_layout.addWidget(fecha_value_label)

            layout.addLayout(fecha_layout)

        # Tercer cuadro: Hora
        if hora:
            hora_layout = QVBoxLayout()

            hora_label = QLabel("Hora")
            hora_label.setObjectName("label_hora_title")
            hora_label.setStyleSheet("color: #FF5722;")
            hora_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            hora_label.setWordWrap(True)
            hora_layout.addWidget(hora_label)

            hora_value_label = QLabel(f"{hora}")
            hora_value_label.setObjectName("label_hora_value")
            hora_value_label.setStyleSheet("color: #FF5722;")
            hora_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            hora_value_label.setWordWrap(True)
            hora_layout.addWidget(hora_value_label)

            layout.addLayout(hora_layout)

        # Cuarto cuadro: Lugar
        if lugar:
            lugar_layout = QVBoxLayout()

            lugar_label = QLabel("Lugar")
            lugar_label.setObjectName("label_lugar_title")
            lugar_label.setStyleSheet("color: #4CAF50;")
            lugar_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            lugar_label.setWordWrap(True)
            lugar_layout.addWidget(lugar_label)

            lugar_value_label = QLabel(f"{lugar}")
            lugar_value_label.setObjectName("label_lugar_value")
            lugar_value_label.setStyleSheet("color: #4CAF50;")
            lugar_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            lugar_value_label.setWordWrap(True)
            lugar_layout.addWidget(lugar_value_label)

            layout.addLayout(lugar_layout)
