from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QDial, QLabel, QWidget
from PySide6.QtCore import Qt

class Equalizer(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        # Añadir el dial de ganancia
        self.add_gain_dial()

        self.setLayout(self.layout)

    def add_gain_dial(self):
        dial_layout = QVBoxLayout()
        label = QLabel("Ganancia")
        self.dial = QDial()
        self.dial.setMinimum(-10)  # Valor mínimo en dB
        self.dial.setMaximum(10)   # Valor máximo en dB
        self.dial.setValue(0)      # Valor inicial
        self.dial.setNotchesVisible(True)

        # Conectar la señal valueChanged al slot update_gain
        self.dial.valueChanged.connect(self.update_gain)

        dial_layout.addWidget(label)
        dial_layout.addWidget(self.dial)
        self.layout.addLayout(dial_layout)

    def update_gain(self):
        # Obtener el valor actual del dial
        current_value = self.dial.value()
        # Verificar si el dial está en el límite superior o inferior
        if current_value == 10:
            self.dial.blockSignals(True)  # Bloquear las señales del dial para evitar cambios
        elif current_value == -10:
            self.dial.blockSignals(True)  # Bloquear las señales del dial para evitar cambios
        else:
            self.dial.blockSignals(False)  # Desbloquear las señales del dial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Equalizer with Gain Dial")
        self.setGeometry(100, 100, 400, 200)

        # Crear el widget Equalizer y establecerlo como el central
        self.equalizer = Equalizer()
        self.setCentralWidget(self.equalizer)

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
