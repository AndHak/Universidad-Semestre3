from PySide6.QtCore import *
from PySide6.QtWidgets import *

from Estilos13 import *

class GameWindow(QMainWindow):

    def setup_ui(self):
        self.resize(QSize(600, 600))

        self.frame_titulo = QFrame()
        self.frame_buttons = QFrame()

        self.root_layout = QVBoxLayout()
        self.root_layout.addWidget(self.frame_titulo, 30)
        self.root_layout.addWidget(self.frame_buttons, 70)

        self.widget = QWidget()
        self.widget.setLayout(self.root_layout)
 
        self.setCentralWidget(self.widget)

        self.setStyleSheet(estilos_juego)



import sys

app = QApplication(sys.argv)

menu = GameWindow()
menu.setup_ui()
menu.show()

sys.exit(app.exec())