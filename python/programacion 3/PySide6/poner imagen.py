from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont

import sys

class MainWindow(QWidget):

    colores = {
        "gris_suave": (213,211,221),
        "beige": (239,208,199),
        "negro": (0,0,0)
    }

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicativo 2")
        self.setFixedSize(1280, 720)

        label = QLabel(self)
        label.setGeometry(0, 0, 1280, 720)  # Set the geometry of the label
        font = QFont()
        label.setFont(font)  # Set the font
        label.setAlignment(Qt.AlignmentFlag.AlignBottom
                           |Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(f"""
            color: rgb{self.colores['negro']};
            font-size: 30px;
            font-weight: bold;
            """)
        label.setText("Bienvenidos")  # Set the text

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
