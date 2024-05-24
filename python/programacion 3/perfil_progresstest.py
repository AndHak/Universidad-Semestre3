import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QProgressBar, QTextEdit, QMessageBox
from PySide6.QtCore import QThread, Signal

class PrimeWorker(QThread):
    progressChanged = Signal(int)
    resultReady = Signal(list)

    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        primes = []
        is_prime = [True] * (self.n + 1)
        for p in range(2, self.n + 1):
            if is_prime[p]:
                primes.append(p)
                for i in range(p * p, self.n + 1, p):
                    is_prime[i] = False
            self.progressChanged.emit(int(p / self.n * 100))
        self.resultReady.emit(primes)

class PrimeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Criba de Eratóstenes con QProgressBar')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.inputLineEdit = QLineEdit(self)
        self.inputLineEdit.setPlaceholderText("Ingrese un número límite")
        
        self.startButton = QPushButton("Calcular Primos", self)
        self.startButton.clicked.connect(self.startCalculation)
        
        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        
        self.resultTextEdit = QTextEdit(self)
        self.resultTextEdit.setReadOnly(True)

        layout.addWidget(self.inputLineEdit)
        layout.addWidget(self.startButton)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.resultTextEdit)

        self.setLayout(layout)

    def startCalculation(self):
        try:
            n = int(self.inputLineEdit.text())
            if n < 2:
                raise ValueError("El número debe ser mayor que 1")
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        self.progressBar.setValue(0)
        self.resultTextEdit.clear()

        self.worker = PrimeWorker(n)
        self.worker.progressChanged.connect(self.progressBar.setValue)
        self.worker.resultReady.connect(self.displayResults)
        self.worker.start()

    def displayResults(self, primes):
        self.resultTextEdit.append("Números primos encontrados:")
        self.resultTextEdit.append(", ".join(map(str, primes)))
        self.progressBar.setValue(100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = PrimeCalculator()
    calculator.show()
    sys.exit(app.exec())
