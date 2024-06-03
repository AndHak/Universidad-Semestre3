import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSlider, QLabel, QWidget, QHBoxLayout
from PySide6.QtCore import Qt

class EqualizerBand(QWidget):
    def __init__(self, label, parent=None):
        super().__init__(parent)
        self.initUI(label)

    def initUI(self, label):
        layout = QVBoxLayout()
        self.slider = QSlider(Qt.Vertical)
        self.slider.setRange(-10, 10)
        self.slider.setValue(0)
        self.label = QLabel(label)
        self.value_label = QLabel("0 dB")
        
        self.slider.valueChanged.connect(self.updateValueLabel)

        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.value_label)
        self.setLayout(layout)

    def updateValueLabel(self, value):
        self.value_label.setText(f"{value} dB")

class Equalizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        frequencies = ["32 Hz", "64 Hz", "125 Hz", "250 Hz", "500 Hz", "1 kHz", "2 kHz", "4 kHz", "8 kHz", "16 kHz"]

        self.bands = [EqualizerBand(freq) for freq in frequencies]

        for band in self.bands:
            layout.addWidget(band)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ecualizador")
        self.setGeometry(100, 100, 800, 400)

        self.equalizer = Equalizer()
        self.setCentralWidget(self.equalizer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
