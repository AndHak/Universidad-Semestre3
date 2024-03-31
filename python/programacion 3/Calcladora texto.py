from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMessageBox, QLabel, QLineEdit
from PySide6.QtGui import QFont 
from PySide6.QtCore import Qt
import re
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 350, 250)

        label = QLabel(self)
        label.setText("RESULTADO")
        label.setFont(QFont("Arial", 20))
        label.move(160,10)

        num1 = QLabel(self)
        num1.setText("Numero 1")
        num1.setFont(QFont("Arial", 10))
        num1.move(10,10)

        self.num1_input = QLineEdit(self)
        self.num1_input.resize(120,20)
        self.num1_input.move(5,30)

        num2 = QLabel(self)
        num2.setText("Numero 2")
        num2.setFont(QFont("Arial", 10))
        num2.move(10,60)

        self.num2_input = QLineEdit(self)
        self.num2_input.resize(120,20)
        self.num2_input.move(5,80)

        operacion = QLabel(self)
        operacion.setText("Operacion")
        operacion.setFont(QFont("Arial", 10))
        operacion.move(10,120)

        self.operacion = QLineEdit(self)
        self.operacion.resize(120,20)
        self.operacion.move(5,140)

        button = QPushButton(self)
        button.setText("CALCULAR")
        button.setFont(QFont("Arial", 10))
        button.resize(120,30)
        button.move(5,220)
        button.clicked.connect(self.calcular)

        self.label_resultado = QLabel(self)
        self.label_resultado.setText("")
        self.label_resultado.setFont(QFont("Arial", 15))
        self.label_resultado.move(130,50)
        self.label_resultado.resize(220,100)
        self.label_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)


    def validar_numero(self, texto):
        try:
            float(texto)  # Intenta convertir el texto a un número flotante
            return True
        except ValueError:
            try:
                int(texto)  # Intenta convertir el texto a un número entero
                return True
            except ValueError:
                return False

    def calcular(self):
        num1 = self.num1_input.text()
        num2 = self.num2_input.text()
        operacion = self.operacion.text()

        if self.validar_numero(num1) and self.validar_numero(num2) and operacion.strip():  
            num1final = float(num1)  # Convertir siempre a flotante
            num2final = float(num2)  # Convertir siempre a flotante
            operacionf = re.sub(r'\s', '', operacion).lower()
                
            if operacionf == "suma" or operacionf == "+":
                resultado = num1final + num2final
                self.label_resultado.setText(str(resultado))

            elif operacionf == "resta" or operacionf == "-":
                resultado = num1final - num2final
                self.label_resultado.setText(str(resultado))

            elif operacionf == "multi" or operacionf == "*":
                resultado = num1final * num2final
                self.label_resultado.setText(str(resultado))

            elif operacionf == "divi" or operacionf == "/":
                if num2final != 0:
                    resultado = num1final / num2final
                    self.label_resultado.setText(str(resultado))
                else:
                    self.label_resultado.setText("División entre 0\nno soportada")

            elif operacionf == "potencia" or operacionf == "^":
                resultado = num1final ** num2final
                self.label_resultado.setText(str(resultado))

            else:
                self.label_resultado.setText("La operación digitada\nno existe")
            
            self.label_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    
        else:
             self.label_resultado.setText("Los tipos de datos\ningresados son\nincorrectos")
             self.label_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
        
                                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())