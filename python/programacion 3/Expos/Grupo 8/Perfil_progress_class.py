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

        #Foto por defecto
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
        self.agregar_foto.setFixedSize(QSize(40, 40))
        self.agregar_foto.setIconSize(QSize(40, 40))
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
        pass


    def abrir_explorador_archivos(self):
        # abrir explorador de archivos
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            # Si hay imagen la carga
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
        #Agregar a este layout los layouts o widgets
        #Este layour pertenece a el frame derecho donde ya esta el line edit del telefono
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


        # Agregar radio buttons para el sexo


        # Agregar checkboxes para los hobbies


        #Se establece el layout info en el frame info
        self.frame_info.setLayout(self.layout_info)

    def validar_telefono(self):
        pass

    def validar_nacionalidad(self, index):
        pass

    def validar_sexo(self, button):
        pass

    def validar_intereses(self):
        pass

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
