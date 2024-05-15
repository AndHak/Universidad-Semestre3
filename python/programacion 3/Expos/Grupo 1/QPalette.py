from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys, os

basedir = os.path.dirname(__file__)

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.styles_setup()
        # self.resize(300, 300)
        
    def styles_setup(self):
        self.setWindowTitle("Ejemplo QPalette")
        
        v_layout = QVBoxLayout()
        
        lbl_text = QLabel('Texto')
        lbl_text.setFont(QFont('Arial', 20)) 
        lbl_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(lbl_text)
        
        line_text = QLineEdit()
        line_text.setPlaceholderText('Placeholder')
        line_text.setDisabled(True)
        v_layout.addWidget(line_text)
        btn = QPushButton('Click')
        v_layout.addWidget(btn)
        
        self.setLayout(v_layout)
        
        # setColor()----------------------------------------------------------
        self.init_style()

    def init_style(self):
        new_palette = QPalette()
        new_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, 'red')
        new_palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, 'blue')
        new_palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, 'green')        
        new_palette.setColor(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, 'lightgray')
        
        print(f'\nColor paleta en rol especifico: {new_palette.color(QPalette.ColorRole.Window)}') # Retorna el color de la paleta para un rol especifico en formato RGB
        brush = new_palette.brush(QPalette.ColorRole.WindowText)
        brush.setColor('red')
        new_palette.setBrush(QPalette.ColorRole.WindowText, brush)
        
        # new_palette.setCurrentColorGroup(QPalette.ColorGroup.Active)
        print(f'Pincel seteado: {new_palette.isBrushSet(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText)}')
        print(f'Color group:  {new_palette.currentColorGroup()}')
        self.setPalette(new_palette)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    app.exec()