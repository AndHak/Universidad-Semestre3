from PySide6.QtCore import *
from PySide6.QtWidgets import *

class Menu(QMainWindow):
    def setup_ui(self):

        self.resize(QSize(600, 600))

        self.root_layout = QVBoxLayout()

        self.frame_titulo = QFrame()
        self.frame_titulo.setStyleSheet("background: white")
        self.frame_inputs = QFrame()
        self.frame_inputs.setStyleSheet("background: white")

        self.root_layout.addWidget(self.frame_titulo, 30)
        self.root_layout.addWidget(self.frame_inputs, 70)

        self.widget = QWidget()
        self.widget.setLayout(self.root_layout)

        self.setCentralWidget(self.widget)
        self.setup_inputs_frame()

    def setup_inputs_frame(self):
        self.input_title = QLabel("Ingrese el nombre de los jugadores")
        self.player_1 = QLineEdit()
        self.player_2 = QLineEdit()
        self.boton_jugar = QPushButton()

        self.inputs_layout = QVBoxLayout()
        self.inputs_layout.addWidget(self.input_title)
        self.inputs_layout.addWidget(self.player_1)
        self.inputs_layout.addWidget(self.player_2)
        self.inputs_layout.addWidget(self.boton_jugar)
        self.inputs_layout.addStretch()

        self.frame_inputs.setLayout(self.inputs_layout)

import sys

app = QApplication(sys.argv)

menu = Menu()
menu.setup_ui()
menu.show()

sys.exit(app.exec())