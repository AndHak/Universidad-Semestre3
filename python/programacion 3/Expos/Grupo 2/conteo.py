import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os

class EditorDeTexto(QWidget):
    basedir = os.path.dirname(__file__)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Editor de Texto')
        layout = QVBoxLayout()

        barra_herramientas = QToolBar()

        self.boton_negrita = QPushButton('N')
        self.boton_negrita.setStyleSheet("font-weight: bold;")
        self.boton_mayusculas = QPushButton()
        self.boton_mayusculas.setIcon(QIcon(os.path.join(self.basedir, "img/boton-de-interfaz-en-mayusculas.png")))
        self.boton_minusculas = QPushButton()
        self.boton_minusculas.setIcon(QIcon(os.path.join(self.basedir, "img/simbolo-de-interfaz-en-minusculas.png")))
        self.boton_alinear_izquierda = QPushButton()
        self.boton_alinear_izquierda.setIcon(QIcon(os.path.join(self.basedir, "img/alinear-a-la-izquierda.png")))
        self.boton_alinear_centro = QPushButton()
        self.boton_alinear_centro.setIcon(QIcon(os.path.join(self.basedir, "img/alinear.png")))
        self.boton_alinear_derecha = QPushButton()
        self.boton_alinear_derecha.setIcon(QIcon(os.path.join(self.basedir, "img/alinear-a-la-derecha.png")))
        self.boton_modo_edicion = QPushButton('Modo Lectura')

        self.boton_negrita.clicked.connect(self.aplicar_negrita)
        self.boton_mayusculas.clicked.connect(self.convertir_mayusculas)
        self.boton_minusculas.clicked.connect(self.convertir_minusculas)
        self.boton_alinear_izquierda.clicked.connect(lambda: self.area_texto.setAlignment(Qt.AlignLeft))
        self.boton_alinear_centro.clicked.connect(lambda: self.area_texto.setAlignment(Qt.AlignCenter))
        self.boton_alinear_derecha.clicked.connect(lambda: self.area_texto.setAlignment(Qt.AlignRight))
        self.boton_modo_edicion.clicked.connect(self.cambiar_modo_edicion)

        barra_herramientas.addWidget(self.boton_negrita)
        barra_herramientas.addWidget(self.boton_mayusculas)
        barra_herramientas.addWidget(self.boton_minusculas)
        barra_herramientas.addWidget(self.boton_alinear_izquierda)
        barra_herramientas.addWidget(self.boton_alinear_centro)
        barra_herramientas.addWidget(self.boton_alinear_derecha)
        barra_herramientas.addWidget(self.boton_modo_edicion)

        self.area_texto = QTextEdit()
        self.area_texto.setPlaceholderText("Escribe aquí...")

        self.contador_palabras = QLabel('Palabras: 0')

        layout.addWidget(barra_herramientas)
        layout.addWidget(self.area_texto)
        layout.addWidget(self.contador_palabras)
        self.setLayout(layout)

        self.area_texto.textChanged.connect(self.actualizar_contador_palabras)

    def aplicar_negrita(self):
        if self.area_texto.textCursor().hasSelection():
            fuente = self.area_texto.currentFont()
            fuente.setBold(not fuente.bold())
            self.area_texto.setCurrentFont(fuente)

    def convertir_mayusculas(self):
        self.area_texto.insertPlainText(self.area_texto.textCursor().selectedText().upper())

    def convertir_minusculas(self):
        self.area_texto.insertPlainText(self.area_texto.textCursor().selectedText().lower())

    def actualizar_contador_palabras(self):
        palabras = self.area_texto.toPlainText().split()
        self.contador_palabras.setText(f'Palabras: {len(palabras)}')

    def cambiar_modo_edicion(self):
        if self.area_texto.isReadOnly():
            self.area_texto.setReadOnly(False)
            self.sender().setText('Modo Lectura')
            self.boton_negrita.setEnabled(True)
            self.boton_mayusculas.setEnabled(True)
            self.boton_minusculas.setEnabled(True)
            self.boton_alinear_izquierda.setEnabled(True)
            self.boton_alinear_centro.setEnabled(True)
            self.boton_alinear_derecha.setEnabled(True)
        else:
            self.area_texto.setReadOnly(True)
            self.sender().setText('Modo Edición')
            self.boton_negrita.setEnabled(False)
            self.boton_mayusculas.setEnabled(False)
            self.boton_minusculas.setEnabled(False)
            self.boton_alinear_izquierda.setEnabled(False)
            self.boton_alinear_centro.setEnabled(False)
            self.boton_alinear_derecha.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    editor = EditorDeTexto()
    editor.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()