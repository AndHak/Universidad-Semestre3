from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from Calculadora3styles import *
import sys
import math

class Main(QMainWindow):

    s = [["C", "(", ")", "mod", "π"], 
        ["7", "8", "9", "÷", "√"],  
        ["4", "5", "6", "×", "x²"],  
        ["1", "2", "3", "−", "="], 
        ["0", ".", "%", "+"]] 
    
    resultado = False
    operation = None
    
    def __init__(self):
        super().__init__()
 
        self.resize(QSize(600, 400))
        #Nombre Ventana
        self.setWindowTitle("Calculadora pro")

        #Icono ventana
        incon_image = r"python\programacion 3\images\calculadora icon.png"
        self.icon_window = QPixmap(incon_image)
        self.setWindowIcon(self.icon_window)

        self.root_layout = QVBoxLayout()
        
        self.frame_operaciones = QFrame()
        self.frame_operaciones.setStyleSheet("background: #ffffff")

        self.frame_buttons_calculator = QFrame()

        #Agregar los frames al layout como widgets
        self.root_layout.addWidget(self.frame_operaciones, 30)
        self.root_layout.addWidget(self.frame_buttons_calculator, 70)

        #Establecer un widget principal
        self.widget = QWidget()
        self.widget.setLayout(self.root_layout)
        self.setCentralWidget(self.widget)

        self.digital_operaciones()
        self.buttons_calculator()
        self.buttons_layout.setSpacing(10) 


    def digital_operaciones(self):
        self.setStyleSheet(estilos_labels)
        self.history_label = QLabel()
        self.history_label.setText("")
        self.history_label.setStyleSheet("""
                                font-size: 25px;
                                font-family: DS-Digital;
                                """)

        self.current_label = QLabel()
        self.current_label.setText("")
        self.current_label.setStyleSheet("""
                                font-size: 40px;
                                font-weight: bold;
                                font-family: DS-Digital;

                                """)
        
        self.history_label.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        self.current_label.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight) 

        self.labels_layout = QVBoxLayout()

        labels_list = [self.history_label, self.current_label]
        for label in labels_list:
            self.labels_layout.addWidget(label)
            self.labels_layout.addSpacing(10)
        
        self.frame_operaciones.setLayout(self.labels_layout)
    
            
    def add_calculator_button(self, i, j, s):
        button = QPushButton(s)
        button.setStyleSheet(estilos_buttons)

        if s == "=":
            button.setObjectName("igual")
            button.clicked.connect(lambda: self.igual())
            self.buttons_layout.addWidget(button, i, j, 2, 1)  
        else:
            self.buttons_layout.addWidget(button, i, j)


        if s.isnumeric() or s == ".":
            button.clicked.connect(lambda: self.append_current_text(s))
        elif s == "C":
            button.clicked.connect(lambda: self.clear_entry())
        elif s == "(":
            button.clicked.connect(lambda: self.abrir_parentesis())
        elif s == ")":
            button.clicked.connect(lambda: self.cerrar_parentesis())
        elif s == "π":
            button.clicked.connect(lambda: self.poner_pi())
        elif s in ["%", "mod", "x²", "√", "÷", "×", "−", "+"]:
            button.clicked.connect(lambda: self.move_to_history(s))
        elif s in ["="]:
            button.setObjectName("igual")
            button.clicked.connect(lambda: self.igual())

    def buttons_calculator(self):
        self.buttons_layout = QGridLayout() 

        for i in range(len(self.s)):  # Iterate over rows
            for j in range(len(self.s[i])):  # Iterate over columns in each row
                self.add_calculator_button(i + 1, j + 1, self.s[i][j])

        self.frame_buttons_calculator.setLayout(self.buttons_layout)

    #Agregar texto a current label
    def append_current_text(self, text):
        if self.resultado:
            self.clear_entry()
            self.resultado = False
        self.current_text = self.current_label.text()
        self.current_label.setText(self.current_text + text)
        
        

    # Agrega el texto actual al history_label
    def move_to_history(self, operation):
        self.resultado = False
        self.history_label.setText(self.current_label.text() + f" {operation}")
        # Limpia el current_label para el siguiente número
        self.current_label.setText("")


        if operation == "%":
            num1 = self.history_label.text().split()[0]
            self.funcion_porcentaje(num1)

        elif operation == "x²":
            num1 = self.history_label.text().split()[0]
            self.funcion_potencia_a_la_n(num1, 2)

        elif operation == "√":
            num1 = self.history_label.text().split()[0]
            self.funcion_raiz(num1)
        
        elif operation == "xⁿ":
            num1 = self.history_label.text().split()[0]
            return
        
        elif operation == "÷":
            num1 = self.history_label.text().split()[0]
            return
            
        elif operation == "×":
            num1 = self.history_label.text().split()[0]
            return
        
        elif operation == "−":
            num1 = self.history_label.text().split()[0]
            return
        
        elif operation == "+":
            num1 = self.history_label.text().split()[0]
            return


    def igual(self):

        operation = str(self.history_label.text().split()[-1])
        num1 = float(self.history_label.text().split()[0])
        num2 = float(self.current_label.text())


        if operation == "xⁿ":
            self.funcion_potencia_a_la_n(num1, num2)
            
        elif operation == "÷":
            self.funcion_division(num1, num2)

        elif operation == "×":
            self.funcion_producto(num1, num2)

        elif operation == "−":
            self.funcion_resta(num1, num2)

        elif operation == "+":
            self.funcion_suma(num1, num2)


        
    #Borra todo
    def clear_entry(self):
        self.history_label.setText("")
        self.current_label.setText("")
        self.resultado = False

    def funcion_porcentaje(self, num1):
        porcentaje = float(num1)/100
        self.current_label.setText(f"{porcentaje}")
        self.resultado = True

    def funcion_potencia_a_la_n(self, num1, num2):
        resultado = float(num1)* float(num2)
        self.history_label.setText(f"{num1}^{num2}")
        self.current_label.setText(f"{resultado}")
        self.resultado = True

    def funcion_raiz(self, num1):
        resultado = math.sqrt(float(num1))
        self.history_label.setText(f"{num1} √")
        self.current_label.setText(f"{resultado}")
        self.resultado = True

    def funcion_division(self, num1, num2):
        if float(num2) == 0:
            self.history_label.setText("")
            self.current_label.setText("ERROR")
            self.resultado = True
        else:
            resultado = float(num1)/float(num2)
            resultado = str(resultado)
            self.history_label.setText(f"{num1} ÷ {num2}")
            self.current_label.setText(resultado)
            self.resultado = True

    def funcion_suma(self, num1, num2):
        resultado = float(num1) + float(num2)
        resultado = str(resultado)
        self.history_label.setText(f"{num1} + {num2}")
        self.current_label.setText(resultado)
        self.resultado = True

    def funcion_resta(self, num1, num2):
        resultado = float(num1) - float(num2)
        resultado = str(resultado)
        self.history_label.setText(f"{num1} − {num2}")
        self.current_label.setText(resultado)
        self.resultado = True

    def funcion_producto(self, num1, num2):
        resultado = float(num1) * float(num2)
        resultado = str(resultado)
        self.history_label.setText(f"{num1} × {num2}")
        self.current_label.setText(resultado)
        self.resultado = True

    def abrir_parentesis(self):
        self.append_current_text('(')

    def cerrar_parentesis(self):
        self.append_current_text(')')
    
    def poner_pi(self):
        self.append_current_text('3.1416')

        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
