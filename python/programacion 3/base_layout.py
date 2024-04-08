from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nombre app")

        icon_image = r"direccion del png"
        self.icon_window = QPixmap(icon_image)
        self.setWindowIcon(self.icon_window)

        self.resize(QSize(800, 800))

        self.root_layout = QVBoxLayout()

        self.frame_principal = QFrame()
        self.frame_principal.setStyleSheet("background: #252938")

        self.root_layout.addWidget(self.frame_principal, 100)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exit(app.exec())