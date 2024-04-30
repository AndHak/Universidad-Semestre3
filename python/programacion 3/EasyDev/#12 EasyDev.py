from PySide6.QtCore import *
from PySide6.QtWidgets import *

class Menu(QMainWindow):
    def setup_ui(self):
        
        self.resize(QSize(800, 800))

        self.root_layout = QVBoxLayout()

        self.frame_titulo = QFrame()
        self.frame_titulo.setStyleSheet("background: black")
        self.frame_inputs = QFrame()
        self.frame_inputs.setStyleSheet("background: black")

        self.root_layout.addWidget(self.frame_titulo, 30)
        self.root_layout.addWidget(self.frame_inputs, 70)

        self.widget = QWidget()
        self.widget.setLayout(self.root_layout)

        self.setCentralWidget(self.widget)


#Ejecutar la aplicacion
    
import sys

app = QApplication(sys.argv)
menu = Menu()
menu.setup_ui()
menu.show()

sys.exit(app.exec())