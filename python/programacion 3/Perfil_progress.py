from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os

class Main(QMainWindow):
    basedir = os.path.dirname(__file__)
    pasos_completos = 0
    pasos_totales = 6
    foto_cargada = False
    nombre_completo = False
    telefono_completo = False
    nacionalidad_completa = False
    sexo_completo = False
    intereses_completos = False

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Completar perfil")

        icon_image = r"direccion del png"
        self.icon_window = QPixmap(icon_image)
        self.setWindowIcon(QIcon(self.icon_window))

        ##########DE USO RAPIDO###########
        self.icon_edit = QIcon(os.path.join(self.basedir, "img/edit.png"))
        self.icon_ok = QIcon(os.path.join(self.basedir, "img/ok.png"))
        self.estilo_line_edit = """border: none; background-color: transparent; border-bottom: 2px solid gray; height: 30px; width: 200px; font-size: 13px;"""
        self.estilo_line_edit_no_valido = """border: none; background-color: transparent; border-bottom: 2px solid red; height: 30px; width: 200px; font-size: 13px;"""
        self.estilo_barra_progreso = """
            QProgressBar {
                border: none;
                border-radius: 5px;
                background-color: #E0E0E0;
                height: 8px;
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 5px;
            }
            """



 
        self.root_layout = QHBoxLayout()

        self.frame_foto = QFrame()
        self.frame_info = QFrame()
        
        self.root_layout.addWidget(self.frame_foto, 1)
        self.root_layout.addWidget(self.frame_info, 99)

        self.desarrollo_frame_foto()
        self.desarrollo_frame_info()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget) 

    def desarrollo_frame_foto(self):
        self.layout_foto = QVBoxLayout()
        self.layout_foto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_foto.setSpacing(20)

        # Foto por defecto
        self.foto_por_defecto = QPixmap(os.path.join(self.basedir, "img/sinfoto.png")).scaled(QSize(200, 200), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        self.foto_usuario = QLabel()
        self.foto_usuario.setFixedSize(QSize(200, 200))
        self.poner_foto_circulo(self.foto_usuario, self.foto_por_defecto)

        self.eliminar_foto = QPushButton()
        self.eliminar_foto.setFixedSize(QSize(40, 40))
        self.eliminar_foto.setIconSize(QSize(40, 40))
        self.eliminar_foto.setStyleSheet("border: none;")
        self.eliminar_foto.setCursor(Qt.PointingHandCursor)
        self.eliminar_foto.setIcon(QIcon(os.path.join(self.basedir, "img/cerrar.png")))
        self.eliminar_foto.clicked.connect(self.restaurar_foto_por_defecto)

        self.agregar_foto = QPushButton()
        self.agregar_foto.setFixedSize(QSize(50, 50))
        self.agregar_foto.setIconSize(QSize(50, 50))
        self.agregar_foto.setStyleSheet("border: none;")
        self.agregar_foto.setCursor(Qt.PointingHandCursor)
        self.agregar_foto.setIcon(QIcon(os.path.join(self.basedir, "img/plus.png")))
        self.agregar_foto.clicked.connect(self.abrir_explorador_archivos)

        self.container_widget = QWidget()
        self.container_widget.setFixedSize(QSize(200, 200))
        self.container_layout = QGridLayout(self.container_widget)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)

        self.container_layout.addWidget(self.foto_usuario, 0, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.container_layout.addWidget(self.eliminar_foto, 0, 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.container_layout.addWidget(self.agregar_foto, 0, 0, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        self.layout_foto.addWidget(self.container_widget)

        self.name_line_edit = QLineEdit()
        self.name_line_edit.setPlaceholderText("Nombre/Apellido")
        self.name_line_edit.setStyleSheet(self.estilo_line_edit)
        self.name_line_edit.setReadOnly(True)
        self.name_line_edit.setMaxLength(30)
        self.name_button_edit = QPushButton()
        self.name_button_edit.setIcon(self.icon_edit)
        self.name_button_edit.clicked.connect(self.validar_nombre)

        self.form_name = QHBoxLayout()
        self.form_name.addWidget(self.name_line_edit)
        self.form_name.addWidget(self.name_button_edit)
        self.layout_foto.addLayout(self.form_name)

        self.pasos_por_completar = QLabel(f"Completa tu perfil     {self.pasos_completos}/{self.pasos_totales}")
        self.layout_foto.addWidget(self.pasos_por_completar)

        self.bar_progress_pasos = QProgressBar()
        self.bar_progress_pasos.setStyleSheet(self.estilo_barra_progreso)
        self.layout_foto.addWidget(self.bar_progress_pasos)


        self.frame_foto.setLayout(self.layout_foto)

    def poner_foto_circulo(self, label, pixmap):
        size = label.size()
        circulo_pixmap = QPixmap(size)
        circulo_pixmap.fill(Qt.transparent)

        painter = QPainter(circulo_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, size.width(), size.height())
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, size.width(), size.height(), pixmap)
        painter.end()

        label.setPixmap(circulo_pixmap)

    def validar_nombre(self):
        if self.name_line_edit.isReadOnly():
            self.name_line_edit.setReadOnly(False)
            self.name_line_edit.setStyleSheet(self.estilo_line_edit)
            self.name_button_edit.setIcon(self.icon_ok)
        else:
            name_text = self.name_line_edit.text().strip()
            if name_text == "":
                self.name_line_edit.clear()
                self.name_line_edit.setPlaceholderText("Nombre/Apellido")
            if not name_text:
                if not self.nombre_completo:
                    self.name_line_edit.setReadOnly(True)
                    self.name_line_edit.setStyleSheet(self.estilo_line_edit)
                    self.name_button_edit.setIcon(self.icon_edit)
                    return
                if self.nombre_completo:
                    self.pasos_completos -= 1
                    self.nombre_completo = False
                    self.name_line_edit.setStyleSheet(self.estilo_line_edit)
                    self.name_line_edit.setReadOnly(True)
                    self.name_button_edit.setIcon(self.icon_edit)
                    self.actualizar_progreso()
                    return

            if name_text and not any(i.isdigit() for i in name_text):
                nombres = name_text.split()
                if len(nombres) <= 2:
                    name_text = ' '.join(nombres).title()
                    self.name_line_edit.setText(name_text)
                    self.name_line_edit.setStyleSheet(self.estilo_line_edit)
                    if not self.nombre_completo:
                        self.pasos_completos += 1
                        self.nombre_completo = True
                    self.name_line_edit.setReadOnly(True)
                    self.name_button_edit.setIcon(self.icon_edit)
                    self.actualizar_progreso()
                else:
                    self.name_line_edit.setStyleSheet(self.estilo_line_edit_no_valido)
                    if self.nombre_completo:
                        self.pasos_completos -= 1
                        self.nombre_completo = False
                        self.actualizar_progreso()
            else:
                self.name_line_edit.setStyleSheet(self.estilo_line_edit_no_valido)
                if self.nombre_completo:
                    self.pasos_completos -= 1
                    self.nombre_completo = False
                    self.actualizar_progreso()

            if not name_text and self.nombre_completo:
                self.pasos_completos -= 1
                self.nombre_completo = False
                self.name_line_edit.setStyleSheet(self.estilo_line_edit)
                self.name_line_edit.setReadOnly(True)
                self.name_button_edit.setIcon(self.icon_edit)
                self.actualizar_progreso()

    def abrir_explorador_archivos(self):
        #abrir explorador de archivos
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            #Si hay imagen la carga
            nueva_foto = QPixmap(file_name).scaled(QSize(200, 200), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.poner_foto_circulo(self.foto_usuario, nueva_foto)
            if not self.foto_cargada:
                self.pasos_completos += 1
                self.foto_cargada = True
                self.actualizar_progreso()

    def restaurar_foto_por_defecto(self):
        if self.foto_cargada:
            self.poner_foto_circulo(self.foto_usuario, self.foto_por_defecto)
            self.pasos_completos -= 1
            self.foto_cargada = False
            self.actualizar_progreso()

    def actualizar_progreso(self):
        self.bar_progress_pasos.setMaximum(self.pasos_totales)
        self.bar_progress_pasos.setValue(self.pasos_completos)

        todos_qlineedit_en_solo_lectura = all(i.isReadOnly for i in self.findChildren(QLineEdit))

        if self.pasos_totales == self.pasos_completos and todos_qlineedit_en_solo_lectura:
            self.pasos_por_completar.setText("Perfil completo")
        else:
            self.pasos_por_completar.setText(f"Completa tu perfil:     {self.pasos_completos}/{self.pasos_totales}")


    ###########Aqui van los otros line edit###############3
    def desarrollo_frame_info(self):
        self.layout_info = QVBoxLayout()
        self.layout_info.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.layout_info.setSpacing(20)
        self.layout_info.addStretch(20)

        # Agregar número de teléfono
        self.telefono_line_edit = QLineEdit()
        self.telefono_line_edit.setPlaceholderText("Número de teléfono")
        self.telefono_line_edit.setStyleSheet(self.estilo_line_edit)
        self.telefono_line_edit.setReadOnly(True)
        self.telefono_line_edit.setMaxLength(10)
        self.telefono_button_edit = QPushButton()
        self.telefono_button_edit.setIcon(self.icon_edit)
        self.telefono_button_edit.clicked.connect(self.validar_telefono)

        form_telefono = QHBoxLayout()
        form_telefono.addWidget(self.telefono_line_edit)
        form_telefono.addWidget(self.telefono_button_edit)
        self.layout_info.addLayout(form_telefono)

        # Agregar QComboBox para las nacionalidades
        self.nacionalidad_layout = QVBoxLayout() 
        self.nacionalidad_layout.setSpacing(10)
        self.nacionalidad_label = QLabel("Seleccionar nacionalidad")
        self.combo_nacionalidad = QComboBox()
        nacionalidades = ["No especificar", "Colombia", "México", "Ecuador"]
        self.combo_nacionalidad.addItems(nacionalidades)
        self.combo_nacionalidad.currentIndexChanged.connect(self.validar_nacionalidad)

        self.nacionalidad_layout.addWidget(self.nacionalidad_label)
        self.nacionalidad_layout.addWidget(self.combo_nacionalidad)
        self.layout_info.addLayout(self.nacionalidad_layout)

        # Agregar radio buttons para el sexo
        self.sexo_group = QGroupBox("Sexo")
        self.sexo_layout = QVBoxLayout()
        self.sexo_button_group = QButtonGroup()
        self.sexo_hombre = QRadioButton("Hombre")
        self.sexo_mujer = QRadioButton("Mujer")
        self.sexo_no_especificar = QRadioButton("No especificar")
        self.sexo_no_especificar.setChecked(True)
        self.sexo_button_group.addButton(self.sexo_hombre)
        self.sexo_button_group.addButton(self.sexo_mujer)
        self.sexo_button_group.addButton(self.sexo_no_especificar)
        self.sexo_button_group.buttonClicked.connect(self.validar_sexo)
        self.sexo_layout.addWidget(self.sexo_hombre)
        self.sexo_layout.addWidget(self.sexo_mujer)
        self.sexo_layout.addWidget(self.sexo_no_especificar)
        self.sexo_group.setLayout(self.sexo_layout)
        self.layout_info.addWidget(self.sexo_group)

        # Agregar checkboxes para los hobbies
        self.hobbies_group = QGroupBox("Intereses")
        self.hobbies_layout = QVBoxLayout()
        self.intereses = ["Gym", "Cine", "Fiesta", "Viajes", "Musica"]
        self.intereses_checkboxes = []
        for interes in self.intereses:
            checkbox = QCheckBox(interes)
            checkbox.stateChanged.connect(self.validar_intereses)
            self.intereses_checkboxes.append(checkbox)
            self.hobbies_layout.addWidget(checkbox)
        self.hobbies_group.setLayout(self.hobbies_layout)
        self.layout_info.addWidget(self.hobbies_group)

        self.frame_info.setLayout(self.layout_info)

    def validar_telefono(self):
        if self.telefono_line_edit.isReadOnly():
            self.telefono_line_edit.setReadOnly(False)
            self.telefono_line_edit.setStyleSheet(self.estilo_line_edit)
            self.telefono_button_edit.setIcon(self.icon_ok)
        else:
            telefono_text = self.telefono_line_edit.text().strip()
            if telefono_text == "":
                self.telefono_line_edit.clear()
                self.telefono_line_edit.setPlaceholderText("Número de teléfono")
            if not telefono_text:
                if not self.telefono_completo:
                    self.telefono_line_edit.setReadOnly(True)
                    self.telefono_line_edit.setStyleSheet(self.estilo_line_edit)
                    self.telefono_button_edit.setIcon(self.icon_edit)
                    return
                if self.telefono_completo:
                    self.pasos_completos -= 1
                    self.telefono_completo = False
                    self.telefono_line_edit.setStyleSheet(self.estilo_line_edit)
                    self.telefono_line_edit.setReadOnly(True)
                    self.telefono_button_edit.setIcon(self.icon_edit)
                    self.actualizar_progreso()
                    return

            if telefono_text.isdigit() and len(telefono_text) == 10:
                self.telefono_line_edit.setStyleSheet(self.estilo_line_edit)
                if not self.telefono_completo:
                    self.pasos_completos += 1
                    self.telefono_completo = True
                self.telefono_line_edit.setReadOnly(True)
                self.telefono_button_edit.setIcon(self.icon_edit)
                self.actualizar_progreso()
            else:
                self.telefono_line_edit.setStyleSheet(self.estilo_line_edit_no_valido)
                if self.telefono_completo:
                    self.pasos_completos -= 1
                    self.telefono_completo = False
                    self.actualizar_progreso()


    def validar_nacionalidad(self, index):
        if index == 0: 
            if self.nacionalidad_completa:
                self.pasos_completos -= 1
                self.nacionalidad_completa = False
                self.actualizar_progreso()
        else:
            if not self.nacionalidad_completa:
                self.pasos_completos += 1
                self.nacionalidad_completa = True
                self.actualizar_progreso()

    def validar_sexo(self, button):
        if button == self.sexo_no_especificar:
            if self.sexo_completo:
                self.pasos_completos -= 1
                self.sexo_completo = False
                self.actualizar_progreso()
        else:
            if not self.sexo_completo:
                self.pasos_completos += 1
                self.sexo_completo = True
                self.actualizar_progreso()

    def validar_intereses(self):
        intereses_seleccionados = sum(checkbox.isChecked() for checkbox in self.intereses_checkboxes)
        if intereses_seleccionados >= 2:
            if not self.intereses_completos:
                self.pasos_completos += 1
                self.intereses_completos = True
                self.actualizar_progreso()
        else:
            if self.intereses_completos:
                self.pasos_completos -= 1
                self.intereses_completos = False
                self.actualizar_progreso()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
