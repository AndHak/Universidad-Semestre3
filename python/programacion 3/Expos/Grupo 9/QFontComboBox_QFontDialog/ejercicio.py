from PySide6.QtWidgets import QApplication, QFontComboBox, QFontDialog, QFrame, QHBoxLayout, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QFont, QIcon, QTextCharFormat
import sys
import os


class Main(QMainWindow):
    basedir = os.path.dirname(__file__)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nombre app")
        icon_image = r"direccion del png"
        self.setWindowIcon(QIcon(icon_image))
        self.root_layout = QHBoxLayout()
        self.frame_izquierdo = QFrame()
        self.frame_derecho = QFrame()
        self.root_layout.addWidget(self.frame_izquierdo, 100)
        self.root_layout.addWidget(self.frame_derecho, 100)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)
        self.desarrollo_pagina_1()
        self.desarrollo_pagina_2()

    def desarrollo_pagina_1(self):
        self.root_pagina_layout = QVBoxLayout()
        self.line_edit = QFontComboBox()
        self.root_pagina_layout.addWidget(self.line_edit)
        self.cambiar_fuente = QPushButton("Cambiar fuente")
        self.cambiar_fuente.clicked.connect(self.cambiar_fuente_texto)
        self.root_pagina_layout.addWidget(self.cambiar_fuente)

        # Agregar botones de 3 fuentes
        font_names = ["Soccer League College", "Bodoni", "Rockwell"]
        for font_name in font_names:
            font_button = QPushButton(font_name)
            font_button.clicked.connect(lambda checked=False, name=font_name: self.cambiar_fuente_texto(name))
            self.root_pagina_layout.addWidget(font_button)

        self.seleccion_fuente = QPushButton("Seleccionar fuente")
        self.seleccion_fuente.clicked.connect(self.abrir_qfont_dialog)
        self.root_pagina_layout.addWidget(self.seleccion_fuente)
        self.frame_izquierdo.setLayout(self.root_pagina_layout)

    def desarrollo_pagina_2(self):
        self.root_pagina2_layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.root_pagina2_layout.addWidget(self.text_edit)
        self.boton_borrar = QPushButton()
        self.boton_borrar.setIcon(QIcon(os.path.join(self.basedir, "limpio.png")))
        self.boton_borrar.clicked.connect(self.borrar)
        self.root_pagina2_layout.addWidget(self.boton_borrar)
        self.frame_derecho.setLayout(self.root_pagina2_layout)

    def abrir_qfont_dialog(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.aplicar_fuente_a_texto(font)

    def borrar(self):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            cursor.removeSelectedText()
        else:
            self.text_edit.selectAll()
            cursor.removeSelectedText()


    def cambiar_fuente_texto(self, font_name=None):
        font = QFont(font_name or self.line_edit.currentFont().family())
        self.aplicar_fuente_a_texto(font)

    def aplicar_fuente_a_texto(self, font):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            texto = QTextCharFormat()
            texto.setFont(font)
            cursor.setCharFormat(texto)
        else:
            self.text_edit.selectAll()
            texto = QTextCharFormat()
            texto.setFont(font)
            cursor.setCharFormat(texto)
            cursor.clearSelection()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())

