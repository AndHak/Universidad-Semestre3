from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from datetime import datetime
import os
import sys

#sebastian david ordoñez bolaños  codigo: 223034072


# class MainWindow(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("")





#     def validar_correo_electronico(self, correo):
#         try:
#             # Usamos la función validate_email para validar el correo electrónico
#             validador = validate_email(correo)
#             # Si la dirección es válida, devuelve True
#             return True
#         except EmailNotValidError:
#             # Si ocurre un error, significa que la dirección no es válida, entonces devuelve False
#             return False


class FabricaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.ventanas = QStackedLayout()
        self.setWindowTitle("Ejercicio Fabrica")

        self.principal()
        
        self.setLayout(self.ventanas)

    def principal(self):
        widget = QWidget(self)
        layout = QVBoxLayout()

        groupbox_idim = QGroupBox('Escoja el material que desee adquirir')
        vbox_group_idim = QVBoxLayout()
        vbox_group_idim.setSpacing(0)
        # Creamos los checkboxes
        self.radio_madera = QRadioButton('Madera')
        self.radio_aluminio = QRadioButton('Aluminio')
        self.radio_vidrio = QRadioButton('Vidrio')
        # Añadimos los checkboxes al grupo
        vbox_group_idim.addWidget(self.radio_madera)
        vbox_group_idim.addWidget(self.radio_aluminio)
        vbox_group_idim.addWidget(self.radio_vidrio)
        groupbox_idim.setLayout(vbox_group_idim)

        self.peso_input = QLineEdit()
        self.piezas_input = QLineEdit()

        
        layout.addWidget(QLabel('Peso por pieza (Kg):'))
        layout.addWidget(self.peso_input)
        layout.addWidget(QLabel('Número de Piezas:'))
        layout.addWidget(self.piezas_input)
        layout.addWidget(groupbox_idim)
        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        self.calcular_btn = QPushButton('Calcular')
        self.calcular_btn.clicked.connect(self.calcular)
        layout.addWidget(self.calcular_btn)

        widget.setLayout(layout)
        self.ventanas.addWidget(widget)

    
    def secundario(self):
        widget = QWidget(self)
        layout = QVBoxLayout()
        peso_por_pieza_text = self.peso_input.text().strip()
        piezas_text = self.piezas_input.text().strip()
        peso = float(peso_por_pieza_text)
        piezas = int(piezas_text)

        material = None
        if self.radio_madera.isChecked():
            material = 'Madera'
        elif self.radio_aluminio.isChecked():
            material = 'Aluminio'
        elif self.radio_vidrio.isChecked():
            material = 'Vidrio'

        peso_total = piezas * peso

        label = QLabel(self)
        label.setText(f'Piezas de {material}: {piezas}\n'
                                  f'Total de piezas procesadas: {piezas}\n'
                                  f'Total de peso de {material}: {peso} Kg\n'
                                  f'Total de peso de todas las piezas: {peso_total} Kg')
        label.setFont(QFont("Courier", 10))  # Establecer la fuente a Courier, tamaño 10

        layout.addWidget(label)
        
        
        widget.setLayout(layout)
        self.ventanas.addWidget(widget)

    def calcular(self):
        # Validación de campos de entrada
        peso_por_pieza_text = self.peso_input.text().strip()
        piezas_text = self.piezas_input.text().strip()

        if not peso_por_pieza_text or not piezas_text:
            self.result_label.setText("'Error', 'Por favor, completa todos los campos pedidos.'")
            return

        else:
            try:
                peso_por_pieza = float(peso_por_pieza_text)
                piezas = int(piezas_text)
            except ValueError:
                self.result_label.setText("'Error', 'Por favor, ingresa numeros enteros .'")
                return
            else:
                # Validación de selección de radio buttons
                if not self.radio_madera.isChecked() and not self.radio_aluminio.isChecked() and not self.radio_vidrio.isChecked():
                    self.result_label.setText("'Error', 'Por favor, selecciona un material.'")
                    return
                else:
                    self.secundario()
                    self.ventanas.setCurrentIndex(1)

        
        
        

        


        
if __name__ == "__main__":
    app = QApplication([])
    window = FabricaApp()
    window.show()
    sys.exit(app.exec())