from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys, os

basedir = os.path.dirname(__file__)

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.styles_setup()
        self.resize(300, 300)
        
    def styles_setup(self):
        self.setWindowTitle("Ejemplo Style")
        
        grid_l = QGridLayout()
        # --------------------------------------------------
        
        login_lbl = QLabel('Login')
        # login_lbl.setStyleSheet('''QLabel {
        #                                 color: blue;
        #                                 font-size: 25px;
        #                                 font-weight: bold;
        #                                 qproperty-alignment: 'AlignCenter';
        #                             }''')
        # login_lbl.setObjectName('login_label')
        grid_l.addWidget(login_lbl, 0, 0, 3, 10)
        
        # self.setStyleSheet('''QWidget {background-color: White }''')
        
        lbl_user = QLabel('Usuario: ')
        # lbl_user.setStyleSheet('''QLabel {
        #                     color: blue;
        #                     font-family: "Algerian";
        #                     font-size: 16px;
        #                     font-weight: bold;
        #                     qproperty-alignment: 'AlignCenter';
        #                 }''')
        line_user = QLineEdit()
        # line_user.setStyleSheet('''QLineEdit {
        #                             background-color: lightgray;
        #                             border: 2px solid gray;
        #                             border-radius: 5px;
        #                             padding: 5px;
        #                             font-size: 14px;
        #                         }
        #                         QLineEdit:focus {
        #                             border: 2px solid blue;
        #                             background-color: white;
        #                         }''')
        grid_l.addWidget(lbl_user, 4, 0, 2, 5)
        grid_l.addWidget(line_user, 4, 5, 2, 5)
        
        
        lbl_pass = QLabel('Contraseña: ')
        # lbl_pass.setStyleSheet('''QLabel {
        #                                 color: blue;
        #                                 font-size: 16px;
        #                                 font-weight: bold;
        #                                 qproperty-alignment: 'AlignCenter';
        #                             }''')
        line_pass = QLineEdit()
        # line_pass.setStyleSheet('''QLineEdit {
        #                             background-color: lightgray;
        #                             border: 2px solid gray;
        #                             border-radius: 5px;
        #                             padding: 5px;
        #                             font-size: 14px;
        #                         }
        #                         QLineEdit:focus {
        #                             border: 2px solid green;
        #                             background-color: white;
        #                         }''')
        grid_l.addWidget(lbl_pass, 6, 0, 2, 5)
        grid_l.addWidget(line_pass, 6, 5, 2, 5)
        
        btn_login = QPushButton('Iniciar Secion')
        # btn_login.setStyleSheet('''QPushButton {
        #                             background-color: lightgray;
        #                             border: 1px solid gray;
        #                             border-radius: 10px;
        #                             padding: 10px;
        #                             font-size: 14px;
        #                         }
        #                         QPushButton:hover {
        #                             background-color: green;
        #                             color: white;
        #                         }
        #                         QPushButton:pressed {
        #                             background-color: red;
        #                             color: white;
        #                         }''')
        grid_l.addWidget(btn_login, 8, 0, 3, 10)
        
        self.setLayout(grid_l)
        
        self.cargar_estilos()

    def cargar_estilos(self):
        try:
            with open("styles.qss", "r") as arc_styles:
                self.setStyleSheet(arc_styles.read())
        except FileNotFoundError:
            print("Archivo de estilos no encontrado.")
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    app.exec()