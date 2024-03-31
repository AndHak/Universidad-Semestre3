from PySide6.QtCore import Qt

from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QLabel, QLineEdit
from PySide6.QtGui import QIcon, QFont
from PySide6 import QtCore
import math
import os
import sys

# problemas con el promedio
# elevacion volverla mas dinamica
#controlar division /0

def apply_dark_theme(app):
    # Define el estilo CSS para el tema oscuro
    dark_stylesheet = """
    * {
        background-color: #19232D;
        color: #F0F0F0;
    }
    QPushButton {
        background-color: #38414B;
        border-style: outset;
        border-width: 2px;
        border-color: #19232D;
        border-radius: 10px;
        padding: 6px;
    }
    QPushButton:hover {
        background-color: #1ABC9C;
        color: #19232D;
    }
    """

    # Aplica el estilo CSS a la aplicación
    app.setStyleSheet(dark_stylesheet)

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        basedir = os.path.dirname(__file__)

        self.input_line = QLineEdit(self)
        self.input_line.setGeometry(5, 5, 215, 125)
        self.input_line.setFont(QFont("Arial", 35))
        self.input_line.setStyleSheet("border: none;")
        self.input_line.setAlignment(QtCore.Qt.AlignmentFlag(10))
        self.input_line.setReadOnly(True)  # Deshabilita la edición directa

        self.setWindowTitle("Calculadora")
        Icon = QIcon(os.path.join(basedir,"img","icon.png"))
        self.setWindowIcon(Icon)
        

        label = QLabel(self)
        label.resize(label.sizeHint())
        

        button1 = QPushButton(self)
        button1.setGeometry(5,300,50,50)
        button1.setFont(QFont("Arial", 15))
        button1.setText("1")
        button1.clicked.connect(lambda: self.append_text("1"))

        button2 = QPushButton(self)
        button2.setGeometry(60,300,50,50)
        button2.setFont(QFont("Arial", 15))
        button2.setText("2")
        button2.clicked.connect(lambda: self.append_text("2"))

        button3 = QPushButton(self)
        button3.setGeometry(115,300,50,50)
        button3.setFont(QFont("Arial", 15))
        button3.setText("3")
        button3.clicked.connect(lambda: self.append_text("3"))
        
        button4 = QPushButton(self)
        button4.setGeometry(5,245,50,50)
        button4.setFont(QFont("Arial", 15))
        button4.setText("4")
        button4.clicked.connect(lambda: self.append_text("4"))

        button5 = QPushButton(self)
        button5.setGeometry(60,245,50,50)
        button5.setFont(QFont("Arial", 15))
        button5.setText("5")
        button5.clicked.connect(lambda: self.append_text("5"))

        button6 = QPushButton(self)
        button6.setGeometry(115,245,50,50)
        button6.setFont(QFont("Arial", 15))
        button6.setText("6")
        button6.clicked.connect(lambda: self.append_text("6"))

        button7 = QPushButton(self)
        button7.setGeometry(5,190,50,50)
        button7.setFont(QFont("Arial", 15))
        button7.setText("7")
        button7.clicked.connect(lambda: self.append_text("7"))

        button8 = QPushButton(self)
        button8.setGeometry(60,190,50,50)
        button8.setFont(QFont("Arial", 15))
        button8.setText("8")
        button8.clicked.connect(lambda: self.append_text("8"))

        button9 = QPushButton(self)
        button9.setGeometry(115,190,50,50)
        button9.setFont(QFont("Arial", 15))
        button9.setText("9")
        button9.clicked.connect(lambda: self.append_text("9"))


        button0 = QPushButton(self)
        button0.setGeometry(60, 355, 50, 50)
        button0.setFont(QFont("Arial", 15))
        button0.setText("0")
        button0.clicked.connect(lambda: self.append_text("0"))

        # Operator buttons
        button_suma = QPushButton(self)
        button_suma.setGeometry(170, 300, 50, 50)
        button_suma.setFont(QFont("Arial", 15))
        button_suma.setText("+")
        button_suma.clicked.connect(lambda: self.append_text("+"))
        

        button_resta = QPushButton(self)
        button_resta.setGeometry(170, 245, 50, 50)
        button_resta.setFont(QFont("Arial", 15))
        button_resta.setText("-")
        button_resta.clicked.connect(lambda: self.append_text("-"))

        button_mult = QPushButton(self)
        button_mult.setGeometry(170, 190, 50, 50)
        button_mult.setFont(QFont("Arial", 15))
        button_mult.setText("*")
        button_mult.clicked.connect(lambda: self.append_text("*"))

        button_div = QPushButton(self)
        button_div.setGeometry(170, 135, 50, 50)
        button_div.setFont(QFont("Arial", 15))
        button_div.setText("/")
        button_div.clicked.connect(lambda: self.append_and_calculate_division("/"))

        button_decimal = QPushButton(self)
        button_decimal.setGeometry(115, 355, 50, 50)
        button_decimal.setFont(QFont("Arial", 15))
        button_decimal.setText(".")
        button_decimal.clicked.connect(lambda: self.append_text("."))

        button_equal = QPushButton(self)
        button_equal.setGeometry(170, 355, 50, 50)
        button_equal.setFont(QFont("Arial", 15))
        button_equal.setText("=")
        button_equal.clicked.connect(self.calculate)

        button_clear_entry = QPushButton(self)
        button_clear_entry.setGeometry(5, 135, 50, 50)
        button_clear_entry.setFont(QFont("Arial", 15))
        button_clear_entry.setText("CE")
        button_clear_entry.clicked.connect(self.clear_entry)

        button_clear_all = QPushButton(self)
        button_clear_all.setGeometry(60, 135, 50, 50)
        button_clear_all.setFont(QFont("Arial", 15))
        button_clear_all.setText("C")
        button_clear_all.clicked.connect(self.clear_all)

        button_porcentaje = QPushButton(self)
        button_porcentaje.setGeometry(5,355,50,50)
        button_porcentaje.setText("%")
        button_porcentaje.setFont(QFont("Arial", 15))
        button_porcentaje.clicked.connect(self.calculate_mod)

        button_potencia = QPushButton(self)
        button_potencia.setGeometry(115,135,50,50)
        button_potencia.setFont(QFont("Arial", 15))
        button_potencia.setText("^2")
        button_potencia.clicked.connect(self.calculate_pow)


    def append_text(self, text):
        current_text = self.input_line.text()
        self.input_line.setText(current_text + text)
        self.input_line.textChanged.connect(self.update_font_size)

    def calculate(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            self.input_line.setText(str(result))
        except Exception as e:
            print("Error:", e)

    def clear_entry(self):
        current_text = self.input_line.text()
        self.input_line.setText(current_text[:-1])

    def clear_all(self):
        self.input_line.clear()

    def calculate_mod(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            result = result / 100  # Calcula el porcentaje
            self.input_line.setText(str(result))
        except Exception as e:
            print("Error:", e)

    def calculate_pow(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            result = math.pow(result, 2)  # Calcula el cuadrado
            self.input_line.setText(str(result))
        except Exception as e:
            print("Error:", e)

    def append_and_calculate_division(self, text):
        current_text = self.input_line.text()
        self.input_line.setText(current_text + text)
        self.calculate_division()

    def calculate_division(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            self.input_line.setText(str(result))
        except ZeroDivisionError:
            self.input_line.setText("/0 no soportada")
        except Exception as e:
            print("Error:", e)
    
    def update_font_size(self):
        text_length = len(self.input_line.text())
        font_size = max(35 - (text_length // 5) * 5, 15)
        font = QFont("Arial", font_size)
        self.input_line.setFont(font)

    
    

if __name__ == "__main__":
    app = QApplication([])
    apply_dark_theme(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())