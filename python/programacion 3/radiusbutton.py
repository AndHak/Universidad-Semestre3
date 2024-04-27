from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QWidget, QCheckBox
from PySide6.QtGui import QPixmap
import sys

class Main(QMainWindow):
    cajas = []

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nombre app")
        icon_image = r"direccion del png"  # Asegurate de poner la dirección correcta aquí
        self.icon_window = QPixmap(icon_image)
        self.setWindowIcon(self.icon_window)

        self.resize(800, 800)
        self.root_layout = QVBoxLayout()

        self.frame_principal = QFrame()
        self.root_layout.addWidget(self.frame_principal)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

        self.create_checkboxes()

    def create_checkboxes(self):
        self.hvox = QVBoxLayout()
        self.frame_principal.setLayout(self.hvox)

        self.partialcheck = QCheckBox("Todos los colores")
        self.partialcheck.stateChanged.connect(self.verificar)
        self.hvox.addWidget(self.partialcheck)

        colors = ["Azul", "Rojo", "Amarillo"]
        for color in colors:
            checkbox = QCheckBox(color)
            self.cajas.append(checkbox)
            checkbox.stateChanged.connect(self.cambiar)
            self.hvox.addWidget(checkbox)

    def verificar(self, state):
        new_state = Qt.Checked if state == Qt.Checked else Qt.Unchecked
        for checkbox in self.cajas:
            checkbox.setCheckState(new_state)

    def cambiar(self):
        total = len(self.cajas)
        checked = sum(1 for box in self.cajas if box.isChecked())
        
        if checked == 0:
            self.partialcheck.setChecked(False)
        elif checked == total:
            self.partialcheck.setChecked(True)
        else:
            self.partialcheck.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
