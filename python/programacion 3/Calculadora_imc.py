from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
                QLabel {
                    color: gray;
                    font-size: 15px;
                    font-family: Arial;
                } 
                
                QLineEdit {
                    border: 2px solid gray;
                    border-radius: 5px;
                    height: 30px;
                    width: 200px;
                }
                           
                QPushButton {
                    height: 30px;
                    width: 260px;
                    font-size: 15px;
                }
                """)

        self.setWindowTitle("Calculadora IMC")
        self.setGeometry(100, 100, 400, 300)

        self.imc_name = QLabel(self)
        self.imc_name.setText("IMC =>")
        self.imc_name.move(10, 20)

        self.genero_name = QLabel(self)
        self.genero_name.setText("Género:")
        self.genero_name.move(10, 60)

        self.altura_name = QLabel(self)
        self.altura_name.setText("Altura:")
        self.altura_name.move(10, 100)

        self.peso_name = QLabel(self)
        self.peso_name.setText("Peso:")
        self.peso_name.move(10, 140)

        # line edits
        self.imc_line_edit = QLineEdit(self)
        self.imc_line_edit.setPlaceholderText("No calculado")
        self.imc_line_edit.move(70, 12)

        self.genero_line_edit = QLineEdit(self)
        self.genero_line_edit.setPlaceholderText("M/F")
        self.genero_line_edit.move(70, 52)

        self.altura_line_edit = QLineEdit(self)
        self.altura_line_edit.setPlaceholderText("metros")
        self.altura_line_edit.move(70, 92)
        self.altura_line_edit.textChanged.connect(self.reset_altura_style)

        self.peso_line_edit = QLineEdit(self)
        self.peso_line_edit.setPlaceholderText("kilogramos")
        self.peso_line_edit.move(70, 132)
        self.peso_line_edit.textChanged.connect(self.reset_peso_style)

        #Boton
        self.boton_calcular = QPushButton(self)
        self.boton_calcular.setText("Calcular")
        self.boton_calcular.move(10, 172)
        self.boton_calcular.clicked.connect(self.altura_y_peso_true)

    def altura_y_peso_true(self):
        altura_text = self.altura_line_edit.text()
        peso_text = self.peso_line_edit.text()

        try:
            altura = float(altura_text)
        except ValueError:
            self.altura_line_edit.setStyleSheet("border: 2px solid red;")
            return
        
        try:
            peso = float(peso_text)
        except ValueError:
            self.peso_line_edit.setStyleSheet("border: 2px solid red;")
            return
        
        if altura <= 0:
            self.altura_line_edit.setStyleSheet("border: 2px solid red;")
        else:
            self.altura_line_edit.setStyleSheet("")
        
        if peso <= 0:
            self.peso_line_edit.setStyleSheet("border: 2px solid red;")
        else:
            self.peso_line_edit.setStyleSheet("")

        self.genero_verify()

    def genero_verify(self):
        genero_text = self.genero_line_edit.text().strip().lower()
        if genero_text == "m" or genero_text == "masculino":
            self.calcular_imc_masculino()
        elif genero_text == "f" or genero_text == "femenino":
            self.calcular_imc_femenino()
        else:
            self.genero_line_edit.setText("?")
            self.calcular_imc_sin_genero()

    def calcular_imc_sin_genero(self):
        altura = float(self.altura_line_edit.text())
        peso = float(self.peso_line_edit.text())
        imc = peso / (altura ** 2)
        self.imc_line_edit.setText(f"{imc:.2f} - N/D")

    def calcular_imc_masculino(self):
        altura = float(self.altura_line_edit.text())
        peso = float(self.peso_line_edit.text())
        imc = peso / (altura ** 2)
        if imc < 20:
            self.imc_line_edit.setText(f"{imc:.2f} - Desnutrición")
        elif imc >= 20 and imc < 25:
            self.imc_line_edit.setText(f"{imc:.2f} - Normalidad")
        elif imc >= 25 and imc < 30:
            self.imc_line_edit.setText(f"{imc:.2f} - Sobrepeso")
        elif imc >= 30 and imc <= 40:
            self.imc_line_edit.setText(f"{imc:.2f} - Obesidad")
        elif imc > 40:
            self.imc_line_edit.setText(f"{imc:.2f} - Obesidad Grave")
 
        
    def calcular_imc_femenino(self):
        altura = float(self.altura_line_edit.text())
        peso = float(self.peso_line_edit.text())
        imc = peso / (altura ** 2)
        if imc < 19:
            self.imc_line_edit.setText(f"{imc:.2f} - Desnutrición")
        elif imc >= 19 and imc < 24:
            self.imc_line_edit.setText(f"{imc:.2f} - Normalidad")
        elif imc >= 24 and imc < 28:
            self.imc_line_edit.setText(f"{imc:.2f} - Sobrepeso")
        elif imc >= 28 and imc <= 32:
            self.imc_line_edit.setText(f"{imc:.2f} - Obesidad")
        elif imc > 32:
            self.imc_line_edit.setText(f"{imc:.2f} - Obesidad Grave")


    def reset_altura_style(self):
        self.altura_line_edit.setStyleSheet("")
    def reset_peso_style(self):
        self.peso_line_edit.setStyleSheet("")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
