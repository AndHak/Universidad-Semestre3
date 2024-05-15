import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculadora Básica')
        self.setGeometry(100, 100, 500, 300)
        
        # Establecer el tema "Fusion"
        QApplication.setStyle("Fusion")
        
        # Configurar la paleta personalizada
        self.setCustomPalette()

        # Layout principal vertical
        main_layout = QVBoxLayout()
        
        # Pantalla de resultados
        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("""
                                        border: 2px solid green;
                                        width: 300px;
                                        height: 50px;
                                        background-color: #ffffff;
                                        color: black;
                                        font-size: 35px;
                                        font-family: Ds-digital;""")
        main_layout.addWidget(self.result_display)
        
        # Layout de la cuadrícula para los botones
        grid_layout = QGridLayout()
        
        # Botones numéricos y de operación con iconos
        buttons = [
            ('7', '7.png', 0, 0), ('8', '8.png', 0, 1), ('9', '9.png', 0, 2), ('/', 'divide.png', 0, 3),
            ('4', '4.png', 1, 0), ('5', '5.png', 1, 1), ('6', '6.png', 1, 2), ('*', 'multiply.png', 1, 3),
            ('1', '1.png', 2, 0), ('2', '2.png', 2, 1), ('3', '3.png', 2, 2), ('-', 'subtract.png', 2, 3),
            ('0', '0.png', 3, 0), ('C', 'clear.png', 3, 1), ('=', 'equal.png', 3, 2), ('+', 'add.png', 3, 3)
        ]

        for (text, icon_path, row, col) in buttons:
            button = QPushButton(text)
            button.setIconSize(QSize(24, 24))
            button.setStyleSheet("""background-color: #f0f0f0; color: black; border-radius: 2px;color: black;
                                        font-size: 35px;
                                        font-family: Ds-digital;""")
            if text == "=":
                button.setText("")
                button.setIcon(QIcon(r"C:\Programacion Universidad\Semestre 3\python\programacion 3\Expos\Grupo 1\temas\icons8-equal-50.png"))
                button.setStyleSheet("""background-color: #f0f0f0; color: black; border-radius: 2px;color: black;
                                        font-size: 35px;
                                        font-family: Ds-digital;""")
            if text == "+":
                button.setText("")
                button.setIcon(QIcon(r"C:\Programacion Universidad\Semestre 3\python\programacion 3\Expos\Grupo 1\temas\icons8-plus-50 (1).png")) 
                button.setStyleSheet("""background-color: #f0f0f0; color: black; border-radius: 2px;color: black;
                                        font-size: 35px;
                                        font-family: Ds-digital;""")
            if text == "-":
                button.setText("")
                button.setIcon(QIcon(r"C:\Programacion Universidad\Semestre 3\python\programacion 3\Expos\Grupo 1\temas\icons8-subtract-26.png")) 
                button.setStyleSheet("""background-color: #f0f0f0; color: black; border-radius: 2px;color: black;
                                        font-size: 35px;
                                        font-family: Ds-digital;""")
            if text == "/":
                button.setText("")
                button.setIcon(QIcon(r"C:\Programacion Universidad\Semestre 3\python\programacion 3\Expos\Grupo 1\temas\icons8-division-32.png")) 
                button.setStyleSheet("""background-color: #f0f0f0; color: black; border-radius: 2px;color: black;
                                        font-size: 35px;
                                        font-family: Ds-digital;""")
            if text == "*":
                button.setText("")
                button.setIcon(QIcon(r"C:\Programacion Universidad\Semestre 3\python\programacion 3\Expos\Grupo 1\temas\icons8-x-50.png"))  
                button.setStyleSheet("""background-color: #f0f0f0; color: black; border-radius: 2px;color: black;
                                        font-size: 35px;
                                        font-family: Ds-digital;
                                        """)

            button.clicked.connect(self.on_button_clicked)
            grid_layout.addWidget(button, row, col)
        main_layout.addLayout(grid_layout)

        button_info = QPushButton()
        button_info.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        main_layout.addWidget(button_info)

        self.setLayout(main_layout)

    def setCustomPalette(self):
        custom_palette = QPalette()
        custom_palette.setColor(QPalette.Window, QColor("#333333"))  # Color de fondo de la ventana
        custom_palette.setColor(QPalette.WindowText, QColor("#FFFFFF"))  # Color del texto de la ventana
        custom_palette.setColor(QPalette.Base, QColor("#222222"))  # Color de fondo de los widgets
        custom_palette.setColor(QPalette.AlternateBase, QColor("#444444"))
        custom_palette.setColor(QPalette.ToolTipBase, QColor("#FFFFFF"))
        custom_palette.setColor(QPalette.ToolTipText, QColor("#000000"))
        custom_palette.setColor(QPalette.Text, QColor("#FFFFFF"))
        custom_palette.setColor(QPalette.Button, QColor("#555555"))
        custom_palette.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
        custom_palette.setColor(QPalette.BrightText, QColor("#FF0000"))
        custom_palette.setColor(QPalette.Link, QColor("#2A82DA"))
        custom_palette.setColor(QPalette.Highlight, QColor("#2A82DA"))
        custom_palette.setColor(QPalette.HighlightedText, QColor("#000000"))

        self.setPalette(custom_palette)

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()
        
        if text == 'C':
            self.result_display.clear()
        elif text == '=':
            try:
                result = str(eval(self.result_display.text()))
                self.result_display.setText(result)
            except Exception as e:
                self.result_display.setText("Error")
        else:
            current_text = self.result_display.text()
            new_text = current_text + text
            self.result_display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
