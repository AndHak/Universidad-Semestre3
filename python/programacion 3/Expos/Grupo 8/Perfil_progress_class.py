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


    def __init__(self):
        super().__init__()

        self.setWindowTitle("Completar perfil")

        icon_image = r"direccion del png"
        self.icon_window = QPixmap(icon_image)
        self.setWindowIcon(QIcon(self.icon_window))



        ##########DE USO RAPIDO###########
        ###################################
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
        ##########DE USO RAPIDO###########
        ###################################



 
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
        #Se debe agregar a este layout
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

        #AQui va el line edit del nombre y debe estar validado

        #Aqui va el label que muestra la informacion del progreso

        #Aqui se debe poner la barra de progreso

        #Agregar todo lo anterior al layout foto



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

    #Esto es para cargar la imagen
    def abrir_explorador_archivos(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            nueva_foto = QPixmap(file_name).scaled(QSize(200, 200), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.poner_foto_circulo(self.foto_usuario, nueva_foto)
            if not self.foto_cargada:
                self.foto_cargada = True

    def restaurar_foto_por_defecto(self):
        if self.foto_cargada:
            self.poner_foto_circulo(self.foto_usuario, self.foto_por_defecto)
            self.foto_cargada = False



    ###########Aqui van los otros line edit###############3
    def desarrollo_frame_info(self):
        #se deben agregar a este layout 
        self.layout_info = QVBoxLayout()
        self.layout_info.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.layout_info.setSpacing(20)
        self.layout_info.addStretch(20)

        # Agregar número de teléfono
        #El telefono tiene que estar validado 


        # Agregar QComboBox para las nacionalidades
        #Agregue 3 nacionalidades


        # Agregar radio buttons para el sexo
        #Hombre, Mujer y no especificar


        # Agregar checkboxes para los hobbies
        #Agregue al menos 5 hobbies

        #Agregar todo lo anterior al layout info


        self.frame_info.setLayout(self.layout_info)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
