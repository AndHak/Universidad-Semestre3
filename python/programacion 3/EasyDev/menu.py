from PySide6.QtCore import *
from PySide6.QtWidgets import *

from python.PySide6.EasyDev.Estilos13 import *

class Menu(QMainWindow):
    def setup_ui(self):

        self.resize(QSize(600, 600))

        self.root_layout = QVBoxLayout()

        self.frame_titulo = QFrame()
        self.frame_inputs = QFrame()


        self.root_layout.addWidget(self.frame_titulo, 30)
        self.root_layout.addWidget(self.frame_inputs, 70)

        self.widget = QWidget()
        self.widget.setLayout(self.root_layout)

        self.setCentralWidget(self.widget)
        self.setStyleSheet(estilos_menu)
        self.setup_inputs_frame()
        self.setup_titulo_frame()


    def setup_inputs_frame(self):
        self.input_title = QLabel("Ingrese el nombre de los jugadores")
        self.input_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.player_1 = QLineEdit()
        self.player_1.setPlaceholderText("Jugador 1")
        self.player_2 = QLineEdit()
        self.player_2.setPlaceholderText("Jugador 2")

        self.inputs_layout = QVBoxLayout()

        widgets = [self.input_title, self.player_1, self.player_2]

        for w in widgets:
            self.inputs_layout.addWidget(w)
            self.inputs_layout.addSpacing(10)

        self.play_button = QPushButton("Jugar")
        self.inputs_layout.addWidget(self.play_button)

        self.inputs_layout.addStretch()

        self.frame_inputs.setLayout(self.inputs_layout)

    def setup_titulo_frame(self):
        self.titulo_principal = QLabel("TIC TAC TOE", objectName="titulo_principal")

        self.titulo_principal.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.titulo_principal_layout = QVBoxLayout()

        self.titulo_principal_layout.addWidget(self.titulo_principal)

        self.frame_titulo.setLayout(self.titulo_principal_layout)

    
import sys

app = QApplication(sys.argv)

menu = Menu()
menu.setup_ui()
menu.show()

sys.exit(app.exec())