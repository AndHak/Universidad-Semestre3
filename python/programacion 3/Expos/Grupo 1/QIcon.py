from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys, os

basedir = os.path.dirname(__file__)

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.icon_setup()
        
    def icon_setup(self):
        self.setWindowTitle("Ejemplo QIcon")
        
        main_layout = QHBoxLayout()
        # ------------------------------------------------------------------------
        v_layout = QVBoxLayout()
        g_box = QGroupBox('Creación de Iconos')
        g_box.setLayout(v_layout)
        
        # Icono a partir de una imagen -------------------------------------------
        icono = QIcon(os.path.join(basedir, 'Iconos',"ico_ima.png"))
        btn_icon = QPushButton(icono, 'Icono normal')
        # btn_icon = QPushButton(' Icono normal ')
        # btn_icon.setIcon(icono)
        # # btn_icon.setIcon(QIcon(os.path.join(basedir, 'Iconos',"ico_ima.png")))
        v_layout.addWidget(btn_icon)
        
        # addFile ----------------------------------------------------------------
        
        icon_1 = QIcon()
        icon_1.addFile('iconos/ico_2.png')
        btn_icon_2 = QPushButton(' Icono con addFile ')
        btn_icon_2.setIcon(icon_1)
        v_layout.addWidget(btn_icon_2)
        size = btn_icon_2.sizeHint()
        print(size)
        g_box.setLayout(v_layout)
        
        # addPixmap --------------------------------------------------------------
        pixmap = QPixmap(os.path.join(basedir, 'iconos/ico_1.png'))
        icon = QIcon(pixmap)
        btn_icon_1 = QPushButton(' Icono con addPixmap ')
        btn_icon_1.setIcon(icon)
        btn_icon_1.setIconSize(QSize(40, 40))
        v_layout.addWidget(btn_icon_1)
        
        # ------------------------------------------------------------------------
        g_box1 = QGroupBox('Otros Metodos')
        v_layout1 = QVBoxLayout()
        g_box1.setLayout(v_layout1)
        
        # Swap - Cambiar icono ---------------------------------------------------
        pixmap = QPixmap(os.path.join(basedir, 'iconos/ico_1.png'))
        self.icon = QIcon(pixmap)
        self.btn_iconos = QPushButton(icon=self.icon)
        self.btn_iconos.setIconSize(QSize(20, 20))
        self.btn_iconos.clicked.connect(self.cambiarIcono)
        v_layout1.addWidget(self.btn_iconos)
        
        # availableSizes ---------------------------------------------------------
        icon_sizes = QIcon()
        # icon_sizes = QIcon(os.path.join(basedir, 'Iconos',"ico_ima.png"))
        # icon_sizes = self.style().standardIcon(QStyle.SP_DialogOpenButton)
        lbl_sizes = QLabel('Tamaños: ')
        v_layout1.addWidget(lbl_sizes)
        for tamano in icon_sizes.availableSizes():
            etiqueta = QLabel(f"{tamano.width()} x {tamano.height()}")
            v_layout1.addWidget(etiqueta)
        
        
        # isNull() ---------------------------------------------------------------
        # icon_null = QIcon()
        icon_null = QIcon(os.path.join(basedir, 'Iconos',"ico_ima.png"))
        lbl_null = QLabel(f'Es nulo: {icon_null.isNull()}')
        v_layout1.addWidget(lbl_null)
        
        #pixmap() ---------------------------------------------------------------
        lbl_pix = QLabel('Pixmap: ')
        v_layout1.addWidget(lbl_pix)
        pixmap = icon_null.pixmap(QSize(30, 30), QIcon.Mode.Normal, QIcon.State.Off)
        lbl_pixmap = QLabel()
        lbl_pixmap.setPixmap(pixmap)
        v_layout1.addWidget(lbl_pixmap)
        
        #-------------------------------------------------------------------------
        v_layout2 = QVBoxLayout()
        g_box2 = QGroupBox('Iconos estandar')
        g_box2.setLayout(v_layout2)
        
        # Iconos Estandar --------------------------------------------------------
        icono = self.style().standardIcon(QStyle.SP_ArrowBack)
        btn_desk = QPushButton(icono, "Flecha atras")
        v_layout2.addWidget(btn_desk)
        
        icono = self.style().standardIcon(QStyle.SP_FileIcon)
        btn_file = QPushButton(icono, "Archivo")
        v_layout2.addWidget(btn_file)
        
        icono = self.style().standardIcon(QStyle.SP_DialogOpenButton)
        btn_opne = QPushButton(icono, "Abrir")
        v_layout2.addWidget(btn_opne)
        
        
        main_layout.addWidget(g_box)
        main_layout.addWidget(g_box1)
        main_layout.addWidget(g_box2)
        
        self.setLayout(main_layout)
        
    def cambiarIcono(self):
        icon_2 = QIcon(QPixmap(os.path.join(basedir, 'iconos/ico_2.png')))
        self.icon.swap(icon_2)
        self.btn_iconos.setIcon(self.icon)
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    app.exec()